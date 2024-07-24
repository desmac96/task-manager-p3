# tests/test_task.py

import unittest
from src.task import Task

class TestTack(unittest.TestCase):
    def test_create_task(self):
        task = ("Test task")
        self.assertEqual(task.description, "Test task")
        self.assertFalse(task.completed)

if __name__=='__main__';
    unittest.main()
    