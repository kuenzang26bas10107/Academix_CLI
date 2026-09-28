"""
This module contains automated unit tests to verify the core logic 
of the Academix CLI application, specifically the validators and the priority engine.
"""
import unittest
from datetime import datetime, timedelta
import validator
import priority_engine
import task_manager

class TestValidators(unittest.TestCase):
    
    def test_is_valid_date(self):
        # Test correct format
        self.assertTrue(validator.is_valid_date("2024-12-31")[0])
        # Test incorrect format
        self.assertFalse(validator.is_valid_date("12-31-2024")[0])
        # Test invalid date (Feb 30th)
        self.assertFalse(validator.is_valid_date("2024-02-30")[0])

    def test_is_valid_percentage(self):
        # Test valid percentages
        self.assertTrue(validator.is_valid_percentage("50")[0])
        self.assertTrue(validator.is_valid_percentage("100")[0])
        # Test out of bounds
        self.assertFalse(validator.is_valid_percentage("105")[0])
        self.assertFalse(validator.is_valid_percentage("0")[0])
        # Test non-numeric string
        self.assertFalse(validator.is_valid_percentage("abc")[0])

    def test_is_valid_hours(self):
        # Test positive hours
        self.assertTrue(validator.is_valid_hours("5.5")[0])
        self.assertTrue(validator.is_valid_hours("10")[0])
        # Test zero or negative hours
        self.assertFalse(validator.is_valid_hours("0")[0])
        self.assertFalse(validator.is_valid_hours("-2")[0])

    def test_is_non_empty_string(self):
        self.assertTrue(validator.is_non_empty_string("CS101")[0])
        self.assertFalse(validator.is_non_empty_string("   ")[0])
        self.assertFalse(validator.is_non_empty_string("")[0])


class TestPriorityEngine(unittest.TestCase):
    
    def setUp(self):
        """Set up dummy dates for testing priority calculations."""
        self.today = datetime.now()
        # Tomorrow
        self.tomorrow = (self.today + timedelta(days=1)).strftime("%Y-%m-%d")
        # Overdue (Yesterday)
        self.yesterday = (self.today - timedelta(days=1)).strftime("%Y-%m-%d")

    def test_critical_overdue_task(self):
        """Overdue tasks should instantly receive a CRITICAL tag and max score."""
        task = {
            "id": "1", "deadline_date": self.yesterday, 
            "weightage_percent": 10.0, "estimated_hours": 2.0, "status": "PENDING"
        }
        result = priority_engine.calculate_task_priority(task)
        self.assertEqual(result["tag"], "CRITICAL")
        self.assertEqual(result["score"], 9999.0)

    def test_completed_task_priority(self):
        """Completed tasks should receive a score of 0 and a DONE tag."""
        task = {
            "id": "2", "deadline_date": self.tomorrow, 
            "weightage_percent": 50.0, "estimated_hours": 5.0, "status": "COMPLETED"
        }
        result = priority_engine.calculate_task_priority(task)
        self.assertEqual(result["tag"], "DONE")
        self.assertEqual(result["score"], 0)

    def test_active_task_priority(self):
        """Test the standard priority calculation math."""
        task = {
            "id": "3", "deadline_date": self.tomorrow, 
            "weightage_percent": 40.0, "estimated_hours": 10.0, "status": "PENDING"
        }
        # Math: Weightage(40) / (DaysRemaining(1) + 1) * (1 + (Hours(10)/10)) 
        # = (40 / 2) * (1 + 1) = 20 * 2 = 40.0
        result = priority_engine.calculate_task_priority(task)
        self.assertEqual(result["score"], 40.0)
        self.assertEqual(result["tag"], "HIGH")

class TestTaskManager(unittest.TestCase):
    
    def test_generate_id(self):
        tasks = {}
        self.assertEqual(task_manager.generate_id(tasks), "1")
        tasks = {"1": {}, "5": {}}
        self.assertEqual(task_manager.generate_id(tasks), "6")

if __name__ == '__main__':
    unittest.main()
