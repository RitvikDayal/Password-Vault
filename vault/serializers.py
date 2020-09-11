from rest_framework import serializers
from .models import Credential

class CredSerializer(serializers.ModelSerializer):
    class Meta:
        model = Credential
        fields = ['website', 'website_url', 'username', 'password', 'note', 'last_update']