from django.shortcuts import redirect
def Login_redirect(request):
    return redirect('/accounts/login')