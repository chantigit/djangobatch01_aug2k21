import requests
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
import json
import	requests

endpoint="http://127.0.0.1:8000/student/"

class StudentTestCase(TestCase):
    def test_create_student(self):
        student = {
                "rollNumber": "CHNTBT1003",
                "course":"Java",
                "age": 26
            }
        jsonData = json.dumps(student)
        responseData = requests.post(url=endpoint, json=student)
        print('responseData.status_code=',responseData.status_code)
        self.assertEqual(responseData.status_code,status.HTTP_201_CREATED)

