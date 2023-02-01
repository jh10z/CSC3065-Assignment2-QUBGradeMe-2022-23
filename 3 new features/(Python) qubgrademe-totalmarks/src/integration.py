import unittest
import logging

from main import app
app.testing = True

# Test
class Test_TotalMarks(unittest.TestCase):
    # Response Code Tests
    def test_addnormal(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "10",
                "mark_2": "10",
                "mark_3": "10",
                "mark_4": "10",
                "mark_5": "10",
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json["total_marks"], 50.0)

    def test_addword(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "word"
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.text, 'Module 1 value is not a number. \n')
    
    def test_addoutofboundsupper(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "101"
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.text, 'Module 1 input is not within 0 and 100. \n')
    
    def test_addoutofboundslower(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "-1"
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.text, 'Module 1 input is not within 0 and 100. \n')

    def test_addnothing(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "",
                "mark_2": "",
                "mark_3": "",
                "mark_4": "",
                "mark_5": "",
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '400 BAD REQUEST')
        self.assertEqual(response.text, "Error: To use functionality, please enter at least one mark.")

    def test_addhalfsupply(self):
        with app.test_client() as client:
            sent = {
                "mark_1": "10",
                "mark_2": "10",
                "mark_3": "10",
                "mark_4": "",
                "mark_5": "",
            }
            response = client.post('/', json = sent)
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json["total_marks"], 30.0)

if __name__ == '__main__':
    unittest.main()