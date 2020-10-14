from django.contrib.auth.models import User
from rest_framework import serializers
from .models import Asset, Attachments


class UserSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = User
        fields = ['url','first_name','last_name', 'username', 'email']


class AssetSerializer(serializers.HyperlinkedModelSerializer):
    class Meta:
        model = Asset
        fields = ['url', 'name', 'user', 'purchase_date', 'description']
