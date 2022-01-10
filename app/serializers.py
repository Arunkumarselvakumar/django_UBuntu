from rest_framework import serializers
from app.models import (
    gondola,
    locationSetup,
    cameraandGPU,
    groundplot,
    cartManager,
    turnstile,
    storeDimension,
    camera
) 

class mgondolaserializers(serializers.ModelSerializer):
    class Meta:
        model = gondola
        fields = "__all__"#("locationId","gondolaID","gondolaDimension","shelfCount")

class fgondolaserializers(serializers.ModelSerializer):
    class Meta:
        model = gondola
        fields = "__all__"
class locationSetupserializers(serializers.ModelSerializer):
    class Meta:
        model = locationSetup
        fields = "__all__"
class cameraandGPUserializers(serializers.ModelSerializer):
    class Meta:
        model = cameraandGPU
        fields = "__all__"
class groundplotserializers(serializers.ModelSerializer):
    class Meta:
        model = groundplot
        fields = "__all__"
class cartManagerserializers(serializers.ModelSerializer):
    class Meta:
        model = cartManager
        fields = "__all__"
class storeDimensionserializers(serializers.ModelSerializer):
    class Meta:
        model = storeDimension
        fields = "__all__"
class turnstileserializers(serializers.ModelSerializer):
    class Meta:
        model = turnstile
        fields = "__all__"
class cameraserializers(serializers.ModelSerializer):
    class Meta:
        model = camera
        fields = "__all__"
"""
class storeFloorPlanserializers(serializers.ModelSerializer):
    class Meta:
        model = storeFloorPlan
        fields = "__all__"

class cameraServiceserializers(serializers.ModelSerializer):
    class Meta:
        model = cameraService
        fields = "__all__"


class cameraInfoserializers(serializers.ModelSerializer):
    class Meta:
        model = cameraInfo
        fields = "__all__"


class groundplotserializers(serializers.ModelSerializer):
    class Meta:
        model = groundplot
        fields = "__all__"


class cartManagerserializers(serializers.ModelSerializer):
    class Meta:
        model = cartManager
        fields = "__all__"
"""