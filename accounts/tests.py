from django.test import TestCase, Client
from django.urls import reverse
from django.contrib.auth.models import User


class AccountsRegistrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.register_url = reverse('register')
        self.dashboard_url = reverse('dashboard')
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
        self.assertRedirects(response, self.dashboard_url)
        
        # Verify user created in DB
        user = User.objects.filter(username='flora_farmer').first()
        self.assertIsNotNone(user)
        self.assertEqual(user.email, 'farmer@flora.ai')
        self.assertTrue(user.check_password('SecurePlantPassword123!'))

        # Verify user is logged in
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'flora_farmer')

    def test_registration_missing_required_fields(self):
        post_data = {
            'username': '',
            'email': '',
            'password': '',
            'password_confirm': '',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.has_error('username'))
        self.assertTrue(form.has_error('email'))
        self.assertTrue(form.has_error('password'))
        self.assertTrue(form.has_error('password_confirm'))

    def test_registration_invalid_email_format(self):
        post_data = {
            'username': 'farmer_test',
            'email': 'invalid-email-format',
            'password': 'SecurePlantPassword123!',
            'password_confirm': 'SecurePlantPassword123!',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].has_error('email'))

    def test_registration_username_with_spaces(self):
        post_data = {
            'username': 'farmer name with spaces',
            'email': 'farmer.space@flora.ai',
            'password': 'SecurePlantPassword123!',
            'password_confirm': 'SecurePlantPassword123!',
        }
        response = self.client.post(self.register_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(response.context['form'], 'username', 'Username cannot contain spaces.')

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
        self.assertRedirects(response, self.dashboard_url)


class AccountsLoginLogoutTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.dashboard_url = reverse('dashboard')
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
        self.assertRedirects(response, self.dashboard_url)
        self.assertTrue(response.context['user'].is_authenticated)
        self.assertEqual(response.context['user'].username, 'active_farmer')

    def test_login_with_email_success(self):
        post_data = {
            'username': 'ACTIVE@FLORA.AI',  # Case-insensitive email login
            'password': 'HarvestPassword123!',
        }
        response = self.client.post(self.login_url, data=post_data, follow=True)
        self.assertRedirects(response, self.dashboard_url)
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

    def test_login_empty_fields(self):
        post_data = {
            'username': '',
            'password': '',
        }
        response = self.client.post(self.login_url, data=post_data)
        self.assertEqual(response.status_code, 200)
        form = response.context['form']
        self.assertTrue(form.has_error('username'))
        self.assertTrue(form.has_error('password'))

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
        self.assertRedirects(response, self.dashboard_url)


class ProtectedViewsAndFlowIntegrationTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.login_url = reverse('login')
        self.logout_url = reverse('logout')
        self.register_url = reverse('register')
        self.dashboard_url = reverse('dashboard')
        self.detection_url = reverse('detection')
        self.history_url = reverse('history')
        self.profile_url = reverse('profile')
        self.home_url = reverse('home')
        self.user = User.objects.create_user(
            username='flow_farmer',
            email='flow@flora.ai',
            password='HarvestPassword123!'
        )

    def test_unauthenticated_dashboard_redirects_to_login(self):
        response = self.client.get(self.dashboard_url)
        expected_redirect = f"{self.login_url}?next={self.dashboard_url}"
        self.assertRedirects(response, expected_redirect)

    def test_unauthenticated_detection_redirects_to_login(self):
        response = self.client.get(self.detection_url)
        expected_redirect = f"{self.login_url}?next={self.detection_url}"
        self.assertRedirects(response, expected_redirect)

    def test_unauthenticated_history_redirects_to_login(self):
        response = self.client.get(self.history_url)
        expected_redirect = f"{self.login_url}?next={self.history_url}"
        self.assertRedirects(response, expected_redirect)

    def test_unauthenticated_profile_redirects_to_login(self):
        response = self.client.get(self.profile_url)
        expected_redirect = f"{self.login_url}?next={self.profile_url}"
        self.assertRedirects(response, expected_redirect)

    def test_authenticated_dashboard_access_succeeds(self):
        self.client.force_login(self.user)
        response = self.client.get(self.dashboard_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/dashboard.html')

    def test_complete_end_to_end_auth_flow(self):
        # 1. Start at landing page
        landing_res = self.client.get(self.home_url)
        self.assertEqual(landing_res.status_code, 200)

        # 2. Register new user
        reg_data = {
            'username': 'e2e_farmer',
            'email': 'e2e@flora.ai',
            'password': 'E2E_SecurePassword123!',
            'password_confirm': 'E2E_SecurePassword123!',
        }
        reg_res = self.client.post(self.register_url, data=reg_data, follow=True)
        self.assertRedirects(reg_res, self.dashboard_url)
        self.assertTrue(reg_res.context['user'].is_authenticated)

        # 3. Access protected dashboard
        dash_res = self.client.get(self.dashboard_url)
        self.assertEqual(dash_res.status_code, 200)

        # 4. Logout
        logout_res = self.client.get(self.logout_url, follow=True)
        self.assertRedirects(logout_res, self.home_url)
        self.assertFalse(logout_res.context['user'].is_authenticated)

        # 5. Verify protected dashboard cannot be accessed after logout
        blocked_res = self.client.get(self.dashboard_url)
        self.assertRedirects(blocked_res, f"{self.login_url}?next={self.dashboard_url}")

        # 6. Login again with email
        login_data = {
            'username': 'e2e@flora.ai',
            'password': 'E2E_SecurePassword123!',
        }
        login_res = self.client.post(self.login_url, data=login_data, follow=True)
        self.assertRedirects(login_res, self.dashboard_url)
        self.assertTrue(login_res.context['user'].is_authenticated)


class AccountsProfileTests(TestCase):
    def setUp(self):
        self.client = Client()
        self.profile_url = reverse('profile')
        self.login_url = reverse('login')
        self.user = User.objects.create_user(
            username='profile_farmer',
            email='farmer.profile@flora.ai',
            password='ProfilePassword123!',
            first_name='Flora',
            last_name='Grower'
        )
        self.other_user = User.objects.create_user(
            username='other_farmer',
            email='other@flora.ai',
            password='OtherPassword123!',
            first_name='Other',
            last_name='User'
        )

    def test_unauthenticated_profile_access_redirects_to_login(self):
        response = self.client.get(self.profile_url)
        self.assertRedirects(response, f"{self.login_url}?next={self.profile_url}")

    def test_profile_page_renders_with_user_data(self):
        self.client.force_login(self.user)
        response = self.client.get(self.profile_url)
        self.assertEqual(response.status_code, 200)
        self.assertTemplateUsed(response, 'pages/profile.html')
        self.assertIn('form', response.context)
        self.assertEqual(response.context['form']['first_name'].value(), 'Flora')
        self.assertEqual(response.context['form']['last_name'].value(), 'Grower')
        self.assertEqual(response.context['form']['email'].value(), 'farmer.profile@flora.ai')

    def test_profile_update_successful_persists_to_db(self):
        self.client.force_login(self.user)
        update_data = {
            'first_name': 'UpdatedFirst',
            'last_name': 'UpdatedLast',
            'email': 'updated.email@flora.ai',
            'phone': '+1 555 987 6543',
            'organization': 'Flora Agrotech Research',
            'location': 'Northern Agricultural Zone',
            'specialization': 'Plant Virology & Fungal Diagnostics',
            'crop_focus': 'Wheat, Barley, Rice',
            'measurement_unit': 'Imperial',
            'notifications_enabled': 'on',
        }
        response = self.client.post(self.profile_url, data=update_data, follow=True)
        self.assertRedirects(response, self.profile_url)

        # Verify User model updated in DB
        self.user.refresh_from_db()
        self.assertEqual(self.user.first_name, 'UpdatedFirst')
        self.assertEqual(self.user.last_name, 'UpdatedLast')
        self.assertEqual(self.user.email, 'updated.email@flora.ai')

        # Verify UserProfile model updated in DB
        profile = self.user.profile
        self.assertEqual(profile.phone, '+1 555 987 6543')
        self.assertEqual(profile.organization, 'Flora Agrotech Research')
        self.assertEqual(profile.location, 'Northern Agricultural Zone')
        self.assertEqual(profile.specialization, 'Plant Virology & Fungal Diagnostics')
        self.assertEqual(profile.crop_focus, 'Wheat, Barley, Rice')
        self.assertEqual(profile.measurement_unit, 'Imperial')
        self.assertTrue(profile.notifications_enabled)

    def test_profile_update_duplicate_email_rejected(self):
        self.client.force_login(self.user)
        update_data = {
            'first_name': 'Flora',
            'last_name': 'Grower',
            'email': 'other@flora.ai',  # Belongs to other_user
            'phone': '+1 555 000 0000',
            'organization': 'Farm',
            'location': 'Zone',
            'specialization': 'Crops',
            'crop_focus': 'Corn',
            'measurement_unit': 'Metric',
        }
        response = self.client.post(self.profile_url, data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertFormError(
            response.context['form'], 'email',
            'An account with this email address already exists.'
        )

        # Verify user's email was not altered in DB
        self.user.refresh_from_db()
        self.assertEqual(self.user.email, 'farmer.profile@flora.ai')

    def test_profile_update_missing_email_rejected(self):
        self.client.force_login(self.user)
        update_data = {
            'first_name': 'Flora',
            'last_name': 'Grower',
            'email': '',
        }
        response = self.client.post(self.profile_url, data=update_data)
        self.assertEqual(response.status_code, 200)
        self.assertTrue(response.context['form'].has_error('email'))

    def test_user_cannot_access_or_modify_other_user_profile(self):
        # User is logged in as self.user
        self.client.force_login(self.user)
        
        # Profile view must only serve and update self.user's profile
        response = self.client.get(self.profile_url)
        self.assertEqual(response.context['user'], self.user)
        self.assertNotEqual(response.context['user'], self.other_user)

        # Attempt to save updates - must only apply to self.user
        update_data = {
            'first_name': 'SelfOnlyFirst',
            'last_name': 'SelfOnlyLast',
            'email': 'selfonly@flora.ai',
        }
        self.client.post(self.profile_url, data=update_data)
        self.other_user.refresh_from_db()
        self.assertEqual(self.other_user.first_name, 'Other')
        self.assertEqual(self.other_user.email, 'other@flora.ai')

