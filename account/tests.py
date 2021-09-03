from django.test import TestCase, Client
from django.contrib.auth.models import User
from .authentication import EmailAuthBackend
from unittest.mock import Mock, patch
from .models import Profile


class UserAccountTest(TestCase):
    def setUp(self) -> None:
        super().setUp()
        self.user = User.objects.create(id=1, username='john', email="john@gmail.com")
        self.user.set_password('john123')
        self.user_profile = Profile.objects.create(user=self.user)

        self.user.save()
        self.user_profile.save()

        self.email_authentication = EmailAuthBackend()

    def tearDown(self) -> None:
        self.user.delete()
        self.user_profile.delete()

    def test_email_authentication(self):

        mock_request = Mock()

        user_none = self.email_authentication.authenticate(mock_request, 'john1@gmail.com', 'john123')
        user_logged_in = self.email_authentication.authenticate(mock_request, 'john@gmail.com', 'john123')

        self.assertIsNone(user_none)
        self.assertTrue(isinstance(user_logged_in, User))
        self.assertEqual(
            [
                user_logged_in.email,
                user_logged_in.username,
            ],
            [
                'john@gmail.com',
                'john',
            ]
        )

    def test_get_logged_user(self):
        user_none = self.email_authentication.get_user(2)
        user_logged_in = self.email_authentication.get_user(1)

        self.assertIsNone(user_none)
        self.assertTrue(isinstance(user_logged_in, User))
        self.assertEqual(
            [
                user_logged_in.email,
                user_logged_in.username,
            ],
            [
                'john@gmail.com',
                'john',
            ]
        )

    @patch('account.authentication.EmailAuthBackend.authenticate', return_value=None)
    def test_email_login(self, mock_authenticate):
        client = Client()
        client.post('/account/login/', {'username': 'john@gmail.com', 'password': 'john123'})

        mock_authenticate.assert_called()


