from rest_framework import serializers 
from api1.models import storeFloorPlan,cartManager,storeFixtures,cameraService,cameraInfo,groundplot#Locationsetup,store_Dimension,Shelves,Master_Host,Camera_gpu,Groundplot,Cart_Manager,Backend_APIs

class storeFloorPlanserializers(serializers.ModelSerializer):
    
    class Meta:
        model = storeFloorPlan
        fields =('__all__')
class storeFixturesserializers(serializers.ModelSerializer): 
    class Meta:
        model = storeFixtures
        fields =('__all__')
class cameraServiceserializers(serializers.ModelSerializer):
    
    class Meta:
        model = cameraService
        fields =('__all__')
class cameraInfoserializers(serializers.ModelSerializer):
    
    class Meta:
        model = cameraInfo
        fields =('__all__')

class groundplotserializers(serializers.ModelSerializer):
    
    class Meta:
        model = groundplot
        fields =('__all__')

class cartManagerserializers(serializers.ModelSerializer):
    
    class Meta:
        model = cartManager
        fields =('__all__')

