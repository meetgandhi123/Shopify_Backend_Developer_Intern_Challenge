from rest_framework import status

from ..serializer import (AddItemSerializer,InventorySerializer)
from ..models import InventoryDB

def getItem(id):
    """retrive a single item corresponding to the ItemId from InventroyDB.

    Args:
        id ([int]): [ItemId of the inventory item]

    Returns:
        [
            status_code: status of the request.
            return_value: returns the record with ItemId equals to id.
        ]
    """
    try:
        item_data = InventoryDB.objects.get(ItemId=id)
        # Condition for chekcing if the item is active.
        if(item_data.DeleteStatus==1):
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Item is deactivated, activate item to update.",
                        'status':False}
            return status_code,return_value

        # the object will be of single record thus setting many=False.
        serializer = InventorySerializer(item_data, many=False)
        status_code=status.HTTP_200_OK

        return status_code,serializer.data
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in retriving record",
                    'status':False}

        return status_code,return_value

def delete_Item(data,update_deleteStatus):
    """ Updating the delete status of the item.
        This function is used for both activating and deactivating the 
        status of an item.

    Args:
        data ([json]): [ItemId, DeleteComment]
        update_deleteStatus ([int]): [for deleting the item 
        update_deleteStatus equals to 1 and for retriving the deleted item 
        update_deleteStatus equals to 0]

    Returns:
        [
            status_code: status of the request.
            return_value: returns the updated record.
        ]
    """
    try:
        # getting the data corrosponsing to the ItemId.
        Item_data = InventoryDB.objects.get(ItemId=data['ItemId'])
        # Updating the data to be updated.
        data['ItemName']=Item_data.ItemName
        data['ItemLocation']=Item_data.ItemLocation
        data['DeleteStatus']=update_deleteStatus
        if(update_deleteStatus==0):
            data['DeleteComment']=Item_data.DeleteComment
            
        serializer = InventorySerializer(Item_data, data=data)
        if(serializer.is_valid()):
            serializer.save()
            status_code=status.HTTP_200_OK
            return_value=serializer.data
            return status_code,return_value
        else:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in updating item record",
                        'status':False}

            return status_code,return_value
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in updating item record",
                    'status':False}

        return status_code,return_value

def editItem(data,id):
    """ Updating the item record of the item with ItemID equals to id.

    Args:
        data ([json]): ['ItemName', 'ItemLocation']
        id ([int]): [ItemId of the inventory item to be updated.]
 
    Returns:
        [
            status_code: status of the request.
            return_value: returns the updated record.
        ]
    """
    try:
        item_data = InventoryDB.objects.get(ItemId=id)
        # Condition for chekcing if the item is active.
        if(item_data.DeleteStatus==1):
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Item is deactivated, activate item to update.",
                        'status':False}
            return status_code,return_value
                                    
        serializer = AddItemSerializer(item_data, data=data)
        if(serializer.is_valid()):
            serializer.save()
            status_code=status.HTTP_200_OK
            return_value=serializer.data
            return status_code,return_value
        else:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in updating item record",
                        'status':False}

            return status_code,return_value
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in updating item record",
                    'status':False}

        return status_code,return_value