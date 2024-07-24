# tests/test_task.py

import unittest
from src.task import Task

class TestTask(unittest.TestCase):
    def test_create_task(self):
        task = Task("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)

    def test_mark_complete(self):
        task = Task("Test task")
        task.mark_complete()
        self.assertTrue(task.completed)

if __name__ == '__main__':
    unittest.main()
