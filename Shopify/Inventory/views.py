from django.shortcuts import render

from rest_framework import status
from rest_framework.response import Response
from rest_framework.parsers import JSONParser
from rest_framework.decorators import api_view

from .modules.Inventory_AddItem import Inventory_AddItem
from .modules.Inventory_UpdateItem import getItem,editItem
from .modules.delete_retriveItem import delete_Item,retrive_Item

from .models import InventoryDB
from .serializer import InventorySerializer

# Create your views here.

#add item
@api_view(["POST"])
def addItem(request):
    try:
        data = JSONParser().parse(request)
        # Calling modules.Inventory_AddItem function for adding new item.
        return_value, status_code=Inventory_AddItem(data)
        return Response(status=status_code,data=return_value)

    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in saving record",
                    'status':False}

        return Response(status=status_code,data=return_value)

#list items
@api_view(["GET"])
def listItems(request):
    try:
        # Get all the data for list items API.
        item_data = InventoryDB.objects.all()
        # As multiple records are obtained thus setting many=True
        serializer = InventorySerializer(item_data, many=True)
        status_code=status.HTTP_200_OK

        return Response(status=status_code,data=serializer.data)
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in retriving record",
                    'status':False}

        return Response(status=status_code,data=return_value)

#list activeItems
@api_view(["GET"])
def activeItems(request):
    try:
        # Get all active (Non delete) items for list API.
        item_data = InventoryDB.objects.filter(DeleteStatus=0)
        # As multiple records are obtained thus setting many=True
        serializer = InventorySerializer(item_data, many=True)
        status_code=status.HTTP_200_OK

        return Response(status=status_code,data=serializer.data)
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in retriving record",
                    'status':False}

        return Response(status=status_code,data=return_value)

#delete item
@api_view(["POST"])
def deleteItem(request):
    try:
        data = JSONParser().parse(request)
        # Calling modules.delete_retriveItem function for updating delete status.
        status_code,return_value=delete_Item(data)
        return Response(status=status_code,data=return_value)

    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in Deleting item",
                    'status':False}

        return Response(status=status_code,data=return_value)    

#retrieve item
@api_view(["GET"])
def retrieveItem(request,id):
    try:
        # Calling modules.delete_retriveItem function for updating delete status.
        status_code,return_value=retrive_Item(id)
        return Response(status=status_code,data=return_value)

    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in retriving item",
                    'status':False}

        return Response(status=status_code,data=return_value)   

#update items
@api_view(["GET","PUT"])
def updateItem(request,id):
    if(request.method=="GET"):
        try:
            # Calling modules.getItem function to get item data with ItemId equals to id.
            status_code,return_value=getItem(id)
            return Response(status=status_code,data=return_value)

        except:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in retriving record",
                        'status':False}

            return Response(status=status_code,data=return_value)

    elif(request.method=="PUT"):
        try:
            data = JSONParser().parse(request)
            # Calling modules.editItem function to update item data with ItemId equals to id.
            status_code,return_value=editItem(data,id)
            return Response(status=status_code,data=return_value)

        except:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in updating record",
                        'status':False}

            return Response(status=status_code,data=return_value)