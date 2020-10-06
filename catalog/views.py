from django.shortcuts import render

from .serializers import MobileSerializer
from rest_framework.views import APIView
from rest_framework.response import Response
from rest_framework import status
from django.shortcuts import get_object_or_404
from .models import Mobile
from rest_framework import permissions
from django.http import Http404
from .permissions import IsAdminOrReadOnly

class MobileList(APIView):
    serializer_class = MobileSerializer
    permission_classes = (IsAdminOrReadOnly,)

   

    def get(self, request):
        mobile1 = Mobile.objects.all().order_by('price')
        serializer = MobileSerializer(mobile1, many=True)
        return Response(serializer.data)

    def post(self, request, format=None):
         serializer = MobileSerializer(data=request.data)
         if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

     