from django.shortcuts import render
from rest_framework import status
from rest_framework.generics import GenericAPIView
from rest_framework.permissions import IsAuthenticated
from rest_framework.response import Response

from cookbooks.models import Cookbook
from favorites.models import Favorite
from favorites.serializer import FavoriteSerializer


# Create your views here.
class LikeCookbookView(GenericAPIView):
    queryset = Cookbook.objects.all()
    permission_classes = [IsAuthenticated]
    serializer_class = FavoriteSerializer

    def post(self,request, *args, **kwargs):
        cookbook = self.get_object()
        user = request.user

        favorite, created = Favorite.objects.get_or_create(user=user, cookbook=cookbook)

        if created:
            # If a new Favorite instance was created, return a success response
            return Response({'status': 'cookbook liked'}, status=status.HTTP_201_CREATED)
        else:
            # If the Favorite instance already existed, return an appropriate response
            favorite.delete()
            return Response({'status': 'cookbook unliked'}, status=status.HTTP_200_OK)



#logged_in_user_liked

class LikeRecipeView(GenericAPIView):

    def post(self,request, *args, **kwargs):
        pass