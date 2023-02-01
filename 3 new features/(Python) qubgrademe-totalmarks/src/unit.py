import unittest
import main

# Test
class Unit(unittest.TestCase):
    def test_addnormal(self):
        json = {
            "mark_1": "10",
            "mark_2": "10",
            "mark_3": "10",
            "mark_4": "10",
            "mark_5": "10",
        }
        self.assertEqual(main.getTotalMarks(json), {"total": 50, "response": "", "status": 200})
    
    def test_addonevalue(self):
        json = {
            "mark_1": "10"
        }
        self.assertEqual(main.getTotalMarks(json), {"total": 10, "response": "", "status": 200})

    def test_addtwovalues(self):
        json = {
            "mark_1": "10",
            "mark_2": "10"
        }
        self.assertEqual(main.getTotalMarks(json), {"total": 20, "response": "", "status": 200})


    def test_addthreevalues(self):
        json = {
            "mark_1": "10",
            "mark_2": "10",
            "mark_3": "10"
        }
        self.assertEqual(main.getTotalMarks(json), {"total": 30, "response": "", "status": 200})

    def test_addfourvalues(self):
        json = {
            "mark_1": "10",
            "mark_2": "10",
            "mark_3": "10",
            "mark_4": "10"
        }
        self.assertEqual(main.getTotalMarks(json), {"total": 40, "response": "", "status": 200})

if __name__ == '__main__':
    unittest.main()