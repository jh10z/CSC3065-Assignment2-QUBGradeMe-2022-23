import unittest
import logging

from main import app
app.testing = True

# Test
class Test_TotalMarks(unittest.TestCase):
    # Response Code Tests
    def test_addupdateservice(self):
        with app.test_client() as client:
            response = client.get("/admin/save?test=http://testurl")
        
        self.assertEqual(response.status, '200 OK')
        self.assertEqual(response.json["test"], 'http://testurl')
    
    def test_deleteservice(self):
        with app.test_client() as client:
            response = client.get("/admin/delete?selected=test")

        self.assertEqual(response.status, '200 OK')
        self.assertFalse("test" in response.json)
    
    def test_mainservices(self):
        with app.test_client() as client:
            response = client.get("/admin/save")
        
        services = {
            "MaxMin",
            "SortModules",
            "TotalMarks",
            "ClassifyGrade",
            "AverageMark",
            "ClassifyModules"
        }
        self.assertEqual(response.status, '200 OK')
        for service in services:
            self.assertTrue(service in response.json)
            
if __name__ == '__main__':
    unittest.main()