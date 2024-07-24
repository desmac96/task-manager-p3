# tests/test_task_manager.py

import unittest
from src.task_manager import TaskManager

class TestTaskManager(unittest.TestCase):
    def setUp(self):
        self.manager = TaskManager()

    def test_add_task(self):
        self.manager.add_task("Test task")
        self.assertEqual(len(self.manager.tasks), 1)
        self.assertEqual(self.manager.tasks[0].description, "Test task")

    def test_remove_task(self):
        self.manager.add_task("Test task")
        self.manager.remove_task(0)
        self.assertEqual(len(self.manager.tasks), 0)

if __name__ == '__main__':
    unittest.main()