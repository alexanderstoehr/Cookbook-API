from rest_framework import status
from rest_framework.generics import GenericAPIView, RetrieveUpdateDestroyAPIView
from rest_framework.response import Response

from recipes.models import Recipe
from recipes.permissions import IsAdminOrReadOnly
from recipes.serializer import RecipeSerializer


# Create your views here.
class ListCreateRecipesView(GenericAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer

    def get(self, request, *args, **kwargs):
        # recipes = Recipe.objects.all()
        # formatted_recipes = RecipeSerializer(recipes, many=True)
        # return Response(formatted_recipes.data)
        queryset = self.get_queryset()
        serializer = self.get_serializer(queryset, many=True)
        return Response(serializer.data)

    def post(self, request, *args, **kwargs):
        serializer = self.get_serializer(data=request.data)
        serializer.is_valid(raise_exception=True)
        serializer.save()
        return Response(serializer.data, status=status.HTTP_201_CREATED)


class RetrieveUpdateDeleteRecipeView(RetrieveUpdateDestroyAPIView):
    queryset = Recipe.objects.all()
    serializer_class = RecipeSerializer
    permission_classes = [IsAdminOrReadOnly]

    #
    # def get(self, request, *args, **kwargs):
    #     # find id > kwargs
    #     # use id to find instance
    #     # instance_id = self.kwargs['pk']
    #     # instance = Recipe.objects.get(pk=instance_id)
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance)
    #     return Response(serializer.data)
    #
    # def patch(self, request, *args, **kwarga):
    #     instance = self.get_object()
    #     serializer = self.get_serializer(instance, data=request.data, partial=True)
    #     serializer.is_valid(raise_exception=True)
    #     serializer.save()
    #     return Response(serializer.data)
    #
    # def delete(self, request, *args, **kwargs):
    #     instance = self.get_object()
    #     instance.delete()
    #     return Response(status=status.HTTP_204_NO_CONTENT)
