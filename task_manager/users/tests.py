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
        self.user4 = User.objects.get(pk=4)
        self.users = User.objects.all()
        self.count = User.objects.count()


class UsersTestCase(UserBaseTestCase):

    def test_list_users(self):

        response = self.client.get(reverse_lazy('users-index'))
        response_users = response.context['users']

        self.assertQuerySetEqual(self.users,
                                 response_users.all(),
                                 ordered=False)

    def test_new_user(self):

        self.client.post(reverse_lazy('users-create'), data={
            'username': 'Coworker',
            'first_name': 'Monkey',
            'last_name': 'Belik',
            'password1': 'Chervonec1755',
            'password2': 'Chervonec1755',
        })

        response = self.client.get(reverse_lazy('users-index'))
        users = response.context['users']
        user = users.get(id=5)

        self.assertTrue(user.username == 'Coworker')
        self.assertTrue(user.first_name == 'Monkey')
        self.assertTrue(user.last_name == 'Belik')

    def test_update_user(self):

        self.client.force_login(self.user2)

        self.client.post(reverse_lazy('user-update', kwargs={'pk': 2}),
                         data={
                             'username': 'nekoUpdated',
                             'first_name': 'Nikolay',
                             'last_name': 'Zemelko',
                             'password1': 'Kola1989',
                             'password2': 'Kola1989',
                         })

        response = self.client.get(reverse_lazy('users-index'))
        users = response.context['users']

        user = users.get(id=2)

        self.assertTrue(user.username == 'nekoUpdated')
        self.assertTrue(user.first_name == 'Nikolay')
        self.assertTrue(user.last_name == 'Zemelko')

    def test_delete_user(self):

        users = self.client.get(reverse_lazy('users-index')).context['users']

        self.assertEqual(self.count, users.all().count())

        self.client.force_login(self.user3)

        self.client.post(reverse_lazy('user-delete', kwargs={'pk': 3}))

        users = self.client.get(reverse_lazy('users-index')).context['users']

        self.assertEqual(self.count - 1, users.all().count())
        self.assertFalse(users.filter(username=self.user3.username))
