from rest_framework import generics
from .models import Advertiser, Item
from .serializers import AdvertiserSerializer, ItemSerializer


class ItemList(generics.ListCreateAPIView):
    serializer_class = ItemSerializer

    def get_queryset(self):
        queryset = Item.objects.all()
        advertiser = self.request.query_params.get('advertiser')
        if advertiser is not None:
            queryset = queryset.filter(ItemAdvertiser=advertiser)
        return queryset

# to update or delete item 
class ItemDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Item.objects.all()
    serializer_class = ItemSerializer


class AdvertiserList(generics.ListCreateAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer

# to update or delete advertiser
class AdvertiserDetail(generics.RetrieveUpdateDestroyAPIView):
    queryset = Advertiser.objects.all()
    serializer_class = AdvertiserSerializer