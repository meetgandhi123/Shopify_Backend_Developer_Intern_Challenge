from rest_framework import status

from ..serializer import (InventorySerializer)
from ..models import InventoryDB


def retrive_Item(data):
    """ Updating the delete status of the item.        

    Args:
        data ([json]): [ItemId, DeleteComment]

    Returns:
        [
            status_code: status of the request.
            return_value: returns the updated record.
        ]
    """
    try:
        # getting the data corrosponsing to the ItemId.
        Item_data = InventoryDB.objects.get(ItemId=data)

        # validation for record already active.
        if(Item_data.DeleteStatus==0):
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Item record already active",
                        'status':False}

            return status_code,return_value
        
        data={}
        # Updating the data to be updated.
        data['ItemName']=Item_data.ItemName
        data['ItemLocation']=Item_data.ItemLocation
        data['DeleteComment']=Item_data.DeleteComment
        data['DeleteStatus']=0 # Activate
 
        # updating the item delete status.
        serializer = InventorySerializer(Item_data, data=data)
        if(serializer.is_valid()):
            serializer.save()
            status_code=status.HTTP_200_OK
            return_value=serializer.data
            return status_code,return_value
        else:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in activating item record",
                        'status':False}

            return status_code,return_value
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in activating item record",
                    'status':False}

        return status_code,return_value

def delete_Item(data):
    """ Updating the delete status of the item.

    Args:
        data ([json]): [ItemId, DeleteComment]

    Returns:
        [
            status_code: status of the request.
            return_value: returns the updated record.
        ]
    """
    try:
        # getting the data corrosponsing to the ItemId.
        Item_data = InventoryDB.objects.get(ItemId=data['ItemId'])

        # adding validation for already deleted record.
        if(Item_data.DeleteStatus==1):
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Item record already deleted",
                        'status':False}

            return status_code,return_value

        # Updating the data to be updated.
        data['ItemName']=Item_data.ItemName
        data['ItemLocation']=Item_data.ItemLocation
        data['DeleteStatus']=1

        serializer = InventorySerializer(Item_data, data=data)
        if(serializer.is_valid()):
            serializer.save()
            status_code=status.HTTP_200_OK
            return_value=serializer.data
            return status_code,return_value
        else:
            status_code=status.HTTP_400_BAD_REQUEST
            return_value={'message':"Error in deleting item record",
                        'status':False}

            return status_code,return_value
    except:
        status_code=status.HTTP_400_BAD_REQUEST
        return_value={'message':"Error in deleting item record",
                    'status':False}

        return status_code,return_value