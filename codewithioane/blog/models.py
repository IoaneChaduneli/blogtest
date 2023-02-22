from django.db import models
from django.contrib.auth.models import User
from django.db.models.signals import pre_save, post_delete
from django.utils.text import slugify
from django.dispatch import receiver
# Create your models here.
def upload_location(instance, filename, **kwarfs):
    file_path = 'blog/{author_id}/{title}-{filename}'.format(
                author_id = str(instance.author.id), title =str(instance.title), filename=filename
    )
    return file_path


class BlogPost(models.Model):
    title = models.CharField(max_length=60)
    text = models.TextField()
    author = models.ForeignKey(User, on_delete=models.CASCADE)
    image = models.FileField(blank=False)
    date_create = models.DateTimeField(auto_now_add=True)
    slug = models.SlugField(blank=True, unique=True)


    def __str__(self) -> str:
        return self.title

@receiver(post_delete, sender=BlogPost)
def submission_delete(sender, instance:BlogPost, **kwargs):
    instance.image.delete()


@receiver(pre_save, sender=BlogPost)
def slugify_set(sender, instance:BlogPost, **kwargs):
    if not instance.slug:
        instance.slug = slugify(instance.author + " " + instance.title)
    
