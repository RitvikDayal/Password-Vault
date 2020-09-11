from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework.response import Response
from .models import Credential
from .serializers import CredSerializer

@api_view(['GET'])
def patterns(request):
    api_urls = {
        'Websites': '/websites-list/',
        'Detail View': '/cred-detail/<str:pk>/',
        'create': '/cred-create/',
        'Update': '/cred-update/<str:pk>/',
        'Delete': '/cred-delete/<str:pk>/',
    }
    return Response(api_urls)

@api_view(['GET'])
def credList(request):
    creds = Credential.objects.all()
    serializer = CredSerializer(creds, many=True)
    return Response(serializer.data)

@api_view(['GET'])
def credDetail(request, pk):
    creds = Credential.objects.get(id=pk)
    serializer = CredSerializer(creds, many=False)
    return Response(serializer.data)