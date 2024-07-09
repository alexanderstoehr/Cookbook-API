from django.db.migrations import serializer
from rest_framework import serializers
from rest_framework.utils import representation

from ingredients.models import Ingredient
from ingredients.serializer import IngredientSerializer
from recipes.models import Recipe


class RecipeSerializer(serializers.ModelSerializer):
    # ingredients = IngredientSerializer(many=True)

    def to_representation(self, instance):
        representation = super().to_representation(instance)
        representation['ingredients'] = IngredientSerializer(instance.ingredients, many=True).data
        return representation

    class Meta:
        model = Recipe
        fields = '__all__'
        # depth = 1
        # extra_kwargs = {
        #     "author": {"read_only": True},
        #     "author": {"write_only": True},
        # }
