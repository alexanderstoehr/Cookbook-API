from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView, ListCreateAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from cookbooks.models import Cookbook
from cookbooks.serializer import CookbookSerializer, CookbookCreateSerializer


# Create your views here.

class ListMyOwnCookbooksView(GenericAPIView):
    serializer_class = CookbookSerializer

    def get_queryset(self):
        return Cookbook.objects.filter(author=self.request.user)

    def get(self, request, *args, **kwargs):
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)



# class ListCreateCookbookView(GenericAPIView):
#     queryset = Cookbook.objects.all()
#
#     # serializer_class = CookbookSerializer
#
#     def get_serializer_class(self):
#         if self.request.method == "POST":
#             return CookbookCreateSerializer
#         return CookbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         queryset = self.get_queryset()
#         serializer = self.get_serializer(queryset, many=True)
#         return Response(serializer.data)
#
#     def post(self, request, *args, **kwargs):
#         serializer = self.get_serializer(data=request.data)
#         serializer.is_valid(raise_exception=True)
#         serializer.save(author=request.user)
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#

class ListCreateCookbookView(ListCreateAPIView):
    """
    get:
    GET ALL ITEMS

    # This endpoint will return all the items
    > markdown **xxx**
    """
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
    # permission_classes = [IsAdminOrReadOnly]


# class RetrieveUpdateDeleteCookbookView(GenericAPIView):
#     queryset = Cookbook.objects.all()
#     serializer_class = CookbookSerializer
#
#     def get(self, request, *args, **kwargs):
#         # find id > kwargs
#         # use id to find instance
#         # instance_id = self.kwargs['pk']
#         # instance = Recipe.objects.get(pk=instance_id)
#         instance = self.get_object()
#         serializer = self.get_serializer(instance)
#         return Response(serializer.data)
#
#     def patch(self, request, *args, **kwarga):
#         instance = self.get_object()
#         serializer = self.get_serializer(instance, data=request.data, partial=True)
#         serializer.is_valid(raise_exception=True)
#         serializer.save()
#         return Response(serializer.data)
#
#     def delete(self, request, *args, **kwargs):
#         instance = self.get_object()
#         instance.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)

class RetrieveUpdateDeleteCookbookView(RetrieveUpdateDestroyAPIView):
    queryset = Cookbook.objects.all()
    serializer_class = CookbookSerializer
