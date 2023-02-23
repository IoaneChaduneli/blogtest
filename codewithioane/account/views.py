from django.shortcuts import render, redirect
from account.forms import RegistrationForm
from django.contrib.auth import login, authenticate, logout
# Create your views here.

def user_register_view(request):
    context ={}
    if request.POST:
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            email = form.cleaned_data.get('email')
            raw_passoword = form.cleaned_data.get('password1')
            account = authenticate(email=email, password=raw_passoword)
            login(request, account)
            return redirect('blog:home')

        else:
            context['registration_form'] = form

    else:
        form = RegistrationForm()
        context['registration_form'] = form
    return render(request, 'Userforms/register.html', context)


def logout_view(request):
    logout(request)
    return redirect('blog:home')


