from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsRegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.home_url = reverse('home')

    def test_registration_page_renders(self):
        response = self.client.get(self.register_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/register.html')
        self.assertIn('form', response.context)

    def test_successful_registration(self):
        post_data = {
            'username': 'flora_farmer',
            'email': 'farmer@flora.ai',
            'password': 'SecurePlantPassword123!',
            'password_confirm': 'SecurePlantPassword123!',
        }
        response = self.client.post(self.register_url, data=post_data, follow=True)
        self.assertRedirects(response, self.home_url)
        
        # Verify user created in DB
        user = User.objects.filter(username='flora_farmer').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'farmer@flora.ai')
        self.assertTrue(user.check_password('SecurePlantPassword123!'))

        # Verify user is logged in
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'flora_farmer')

    def test_registration_duplicate_username(self):
        User.objects.create_user(username='flora_farmer', email='existing@flora.ai', password='Password123!')
        
        post_data = {
            'username': 'FLORA_FARMER',  # Case-insensitive duplicate
            'email': 'newfarmer@flora.ai',
            'password': 'SecurePlantPassword123!',
            'password_confirm': 'SecurePlantPassword123!',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'username', 'A user with this username already exists.')

    def test_registration_duplicate_email(self):
        User.objects.create_user(username='farmer1', email='farmer@flora.ai', password='Password123!')
        
        post_data = {
            'username': 'farmer2',
            'email': 'FARMER@FLORA.AI',  # Case-insensitive duplicate
            'password': 'SecurePlantPassword123!',
            'password_confirm': 'SecurePlantPassword123!',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'email', 'An account with this email address already exists.')

    def test_registration_password_mismatch(self):
        post_data = {
            'username': 'farmer_mismatch',
            'email': 'mismatch@flora.ai',
            'password': 'Password12345!',
            'password_confirm': 'DifferentPassword12345!',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'password_confirm', 'Passwords do not match.')

    def test_authenticated_user_redirected_from_register(self):
        user = User.objects.create_user(username='auth_user', password='Password123!')
        self.client.force_login(user)
        response = self.client.get(self.register_url)
        self.assertRedirects(response, self.home_url)


class AccountsLoginLogoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.home_url = reverse('home')
        self.user = User.objects.create_user(
            username='active_farmer',
            email='active@flora.ai',
            password='HarvestPassword123!'
        )

    def test_login_page_renders(self):
        response = self.client.get(self.login_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/login.html')
        self.assertIn('form', response.context)

    def test_login_with_username_success(self):
        post_data = {
            'username': 'active_farmer',
            'password': 'HarvestPassword123!',
        }
        response = self.client.post(self.login_url, data=post_data, follow=True)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'active_farmer')

    def test_login_with_email_success(self):
        post_data = {
            'username': 'ACTIVE@FLORA.AI',  # Case-insensitive email login
            'password': 'HarvestPassword123!',
        }
        response = self.client.post(self.login_url, data=post_data, follow=True)
        self.assertRedirects(response, self.home_url)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'active_farmer')

    def test_login_invalid_password(self):
        post_data = {
            'username': 'active_farmer',
            'password': 'WrongPassword!',
        }
        response = self.client.post(self.login_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context['form'], None,
            "Invalid username/email or password. Please check your credentials and try again."
        )

    def test_login_nonexistent_user(self):
        post_data = {
            'username': 'ghost_user',
            'password': 'SomePassword123!',
        }
        response = self.client.post(self.login_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context['form'], None,
            "Invalid username/email or password. Please check your credentials and try again."
        )

    def test_login_remember_me_functionality(self):
        # With remember_me enabled
        post_data = {
            'username': 'active_farmer',
            'password': 'HarvestPassword123!',
            'remember_me': 'on'
        }
        self.client.post(self.login_url, data=post_data)
        self.assertEqual(self.client.session.get_expiry_age(), 1209600)

        # Without remember_me
        self.client.logout()
        post_data_no_remember = {
            'username': 'active_farmer',
            'password': 'HarvestPassword123!',
        }
        self.client.post(self.login_url, data=post_data_no_remember)
        self.assertEqual(self.client.session.get_expire_at_browser_close(), True)

    def test_logout(self):
        self.client.force_login(self.user)
        response = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(response, self.home_url)
        self.assertFalse(response.context['user'].is_authenticated)

    def test_authenticated_user_redirected_from_login(self):
        self.client.force_login(self.user)
        response = self.client.get(self.login_url)
        self.assertRedirects(response, self.home_url)
