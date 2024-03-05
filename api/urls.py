from django.urls import path
from .views import ItemList, ItemDetail, AdvertiserDetail, AdvertiserList

urlpatterns = [
    path('advertiser/', AdvertiserList.as_view()),
    path('advertiser/<int:pk>/', AdvertiserDetail.as_view()),
    path('item/', ItemList.as_view()),
    path('item/<int:pk>/', ItemDetail.as_view()),
]