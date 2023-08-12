from django.test import TestCase, Client
from .models import Label
from django.contrib.auth.models import User
from django.urls import reverse_lazy


class LabelBaseTestCase(TestCase):

    fixtures = ['test-label.json', 'test-user.json']

    def setUp(self) -> None:

        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.label1 = Label.objects.get(pk=1)
        self.label2 = Label.objects.get(pk=2)
        self.labels = Label.objects.all()
        self.count = Label.objects.count()


class StatusesTestCase(LabelBaseTestCase):

    def test_list_label(self):

        self.client.force_login(self.user1)

        response = self.client.get(reverse_lazy('labels-index'))
        response_labels = response.context['labels']

        self.assertQuerySetEqual(self.labels,
                                 response_labels.all(),
                                 ordered=False)

    def test_new_label(self):

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('labels-create'), data={
            'label_name': 'New label from Test',
        })

        response = self.client.get(reverse_lazy('labels-index'))
        labels = response.context['labels']
        label = labels.get(id=3)

        self.assertTrue(label.label_name == 'New label from Test')

    def test_update_label(self):

        self.client.force_login(self.user1)
        self.client.post(reverse_lazy('label-update', kwargs={'pk': 1}),
                         data={
                             'label_name': 'SomeLabel12 Updated',
                         })

        response = self.client.get(reverse_lazy('labels-index'))
        labels = response.context['labels']
        label = labels.get(id=1)

        self.assertTrue(label.label_name == 'SomeLabel12 Updated')

    def test_delete_label(self):

        labels = self.client.get(
            reverse_lazy('labels-index')).context['labels']

        self.assertEqual(self.count, labels.count())

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('label-delete', kwargs={'pk': 2}))

        labels = self.client.get(
            reverse_lazy('labels-index')
        ). context['labels']

        self.assertEqual(self.count - 1, labels.all().count())
        self.assertFalse(labels.filter(label_name=self.label2.label_name))
