from django.test import TestCase, Client
from .models import Task
from django.urls import reverse_lazy
from django.contrib.auth.models import User


class TaskBaseTestCase(TestCase):

    fixtures = ['test-user.json', 'test-status.json', 'test-tasks.json']

    def setUp(self) -> None:

        self.client = Client()
        self.user1 = User.objects.get(pk=1)
        self.task1 = Task.objects.get(pk=1)
        self.task2 = Task.objects.get(pk=2)
        self.tasks = Task.objects.all()
        self.count = Task.objects.count()


class TasksTestCase(TaskBaseTestCase):

    def test_list_tasks(self):

        response = self.client.get(reverse_lazy('tasks-index'))
        response_tasks = response.context['tasks']

        self.assertQuerySetEqual(self.tasks,
                                 response_tasks.all(),
                                 ordered=False)

    def test_new_task_minimum_fields(self):

        self.client.force_login(self.user1)
        self.client.post(reverse_lazy('tasks-create'), data={
            'task_name': 'New Task3',
            'status': 2,
        })

        response = self.client.get(reverse_lazy('tasks-index'))
        tasks = response.context['tasks']
        task = tasks.get(id=3)

        self.assertTrue(task.task_name == 'New Task3')
        self.assertTrue(task.status.status_name == 'New Status2')
        self.assertEqual(self.user1, task.author)
        self.assertIsNone(task.executor)
        self.assertFalse(task.description)
        self.assertFalse(task.labels.all())
        self.assertTrue(self.count + 1 == tasks.count())

    def test_update_task(self):

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('task-update', kwargs={'pk': 1}),
                         data={
                             'task_name': 'Task1 Updated',
                             'description': 'It`s updated task',
                             'status': 2,
                             'executor': 2,
                             'labels': []
                         })

        response = self.client.get(reverse_lazy('tasks-index'))
        tasks = response.context['tasks']

        task = tasks.get(id=1)

        self.assertTrue(task.task_name == 'Task1 Updated')
        self.assertTrue(task.description == 'It`s updated task')
        self.assertTrue(task.status.status_name == 'New Status2')

    def test_delete_task(self):

        tasks = self.client.get(reverse_lazy('tasks-index')).context['tasks']

        self.assertEqual(self.count, tasks.count())

        self.client.force_login(self.user1)

        self.client.post(reverse_lazy('task-delete', kwargs={'pk': 1}))

        tasks = self.client.get(reverse_lazy('tasks-index')).context['tasks']

        self.assertEqual(self.count - 1, tasks.count())
        self.assertFalse(tasks.filter(task_name=self.task1.task_name))
