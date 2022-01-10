from django.http import HttpResponse
from django.http.response import JsonResponse
from rest_framework.parsers import JSONParser
import json
from bson import json_util
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
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from app.serializers import (
    mgondolaserializers,
    fgondolaserializers,
    locationSetupserializers,
    cameraandGPUserializers,
    groundplotserializers,
    cartManagerserializers,
    turnstileserializers,
    storeDimensionserializers,
    cameraserializers
)
##camera starts
@csrf_exempt
@api_view(["POST","PUT","GET"])
def camera_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    
    if request.method == 'PUT':
        cameraId = user_data['cameraId']
        location = camera.objects.get(locationId=user_data['locationId'])
        gond = camera.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        print(aa[0])
        res1 = aa[0]['camera']
        fb = next((item for item in res1 if item["cameraId"] == cameraId), None)
        gon_dat = user_data
        gon_dat.pop("locationId")
        fb.update(gon_dat)
        tutorial_serializer = cameraserializers(location, data=aa[0])
        response = {
            "status": "pass",
            "data":aa[0]}
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(response, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = camera.objects.filter(locationId=user_data['locationId'])
        if gond:
            #turnstileId = user_data['turnstileId']
            location = camera.objects.get(locationId=user_data['locationId'])
            gond = camera.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            #print(aa[0])
            res1 = aa[0]['camera']
            c = []
            n = user_data["camera"][0]["cameraId"]
            #print(n,type(n))
            for i in range(0,len(aa[0]["camera"])):
                c.append((aa[0]["camera"][i]["cameraId"]))
            if n in c:
                response = {
                    "status": "error",
                    "errortype" : "camera Id exits",
                    "existing ids" : c
                }
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST )
            else:
                aa[0]["camera"].append(user_data["camera"][0])

            tutorial_serializer = cameraserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cameraserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = camera.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)

##camera ends here
@csrf_exempt
@api_view(["POST","PUT","GET"])
def storeDimension_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = storeDimension.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = storeDimension.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = storeDimensionserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = storeDimensionserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
     #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = storeDimension.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)

@csrf_exempt
@api_view(["POST","PUT","GET"])
def turnstile_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    
    if request.method == 'PUT':
        turnstileId = user_data['turnstileId']
        location = turnstile.objects.get(locationId=user_data['locationId'])
        gond = turnstile.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        print(aa[0])
        res1 = aa[0]['turnstile']
        fb = next((item for item in res1 if item["turnstileId"] == turnstileId), None)
        gon_dat = user_data
        gon_dat.pop("locationId")
        fb.update(gon_dat)
        tutorial_serializer = turnstileserializers(location, data=aa[0])
        response = {
            "status": "pass",
            "data":aa[0]}
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(response, status=status.HTTP_201_CREATED) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = turnstile.objects.filter(locationId=user_data['locationId'])
        if gond:
            #turnstileId = user_data['turnstileId']
            location = turnstile.objects.get(locationId=user_data['locationId'])
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            #print(aa[0])
            res1 = aa[0]['turnstile']
            c = []
            n = user_data["turnstile"][0]["turnstileId"]
            #print(n,type(n))
            for i in range(0,len(aa[0]["turnstile"])):
                c.append((aa[0]["turnstile"][i]["turnstileId"]))
            if n in c:
                response = {
                    "status": "error",
                    "errortype" : "turnstile id exits",
                    "existing ids" : c
                }
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST )
            else:
                aa[0]["turnstile"].append(user_data["turnstile"][0])

            tutorial_serializer = turnstileserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = turnstileserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = turnstile.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)

@csrf_exempt
@api_view(["POST","PUT","GET"])
def cartManager_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = cartManager.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = cartManager.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cartManagerserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cartManagerserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = cartManager.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)

@csrf_exempt
@api_view(["POST","PUT","GET"])
def groundplot_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = groundplot.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = groundplot.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = groundplotserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = groundplotserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = groundplot.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)

@csrf_exempt
@api_view(["POST","PUT","GET"])
def cameraandGPU_(request):
    user_data = JSONParser().parse(request)
    aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = cameraandGPU.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = cameraandGPU.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cameraandGPUserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cameraandGPUserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = cameraandGPU.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)


@csrf_exempt
@api_view(["POST","PUT","GET"])
def locationSetup_(request):
    user_data = JSONParser().parse(request)
    #aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = locationSetup.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = locationSetup.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = locationSetupserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = locationSetupserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = locationSetup.objects.filter(locationId=user_data['locationId'])
        aa = json.loads(json_util.dumps(gond.values()))
        return JsonResponse(aa[0], safe=False)



@csrf_exempt
@api_view(["POST","PUT","GET"])
def mgondola_(request):
    user_data = JSONParser().parse(request)
    aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = gondola.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = gondola.objects.get(locationId=user_data["locationId"])
            #edit starts here
            gond = gondola.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            #print(aa[0])
            #res1 = aa[0]['gondola']
            c = []
            n = user_data["gondola"][0]["gondolaId"]
            #print(n,type(n))
            for i in range(0,len(aa[0]["gondola"])):
                c.append((aa[0]["gondola"][i]["gondolaId"]))
            if n in c:
                response = {
                    "status": "error",
                    "errortype" : "gondola id exits",
                    "existing ids" : c
                }
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST )
            else:
                aa[0]["gondola"].append(user_data["gondola"][0])
            #print(aa[0]["gondola"])
            # edit ends here
            tutorial_serializer = mgondolaserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = mgondolaserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(
                    tutorial_serializer.data, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST)


        
    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = gondola.objects.filter(locationId=user_data['locationId']) 
        aa = json.loads(json_util.dumps(gond.values()))    
        #tutorials_serializer = mgondolaserializers(gond, many=True)
        return JsonResponse(aa[0], safe=False)
   
@csrf_exempt
@api_view(["GET","PUT"])
def fgondola_(request):
    user_data = JSONParser().parse(request)
    gond = gondola.objects.filter(locationId=user_data['locationId'])
    gondolaId = user_data['gondolaId']
    aa = json.loads(json_util.dumps(gond.values()))
     # This we are going to send Gondola id wise data       
    if request.method == 'GET':
        #aa = json.loads(json_util.dumps(gond.values()))
        res1 = aa[0]['gondola']
        fb = next((item for item in res1 if item["gondolaId"] == gondolaId), None)
        #tutorials_serializer = mgondolaserializers(gond, many=True)
        return JsonResponse(fb, safe=False)
    # this will update Gandola id wise data
    if request.method == 'PUT':
        location = gondola.objects.get(locationId=user_data['locationId'])
        #aa = json.loads(json_util.dumps(gond.values()))
        res1 = aa[0]['gondola']
        fb = next((item for item in res1 if item["gondolaId"] == gondolaId), None)
        gon_dat = user_data
        gon_dat.pop("locationId")
        fb.update(gon_dat)
        tutorial_serializer = fgondolaserializers(location, data=aa[0])
        response = {
            "status": "pass",
            "data":fb        }
        if tutorial_serializer.is_valid(): 
            tutorial_serializer.save() 
            return JsonResponse(response) 
        return JsonResponse(tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST) 

"""
@csrf_exempt
@api_view(["GET", "DELETE"])
def all_(request):
    user_data = JSONParser().parse(request)
    if request.method == "GET":
        try:
            a = {}
            try:
                ground = groundplot.objects.filter(
                    locationId=user_data["locationId"]
                ).values()
                if ground:
                    a.update({"groundplot": ground[0]})
            except:
                pass
            store = storeFloorPlan.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            if store:
                a.update({"storeFloorPlan": store[0]})
            camS = cameraService.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            if camS:
                a.update({"cameraService": camS[0]})
            camI = cameraInfo.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            if camI:
                a.update({"cameraInfo": camI[0]})
            she = storeFixtures.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            if she:
                a.update({"storeFixtures": she[0]})
            cart = cartManager.objects.filter(
                locationId=user_data["locationId"]
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
                locationId=user_data["locationId"]
            ).values()
            store1 = storeFloorPlan.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            camS = cameraService.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            camI = cameraInfo.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            she1 = storeFixtures.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            cart = cartManager.objects.filter(
                locationId=user_data["locationId"]
            ).values()
            if ground1 or store1 or camS or she1 or camI or car:

                ground = groundplot.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                store = storeFloorPlan.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                camS = cameraService.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                camI = cameraInfo.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                she = storeFixtures.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                cart = cartManager.objects.filter(
                    locationId=user_data["locationId"]
                ).delete()
                
            response = {user_data["locationId"]: "deleted"}
            c = json.loads(json_util.dumps(response))
            return JsonResponse(c, safe=False)
        except:
            message = {"message": "User Already removed"}
            return JsonResponse(message, safe=False)


@csrf_exempt
@api_view(["PUT"])
def storeFloorPlan_(request):
    if request.method == "PUT":
        user_data = JSONParser().parse(request)
        c = json.loads(json_util.dumps(user_data))
        a = storeFloorPlan.objects.filter(
            locationId=user_data["locationId"]
        ).values()
        if a:
            location = storeFloorPlan.objects.get(
                locationId=user_data["locationId"]
            )
            tutorial_serializer = storeFloorPlanserializers(
                location, data=user_data
            )
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = storeFloorPlanserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )




@csrf_exempt
@api_view(["PUT"])
def groundplot_(request):
    if request.method == "PUT":
        user_data = JSONParser().parse(request)
        a = groundplot.objects.filter(locationId=user_data["locationId"]).values()
        aa = json.loads(json_util.dumps(user_data))
        if a:
            ground = groundplot.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = groundplotserializers(ground, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = groundplotserializers(data=user_data)
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
        user_data = JSONParser().parse(request)
        a = cameraService.objects.filter(
            locationId=user_data["locationId"]
        ).values()
        aa = json.loads(json_util.dumps(user_data))
        if a:
            camera = cameraService.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cameraServiceserializers(camera, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = cameraServiceserializers(data=user_data)
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
        user_data = JSONParser().parse(request)
        a = cameraInfo.objects.filter(locationId=user_data["locationId"]).values()
        aa = json.loads(json_util.dumps(user_data))
        if a:
            camera = cameraInfo.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cameraInfoserializers(camera, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(aa, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )

        else:
            tutorial_serializer = cameraInfoserializers(data=user_data)
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
        user_data = JSONParser().parse(request)
        c = json.loads(json_util.dumps(user_data))
        a = cartManager.objects.filter(locationId=user_data["locationId"]).values()
        if a:
            location = cartManager.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cartManagerserializers(location, data=user_data)
            if tutorial_serializer.is_valid(raise_exception=True):
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
        else:
            tutorial_serializer = cartManagerserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                return JsonResponse(c, status=status.HTTP_201_CREATED)
            return JsonResponse(
                tutorial_serializer.errors, status=status.HTTP_400_BAD_REQUEST
            )
"""