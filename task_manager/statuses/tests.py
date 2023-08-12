from django.test import TestCase, Client
from .models import Status
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class StatusBaseTestCase(TestCase):

    fixtures = ['test-status.json', 'test-user.json']

    def setUp(self) -> None:

        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.status1 = Status.objects.get(pk=1)
        self.status2 = Status.objects.get(pk=2)
        self.status3 = Status.objects.get(pk=3)
        self.statuses = Status.objects.all()
        self.count = Status.objects.count()


class StatusesTestCase(StatusBaseTestCase):

    def test_list_status(self):

        self.client.force_login(self.user1)

        response = self.client.get(reverse_lazy('statuses-index'))
        response_statuses = response.context['statuses']

        self.assertQuerySetEqual(self.statuses,
                                 response_statuses.all(),
                                 ordered=False)

    def test_new_status(self):

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('statuses-create'), data={
            'status_name': 'Overrided',
        })

        response = self.client.get(reverse_lazy('statuses-index'))
        statuses = response.context['statuses']
        status = statuses.get(id=4)

        self.assertTrue(status.status_name == 'Overrided')
        self.assertTrue(status.date_of_creation)

    def test_update_status(self):

        self.client.force_login(self.user1)
        self.client.post(reverse_lazy('status-update', kwargs={'pk': 1}),
                         data={
                             'status_name': 'Status 1 Changed',
                         })

        response = self.client.get(reverse_lazy('statuses-index'))
        statuses = response.context['statuses']
        status = statuses.get(id=1)

        self.assertTrue(status.status_name == 'Status 1 Changed')

    def test_delete_status(self):

        statuses = self.client.get(
            reverse_lazy('statuses-index')).context['statuses']

        self.assertEqual(self.count, statuses.all().count())

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('status-delete', kwargs={'pk': 3}))

        statuses = self.client.get(
            reverse_lazy('statuses-index')
        ).context['statuses']

        self.assertEqual(self.count - 1, statuses.all().count())
        self.assertFalse(statuses.filter(status_name=self.status3.status_name))
