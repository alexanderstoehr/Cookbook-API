
from rest_framework import serializers

from cookbooks.models import Cookbook
from favorites.models import Favorite


class FavoriteSerializer(serializers.ModelSerializer):
    #instance_id = serializers.IntegerField()

    class Meta:
        model = Favorite
        fields = "__all__"
