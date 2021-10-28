import requests
from django.test import TestCase
from rest_framework.test import APIClient
from rest_framework import status
from django.urls import reverse
from app1.models import Bucketlist
'''
class ViewTestCase(TestCase):
    """Test suite for the api views."""
    def setUp(self):
        """Define the test client and other test variables."""
        self.client = APIClient()  #requests
        """Preparing  Mock Data"""
        self.bucketlist_data = {'name': 'Make a Laptop'}
        self.response = self.client.post(reverse('create'),self.bucketlist_data,format="json")
    def test_api_can_create_a_bucketlist(self):
        """Test the api has bucket creation capability."""
        print('self.response.status_code:',self.response.status_code)
        self.assertEqual(self.response.status_code, status.HTTP_201_CREATED)
    def test_api_can_get_a_bucketlist(self):
        """Test the api can get a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        print('\nDb bucketlist:',bucketlist)
        response = self.client.get(reverse('details',kwargs={'pk': bucketlist.id}), format="json")
        print('\nApi bucketlist:',response)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
        self.assertContains(response, bucketlist)

    def test_api_can_update_bucketlist(self):
        """Test the api can update a given bucketlist."""
        bucketlist = Bucketlist.objects.get()
        print('Before modification:', bucketlist.name)
        change_bucketlist = {'name': 'Making a movie'}
        self.assertEqual(Bucketlist.objects.get().name, 'Make a Laptop')
        res = self.client.put(reverse('details', kwargs={'pk': bucketlist.id}),change_bucketlist, format='json')
        print('After modification:',res)
        self.assertEqual(res.status_code, status.HTTP_200_OK)
        self.assertEqual(Bucketlist.objects.get().name, 'Making a movie')

    def test_api_can_delete_bucketlist(self):
        """Test the api can delete a bucketlist."""
        bucketlist = Bucketlist.objects.get()
        response = self.client.delete(
            reverse('details', kwargs={'pk': bucketlist.id}),
            format='json',
            follow=True)

        self.assertEquals(response.status_code, status.HTTP_204_NO_CONTENT)
'''
class PublicApiTestCase(TestCase):
    def test1(self):
        URL1 = "https://jsonplaceholder.typicode.com/users"
        apiResponse = requests.get(url=URL1)
        print('apiResponse status code=',apiResponse.status_code)
        jsonResponse = apiResponse.json()
        print('Response=',jsonResponse)
        self.assertEqual(apiResponse.status_code,status.HTTP_200_OK)
