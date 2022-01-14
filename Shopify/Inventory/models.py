from django.db import models

# Create your models here.
class InventoryDB(models.Model):
    ItemId = models.AutoField(primary_key=True)
    ItemName = models.TextField(max_length=20,null=False,blank=False)
    ItemLocation = models.TextField(max_length=20,null=False,blank=False)
    DeleteComment = models.TextField(max_length=200)
    DeleteStatus = models.IntegerField(default=0)
    
    class Meta:
        db_table = "InventoryDB"
