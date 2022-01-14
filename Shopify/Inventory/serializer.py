from rest_framework import serializers
from .models import InventoryDB

class InventorySerializer(serializers.ModelSerializer):
    """
    This serializer used to get and update delete status of item records.
    """ 
    class Meta:
        model = InventoryDB
        fields = ('ItemId','ItemName', 'ItemLocation','DeleteComment','DeleteStatus')

class AddItemSerializer(serializers.ModelSerializer):
    """
    This serializer used to add and edit item data.
    """
    class Meta:
        model = InventoryDB
        fields = ('ItemId','ItemName', 'ItemLocation')
