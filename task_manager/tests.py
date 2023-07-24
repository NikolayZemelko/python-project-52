from django.test import TestCase, Client
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class UserBaseTestCase(TestCase):

    fixtures = ['test-user.json']

    def setUp(self) -> None:

        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.user2 = User.objects.get(pk=2)
        self.user3 = User.objects.get(pk=3)
        self.users = User.objects.all()
        self.count = User.objects.count()


class UsersTestCase(UserBaseTestCase):

    def test_new_user(self):

        self.client.post(reverse_lazy('users-create'), data={
            'username': self.user1.username,
            'first_name': self.user1.first_name,
            'last_name': self.user1.last_name,
            'password1': self.user1.password,
            'password2': self.user1.password,
        })

        response = self.client.get(reverse_lazy('users'))
        users = response.context['users']
        user = users.get(username='marganezz')

        self.assertTrue(user.username == 'marganezz')
        self.assertTrue(user.first_name == 'Frederic')
        self.assertTrue(user.last_name == 'Baum')

    def test_update_user(self):

        self.client.post(reverse_lazy('users-create'), data={
            'username': self.user2.username,
            'first_name': self.user2.first_name,
            'last_name': self.user2.last_name,
            'password1': self.user2.password,
            'password2': self.user2.password,
        })

        self.client.force_login(self.user2)

        self.client.post(reverse_lazy('user-update', kwargs={'pk': 2}),
                         data={
                             'username': 'neko666',
                             'first_name': 'Nikolay',
                             'last_name': 'Zemelko',
                             'password1': 'Kola1989',
                             'password2': 'Kola1989'
                         })

        response = self.client.get(reverse_lazy('users'))
        users = response.context['users']

        user = users.get(username='neko666')

        self.assertTrue(user.username == 'neko666')
        self.assertTrue(user.first_name == 'Nikolay')
        self.assertTrue(user.last_name == 'Zemelko')

    def test_delete_user(self):

        self.client.post(reverse_lazy('users-create'), data={
            'username': self.user3.username,
            'first_name': self.user3.first_name,
            'last_name': self.user3.last_name,
            'password1': self.user3.password,
            'password2': self.user3.password,
        })

        users = self.client.get(reverse_lazy('users')).context['users']

        self.assertEqual(self.count, users.all().count())

        self.client.force_login(self.user3)
        self.client.post(reverse_lazy('user-delete', kwargs={'pk': 3}))

        users = self.client.get(reverse_lazy('users')).context['users']

        self.assertEqual(2, users.all().count())
