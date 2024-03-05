from django.db import models


# an advertiser can have many item
class Advertiser (models.Model):
    id = models.AutoField(primary_key=True)
    AdvertiserName=models.CharField(max_length=100,unique=True)
    

    def __str__(self):
        return self.AdvertiserName

# an item only belongs to one advertiser
class Item(models.Model):
    id = models.AutoField(primary_key=True)
    ItemName=models.CharField(max_length=150)
    date_added= models.DateTimeField(auto_now_add=True)
    content=models.TextField(max_length=255,default="description") # a description about an item 
    ItemAdvertiser=models.ForeignKey(Advertiser,on_delete=models.CASCADE)

    def __str__(self):
        return self.ItemName
