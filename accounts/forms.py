from django import forms
from django.contrib.auth import authenticate
from django.contrib.auth.models import User
from django.contrib.auth.password_validation import validate_password
from django.core.exceptions import ValidationError


class LoginForm(forms.Form):
    """
    Form handling user authentication with support for either
    username or email identifier.
    """
    username = forms.CharField(
        label="Username or Email",
        max_length=254,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'id_username',
            'class': 'form-input',
            'placeholder': 'Enter username or email address',
            'autocomplete': 'username',
            'aria-required': 'true'
        })
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'id_password',
            'class': 'form-input',
            'placeholder': 'Enter your password',
            'autocomplete': 'current-password',
            'aria-required': 'true'
        })
    )
    remember_me = forms.BooleanField(
        required=False,
        widget=forms.CheckboxInput(attrs={
            'id': 'id_remember_me'
        })
    )

    def __init__(self, request=None, *args, **kwargs):
        self.request = request
        self.user_cache = None
        super().__init__(*args, **kwargs)

    def clean(self):
        cleaned_data = super().clean()
        username_input = cleaned_data.get('username')
        password = cleaned_data.get('password')

        if username_input and password:
            username_input = username_input.strip()
            resolved_username = username_input

            # Check if identifier is an email address
            if '@' in username_input:
                user_match = User.objects.filter(email__iexact=username_input).first()
                if user_match:
                    resolved_username = user_match.username

            self.user_cache = authenticate(
                self.request,
                username=resolved_username,
                password=password
            )

            if self.user_cache is None:
                raise forms.ValidationError(
                    "Invalid username/email or password. Please check your credentials and try again.",
                    code="invalid_login"
                )
            elif not self.user_cache.is_active:
                raise forms.ValidationError(
                    "This account is currently disabled.",
                    code="inactive"
                )

        return cleaned_data

    def get_user(self):
        return self.user_cache


class RegistrationForm(forms.Form):
    """
    Form handling new user registration with strict validation
    for uniqueness, email format, and password security policies.
    """
    username = forms.CharField(
        label="Username",
        max_length=150,
        required=True,
        widget=forms.TextInput(attrs={
            'id': 'id_reg_username',
            'class': 'form-input',
            'placeholder': 'Choose a username (e.g. greenfarmer)',
            'autocomplete': 'username',
            'aria-required': 'true'
        })
    )
    email = forms.EmailField(
        label="Email Address",
        max_length=254,
        required=True,
        widget=forms.EmailInput(attrs={
            'id': 'id_reg_email',
            'class': 'form-input',
            'placeholder': 'your.email@example.com',
            'autocomplete': 'email',
            'aria-required': 'true'
        })
    )
    password = forms.CharField(
        label="Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'id_reg_password',
            'class': 'form-input',
            'placeholder': 'Create a strong password',
            'autocomplete': 'new-password',
            'aria-required': 'true'
        })
    )
    password_confirm = forms.CharField(
        label="Confirm Password",
        required=True,
        widget=forms.PasswordInput(attrs={
            'id': 'id_reg_password_confirm',
            'class': 'form-input',
            'placeholder': 'Re-enter your password',
            'autocomplete': 'new-password',
            'aria-required': 'true'
        })
    )

    def clean_username(self):
        username = self.cleaned_data.get('username', '').strip()
        if not username:
            raise forms.ValidationError("Username is required.")
        
        # Disallow spaces in username
        if ' ' in username:
            raise forms.ValidationError("Username cannot contain spaces.")

        # Check case-insensitive uniqueness
        if User.objects.filter(username__iexact=username).exists():
            raise forms.ValidationError("A user with this username already exists.")
        
        return username

    def clean_email(self):
        email = self.cleaned_data.get('email', '').strip().lower()
        if not email:
            raise forms.ValidationError("Email address is required.")

        # Check case-insensitive uniqueness
        if User.objects.filter(email__iexact=email).exists():
            raise forms.ValidationError("An account with this email address already exists.")

        return email

    def clean(self):
        cleaned_data = super().clean()
        password = cleaned_data.get('password')
        password_confirm = cleaned_data.get('password_confirm')
        username = cleaned_data.get('username')
        email = cleaned_data.get('email')

        if password and password_confirm:
            if password != password_confirm:
                self.add_error('password_confirm', "Passwords do not match.")

            # Validate against Django password strength validators
            # Create a temporary user instance for validator user attributes comparison
            temp_user = User(username=username or '', email=email or '')
            try:
                validate_password(password, user=temp_user)
            except ValidationError as error:
                for msg in error.messages:
                    self.add_error('password', msg)

        return cleaned_data

    def save(self):
        """
        Creates and persists a new user with securely hashed password.
        """
        username = self.cleaned_data['username']
        email = self.cleaned_data['email']
        password = self.cleaned_data['password']

        user = User.objects.create_user(
            username=username,
            email=email,
            password=password
        )
        return user
