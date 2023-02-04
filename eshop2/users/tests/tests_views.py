from http import HTTPStatus
from django.core import mail
from django.test import TestCase
from django.urls import reverse

from users.models import MyUser


class RegistrationViewTestCase(TestCase):
    def setUp(self):
        self.valid_data = {
            'first_name': 'Artem',
            'last_name': 'Rodionov',
            'email': 'valid.emai@gmail.com',
            'password1': 'strong_password1317',
            'password2': 'strong_password1317',
        }
        self.path = reverse('account_signup')

    def test_get_request(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Store - Регистрация')
        self.assertTemplateUsed(response, 'users/signup.html')

    def test_registration_with_valid_data(self):
        response = self.client.post(self.path, self.valid_data)

        # check that email has been sent
        self.assertEqual(len(mail.outbox), 1)
        self.assertEqual(mail.outbox[0].to, [self.valid_data['email']])

        # check that a new user has been created
        self.assertTrue(MyUser.objects.count() == 1)
        User = MyUser.objects.first()
        self.assertEqual(User.first_name, self.valid_data['first_name'])

        self.assertRedirects(response, '/')

    def test_registration_with_invalid_data(self):
        invalid_data = self.valid_data
        invalid_data['password2'] = 'any_other'
        self.client.post(self.path, invalid_data)

        # check that email has not been sent
        self.assertEqual(len(mail.outbox), 0)

        # check that a new user has not been created
        self.assertTrue(MyUser.objects.count() == 0)


class LoginViewTestCase(TestCase):
    def setUp(self) -> None:
        self.data = {
            'first_name': 'Artem',
            'last_name': 'Rodionov',
            'email': 'validemai@gmail.com',
            'password': 'strong_password1317',
        }
        MyUser.objects.create_user(**self.data)

        self.login_data = {
            'login': 'validemai@gmail.com',
            'password': 'strong_password1317',
        }

        self.path = reverse('account_login')

    def test_get_request(self):
        response = self.client.get(self.path)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertContains(response, 'Store - Авторизация')
        self.assertTemplateUsed(response, 'users/login.html')

    def test_login_valid_data(self):
        response = self.client.post(self.path, self.login_data, follow=True)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertRedirects(response, '/')

    def test_login_invalid_data(self):
        invalid_login_data = self.login_data
        invalid_login_data['password'] = '1234512345'
        response = self.client.post(self.path, self.login_data, follow=True)

        self.assertEqual(response.status_code, HTTPStatus.OK)
        self.assertIn('E-mail адрес и/или пароль не верны.', response.content.decode())
