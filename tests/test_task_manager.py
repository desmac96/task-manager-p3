# tests/test_task_manager.py

"""
Unit tests for the TaskManager class.
"""

import unittest
from src.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    """
    Test case for the TaskManager class.
    """

    def setUp(self):
        """
        Set up a TaskManager instance for testing.
        """
        self.manager = TaskManager()

    def test_add_task(self):
        """
        Test adding a task to the TaskManager.
        """
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Test task")

    def test_remove_task(self):
        """
        Test removing a task from the TaskManager.
        """
        self.manager.add_task("Test task")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

    def test_list_tasks(self):
        """
        Test listing all tasks in the TaskManager.
        """
        self.manager.add_task("Test task")
        tasks = self.manager.list_tasks()
        self.assertEqual(len(tasks), 1)
        self.assertEqual(tasks[0].description, "Test task")

    def test_mark_task_complete(self):
        """
        Test marking a task as complete in the TaskManager.
        """
        self.manager.add_task("Test task")
        self.manager.mark_task_complete(0)
        self.assertTrue(self.manager.tasks[0].completed)

if __name__ == '__main__':
    unittest.main()
