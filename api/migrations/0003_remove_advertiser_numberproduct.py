# Generated by Django 5.0.3 on 2024-03-05 14:34

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0002_advertiser_numberproduct_item_content_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='advertiser',
            name='NumberProduct',
        ),
    ]
