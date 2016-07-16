from rest_framework import serializers
from RegressionOneApp.models import Thingamabob

class ThingamabobSerializer(serializers.ModelSerializer):
    class Meta:
        model = Thingamabob
        fields = ('description', 'done', 'updated')