from . import views
from django.urls import path, include

urlpatterns = [
    path('item/add', views.addItem,name="inventory_addItem"),
    path('item/list', views.listItems),
    path('item/listActive', views.activeItems),
    path('item/update/<id>', views.updateItem),
    path('item/delete', views.deleteItem),
    path('item/retrieve/<id>', views.retrieveItem),
]