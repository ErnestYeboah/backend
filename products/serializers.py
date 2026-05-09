from rest_framework.serializers import ModelSerializer
from .models import *

class ProductSerializer(ModelSerializer):
    class Meta :
        model = Product
        fields = "__all__"

class FavoriteSerializer(ModelSerializer):
    class Meta :
        model = Favorite
        fields = "__all__"

class CartSerializer(ModelSerializer):
    class Meta :
        model = Cart
        fields = "__all__"