from django.core.exceptions import ValidationError
from django.test import TestCase
from tasks.models import Task, Category

class TaskModelTest(TestCase):
    def setUp(self):
        self.category = Category.objects.create(name="Test Category")
        self.task = Task.objects.create(
            title="Test Task",
            due_date="2024-12-31",
            category=self.category,
            completed=False
        )

    def test_task_creation(self):
        self.assertEqual(self.task.title, "Test Task")
        self.assertEqual(self.task.due_date, "2024-12-31")
        self.assertEqual(self.task.completed, False)
        self.assertEqual(self.task.category, self.category)
        

    def test_task_str(self):
        self.assertEqual(str(self.task), "Test Task")

    def test_task_due_date(self):
        self.assertEqual(str(self.task.due_date), "2024-12-31")

    def test_task_completed_default(self):
        self.assertFalse(self.task.completed, False)

    def test_task_category_relationship(self):
        self.assertEqual(self.task.category, self.category)
        self.assertEqual(self.category.task_set.count(), 1)
        self.assertEqual(self.category.task_set.first(), self.task)

# generate a unit test that checks for an error if the title is longer than 100 characters
    def test_task_title_length(self):
        long_title = "T" * 101  # 101 characters
        with self.assertRaises(ValidationError):
            task = Task(
                title=long_title,
                due_date="2024-12-31",
                category=self.category,
                completed=False
            )
            task.save()