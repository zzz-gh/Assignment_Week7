from django.urls import path
from . import views

urlpatterns = [
    path('list',views.index,name = "Productlist"),
    path('detail/<int:product_id>',views.detail,name = "Details"),
    path('create',views.create),
    path('thankyou',views.thankyou)
]