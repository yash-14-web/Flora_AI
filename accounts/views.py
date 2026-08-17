from django.shortcuts import render, redirect
from django.contrib.auth import login as auth_login, logout as auth_logout
from django.conf import settings
from django.utils.http import url_has_allowed_host_and_scheme
from .forms import LoginForm, RegistrationForm


def login_view(request):
    """
    Handles user login requests.
    Supports login by username or email and remember-me session persistence.
    """
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    redirect_to = request.POST.get('next') or request.GET.get('next') or ''

    if request.method == 'POST':
        form = LoginForm(request=request, data=request.POST)
        if form.is_valid():
            user = form.get_user()
            auth_login(request, user)

            # Handle Remember Me checkbox
            if form.cleaned_data.get('remember_me'):
                # Persist session across browser sessions (default 2 weeks)
                request.session.set_expiry(1209600)
            else:
                # Browser session only (expires when browser is closed)
                request.session.set_expiry(0)

            # Secure redirect validation
            if redirect_to and url_has_allowed_host_and_scheme(
                url=redirect_to,
                allowed_hosts={request.get_host()},
                require_https=request.is_secure()
            ):
                return redirect(redirect_to)

            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = LoginForm(request=request)

    return render(request, 'pages/login.html', {
        'form': form,
        'next': redirect_to
    })


def register_view(request):
    """
    Handles new user registration requests.
    Creates the user and automatically logs them into their new session.
    """
    if request.user.is_authenticated:
        return redirect(settings.LOGIN_REDIRECT_URL)

    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            user = form.save()
            auth_login(request, user)
            return redirect(settings.LOGIN_REDIRECT_URL)
    else:
        form = RegistrationForm()

    return render(request, 'pages/register.html', {
        'form': form
    })


def logout_view(request):
    """
    Handles user logout and terminates the authenticated session.
    Redirects to the public home page.
    """
    auth_logout(request)
    return redirect(settings.LOGOUT_REDIRECT_URL)
