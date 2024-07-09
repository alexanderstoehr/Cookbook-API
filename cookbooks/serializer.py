from django.db.migrations import serializer
from rest_framework import serializers

from cookbooks.models import Cookbook
from recipes.serializer import RecipeSerializer


class CookbookCreateSerializer(serializers.ModelSerializer):

    class Meta:
        model = Cookbook
        fields = ["id","title","description", "author"]
        read_only_fields = ["author"]

class CookbookSerializer(serializers.ModelSerializer):
    recipes = RecipeSerializer(many=True, read_only=True)
    amount_of_recipes = serializers.SerializerMethodField()

    def get_amount_of_recipes(self,obj):
        return obj.recipes.count()

    class Meta:
        model = Cookbook
        fields = ['id', 'title', 'description', 'created_at', 'updated_at', 'author', 'recipes', "amount_of_recipes"]  # Explicit field order
