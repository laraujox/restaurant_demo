from rest_framework.serializers import ModelSerializer

from products.models import Customization, Product


class CustomizationSerializer(ModelSerializer):
    class Meta:
        model = Customization
        exclude = []


class ProductSerializer(ModelSerializer):
    customization = CustomizationSerializer()

    class Meta:
        model = Product
        exclude = []
