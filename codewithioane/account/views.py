from django.shortcuts import render, redirect
from account.forms import RegistrationForm, AccountAuthenticateform, AccountUpdateForm
from django.contrib.auth import login, authenticate, logout
from django.contrib.auth.decorators import login_required
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


def login_view(request):
    context ={}
    user = request.user
    if request.POST:
        form = AccountAuthenticateform(request.POST)
        if form.is_valid():
            email = form.cleaned_data['email']
            password = form.cleaned_data['password']
            user = authenticate(request, email=email, password=password)
            login(request, user)
            return redirect('blog:home')
        else:
            context['login_form'] = form
    else:
        form = AccountAuthenticateform()
        context['login_form'] =form
    return render(request, 'Userforms/login.html', context)


@login_required(login_url='/login/')
def account_update_view(request):
    context = {}
    user = request.user
    if request.POST:
        form = AccountUpdateForm(request.POST, instance=user)
        if form.is_valid():
            form.initial = {
                'email':request.POST['email'],
                'username': request.POST['username']
            }
            form.save()
            context['success_message'] = 'Updated'
    else:
        form = AccountUpdateForm(instance=user,
                initial= {
                    'email': request.user.email,
                    'username': request.user.username
                }
        )
    context['account_form'] = form
    return render(request, 'Userforms/account.html', context)
