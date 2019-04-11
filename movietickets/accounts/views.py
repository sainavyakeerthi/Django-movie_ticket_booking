from accounts.forms import RegistrationForm,EditProfile
from django.shortcuts import render,redirect,HttpResponse
from django.contrib.auth.forms import PasswordChangeForm
from django.contrib.auth import update_session_auth_hash

def register(request):
    if request.method =='POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect('accounts/reg_valid.html')
        return redirect('/')
    else:
        form=RegistrationForm()
        args={'form':form}
        return render(request,'accounts/reg_form.html',args)


def view_profile(request):
    args={'user':request.user}
    return render(request,'accounts/profile.html',args)

def edit_profile(request):
    if request.method =='POST':
        form=EditProfile(request.POST,instance=request.user)
        if form.is_valid():
            form.save()
            return redirect('accounts:profile')
    else:
        form=EditProfile(instance=request.user)
        args={'form':form}
        return render(request,'accounts/edit.html',args)


def change_pwd(request):
    if request.method =='POST':
        form=PasswordChangeForm(data=request.POST,user=request.user)
        if form.is_valid():
            form.save()
            update_session_auth_hash(request,form.user)
            return redirect('/accounts/profile')
    else:
        form=PasswordChangeForm(user=request.user)
        args={'form':form}
        return render(request,'accounts/changepwd.html',args)


