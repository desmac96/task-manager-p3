# tests/test_task.py

"""
Unit tests for the Task class.
"""

import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    """
    Test case for the Task class.
    """

    def test_create_task(self):
        """
        Test creating a task with a description.
        """
        task = Task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)

    def test_mark_complete(self):
        """
        Test marking a task as complete.
        """
        task = Task("Test task")
        task.mark_complete()
        self.assertTrue(task.completed)

if __name__ == '__main__':
    unittest.main()
