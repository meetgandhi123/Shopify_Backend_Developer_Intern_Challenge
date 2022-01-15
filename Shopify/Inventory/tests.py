import json

from django.urls import reverse
from django.test import TestCase
from rest_framework import status
from rest_framework.test import APITestCase, RequestsClient

from .serializer import AddItemSerializer, InventorySerializer

from.models import InventoryDB

# testcases for add item API.
class TestAddItems(APITestCase):
    def test_valid_addItems(self):
        """
        Ensure we can add new valid item in Inventory.
        """
        url = reverse('inventory_addItem')
        data = {
                "ItemName":"Book",
                "ItemLocation":"A10"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_invalidItemName_addItems(self):
        """
        Ensure that no item without ItemName is added.
        """
        url = reverse('inventory_addItem')
        data = {
                "ItemName":"",
                "ItemLocation":"A10"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    
    def test_invalidItemLocation_addItems(self):
        """
        Ensure that no item without ItemLocation is added.
        """
        url = reverse('inventory_addItem')
        data = {
                "ItemName":"",
                "ItemLocation":"A10"
                }
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
    

# Test cases for listItems API.
class TestListItems(APITestCase):

    def setUp(self):
        InventoryDB.objects.create(
            ItemId = 1,
            ItemName = "Mobile",
            ItemLocation = "F12")

        InventoryDB.objects.create(
            ItemId = 2,
            ItemName = "Mobile",
            ItemLocation = "F12")

        InventoryDB.objects.create(
            ItemId = 3,
            ItemName = "Ipad",
            ItemLocation = "A2",
            DeleteComment="Sold",
            DeleteStatus=1)

    def test_listItems(self):
        """
        Ensure we can retrive all item in Inventory.
        """
        url = reverse('inventory_list')
        response = self.client.get(url, format='json')
        self.assertGreater(len(response.data),1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_active_listItems(self):
        """
        Ensure we can retrive only Active item in Inventory.
        """
        url = reverse('inventory_listActive')
        response = self.client.get(url, format='json')
        self.assertGreater(len(response.data),1)
        self.assertEqual(response.status_code, status.HTTP_200_OK)

# testcases for delete item API.
class TestDeleteItems(APITestCase):

    def setUp(self):
        InventoryDB.objects.create(
            ItemId = 1,
            ItemName = "Mobile",
            ItemLocation = "F12")

    def test_valid_DeleteItems(self):
        """
        Ensure we can delete item in Inventory.
        """
        url = reverse('inventory_delete')
        data = {
                "ItemId":1,
                "DeleteComment":"Sold",
                "DeleteStatus":1
                }

        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        # Test Invalid Delete Items, the case when DeleteStatus is already 1.    
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

# testcases for get item API.
class TestGetItems(APITestCase):

    def setUp(self):
        InventoryDB.objects.create(
            ItemId = 1,
            ItemName = "Mobile",
            ItemLocation = "F12")  

        InventoryDB.objects.create(
            ItemId = 2,
            ItemName = "Ipad",
            ItemLocation = "A2",
            DeleteComment="Sold",
            DeleteStatus=1)                  

    def test_get_Items(self):
        """
        Ensure we can get item in Inventory.
        """
        response = self.client.get('/item/update/1')
        self.assertEqual(response.data['ItemId'], 1)
        self.assertEqual(response.data['ItemName'], "Mobile")
        self.assertEqual(response.data['ItemLocation'], "F12")
        self.assertEqual(response.data['DeleteStatus'], 0)

    def test_get_Deactivated_Items(self):
        """
        Ensure we can not get deactivated item in Inventory.
        """
        response = self.client.get('/item/update/2')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
            

# testcases for update item API.
class TestUpdateItems(APITestCase):

    def setUp(self):
        InventoryDB.objects.create(
            ItemId = 1,
            ItemName = "Mobile",
            ItemLocation = "F12") 
        
        InventoryDB.objects.create(
            ItemId = 2,
            ItemName = "Mobile",
            ItemLocation = "F12") 

    def test_update_Items(self):
        """
        Ensure we can update item in Inventory.
        """
        data={
            "ItemName" : "Mobile_Apple",
            "ItemLocation" : "A2" 
        } 
        url = '/item/update/1'

        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)
    
    def test_Deactivate_update_Items(self):
        """
        Ensure we can not update inactive items in Inventory.
        """
        data={
            "ItemId":2,
            "DeleteComment" : "Sold",
            "DeleteStatus" : 1 
        } 
        url = reverse('inventory_delete')
        response = self.client.post(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

        url = '/item/update/2'
        data={
            "ItemName" : "Mobile",
            "ItemLocation" : "A1" 
        } 
        response = self.client.put(url, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
