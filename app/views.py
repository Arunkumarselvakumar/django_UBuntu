from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
from bson import json_util
from app.models import (
    storeFloorPlan,
    cartManager,
    storeFixtures,
    cameraService,
    cameraInfo,
    groundplot,
)  
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from app.serializers import (
    storeFixturesserializers,
    cartManagerserializers,
    storeFloorPlanserializers,
    cameraServiceserializers,
    cameraInfoserializers,
    groundplotserializers,
)  

@csrf_exempt
@api_view(["GET", "DELETE"])
def all_(request):
    tutorial_data = JSONParser().parse(request)
    # mail=tutorial_data['locationId']
    if request.method == "GET":
        try:
            a = {}
            try:
                ground = groundplot.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).values()
                if ground:
                    a.update({"groundplot": ground[0]})
            except:
                pass 
            store = storeFloorPlan.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if store:
                a.update({"storeFloorPlan": store[0]})
            camS = cameraService.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if camS:
                a.update({"cameraService": camS[0]})
            camI = cameraInfo.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if camI:
                a.update({"cameraInfo": camI[0]})
            she = storeFixtures.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if she:
                a.update({"storeFixtures": she[0]})
            cart = cartManager.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if cart:
                a.update({"cartManager": cart[0]})

            c = json.loads(json_util.dumps(a))
            return JsonResponse(c, safe=False)

        except Exception as e:
            return e
    if request.method == "DELETE":
        try:
            ground1 = groundplot.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            store1 = storeFloorPlan.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            camS = cameraService.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            camI = cameraInfo.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            she1 = storeFixtures.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            cart = cartManager.objects.filter(
                locationId=tutorial_data["locationId"]
            ).values()
            if ground1 or store1 or camS or she1 or camI or car:

                ground = groundplot.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                store = storeFloorPlan.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                camS = cameraService.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                camI = cameraInfo.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                she = storeFixtures.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                cart = cartManager.objects.filter(
                    locationId=tutorial_data["locationId"]
                ).delete()
                """
                try:
                    ground1 = groundplot.objects.filter(locationId=tutorial_data['locationId']).values()
                    if ground1:
                        ground = groundplot.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass
                try:
                    store1 = storeFloorPlan.objects.filter(locationId=tutorial_data['locationId']).values()
                    if store1:
                        store = storeFloorPlan.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass        
                try:
                    camS = cameraService.objects.filter(locationId=tutorial_data['locationId']).values()
                    if camS:
                        camS = cameraService.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass
                try:
                    camI = cameraInfo.objects.filter(locationId=tutorial_data['locationId']).values()
                    if camI:
                        camI = cameraInfo.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass
                try:
                    she1 = storeFixtures.objects.filter(locationId=tutorial_data['locationId']).values()
                    if she1:
                        she = storeFixtures.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass
                try:
                    cart = cartManager.objects.filter(locationId=tutorial_data['locationId']).values()
                    if cart:
                        cart = cartManager.objects.filter(locationId=tutorial_data['locationId']).delete()
                except:
                    pass
                """
            response = {tutorial_data["locationId"]: "deleted"}
            c = json.loads(json_util.dumps(response))
            return JsonResponse(c, safe=False)
        except:
            message = {"message": "User Already removed"}
            return JsonResponse(message, safe=False)


@csrf_exempt
@api_view(["PUT"])
def storeFloorPlan_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        c = json.loads(json_util.dumps(tutorial_data))
        a = storeFloorPlan.objects.filter(
            locationId=tutorial_data["locationId"]
        ).values()
        # b = a[0]
        if a:
            location = storeFloorPlan.objects.get(
                locationId=tutorial_data["locationId"]
            )
            tutorial_serializer = storeFloorPlanserializers(
                location, data=tutorial_data
            )
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = storeFloorPlanserializers(data=tutorial_data)
            # c = json.loads(json_util.dumps(tutorial_data))
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
@api_view(["PUT"])
def storeFixtures_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        a = storeFixtures.objects.filter(
            locationId=tutorial_data["locationId"]
        ).values()
        # b = a[0]
        if a:
            shelve = storeFixtures.objects.get(locationId=tutorial_data["locationId"])
            tutorial_serializer = storeFixturesserializers(shelve, data=tutorial_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED
                )
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = storeFixturesserializers(data=tutorial_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED
                )
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
@api_view(["PUT"])
def groundplot_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        a = groundplot.objects.filter(locationId=tutorial_data["locationId"]).values()
        aa = json.loads(json_util.dumps(tutorial_data))  # b = a[0]
        if a:
            ground = groundplot.objects.get(locationId=tutorial_data["locationId"])
            tutorial_serializer = groundplotserializers(ground, data=tutorial_data)
            if tutorial_serializer.is_valid():  # raise_exception=True
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        # a = json.loads(json_util.dumps(tutorial_data))
        else:
            tutorial_serializer = groundplotserializers(data=tutorial_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
@api_view(["PUT"])
def cameraService_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        a = cameraService.objects.filter(
            locationId=tutorial_data["locationId"]
        ).values()
        aa = json.loads(json_util.dumps(tutorial_data))  # b = a[0]
        if a:
            camera = cameraService.objects.get(locationId=tutorial_data["locationId"])
            tutorial_serializer = cameraServiceserializers(camera, data=tutorial_data)
            if tutorial_serializer.is_valid():  # raise_exception=True
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        # a = json.loads(json_util.dumps(tutorial_data))
        else:
            tutorial_serializer = cameraServiceserializers(data=tutorial_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
@api_view(["PUT"])
def cameraInfo_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        a = cameraInfo.objects.filter(locationId=tutorial_data["locationId"]).values()
        aa = json.loads(json_util.dumps(tutorial_data))  # b = a[0]
        if a:
            camera = cameraInfo.objects.get(locationId=tutorial_data["locationId"])
            tutorial_serializer = cameraInfoserializers(camera, data=tutorial_data)
            if tutorial_serializer.is_valid():  # raise_exception=True
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        # a = json.loads(json_util.dumps(tutorial_data))
        else:
            tutorial_serializer = cameraInfoserializers(data=tutorial_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )


@csrf_exempt
@api_view(["PUT"])
def cartManager_(request):
    if request.method == "PUT":
        tutorial_data = JSONParser().parse(request)
        c = json.loads(json_util.dumps(tutorial_data))
        a = cartManager.objects.filter(locationId=tutorial_data["locationId"]).values()
        # b = a[0]
        if a:
            location = cartManager.objects.get(locationId=tutorial_data["locationId"])
            tutorial_serializer = cartManagerserializers(location, data=tutorial_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = cartManagerserializers(data=tutorial_data)
            # c = json.loads(json_util.dumps(tutorial_data))
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
