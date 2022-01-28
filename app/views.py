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
    camera,
    smartshelf
)
from django.views.decorators.csrf import csrf_exempt
from rest_framework.decorators import api_view
from rest_framework import status
from app.serializers import (
    gondolaserializers,
    locationSetupserializers,
    cameraandGPUserializers,
    groundplotserializers,
    cartManagerserializers,
    turnstileserializers,
    storeDimensionserializers,
    cameraserializers,
    smartshelfserializers
)

##camera starts
@csrf_exempt
@api_view(["POST","PUT","GET","DELETE"])
def camera_(request):
    user_data = JSONParser().parse(request)
    response = {}
    if request.method == 'PUT':
        try:
            cameraId = user_data['cameraId']
            location = camera.objects.get(locationId=user_data['locationId'])
            gond = camera.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['camera']
            fb = next((item for item in res1 if item["cameraId"] == cameraId), None)
            gon_dat = user_data
            gon_dat.pop("locationId")
            fb.update(gon_dat)
            tutorial_serializer = cameraserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0] 
                return JsonResponse(response, status=status.HTTP_201_CREATED) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="Camera ID not found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            cameraId = user_data['cameraId']
            location = camera.objects.get(locationId=user_data['locationId'])
            gond = camera.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['camera']
            for i in range(len(res1)):
                if res1[i].get('cameraId') == cameraId:
                    del res1[i]
                    break
            tutorial_serializer = cameraserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0] 
                return JsonResponse(response, status=status.HTTP_200_OK) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="Camera ID not found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = camera.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = camera.objects.get(locationId=user_data['locationId'])
            gond = camera.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['camera']
            c = []
            n = user_data["camera"][0]["cameraId"]
            for i in range(0,len(aa[0]["camera"])):
                c.append((aa[0]["camera"][i]["cameraId"]))
            if n in c:
                response["status"]="Failed"
                response["data"]="camera Id exits"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            else:
                aa[0]["camera"].append(user_data["camera"][0])

            tutorial_serializer = cameraserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(
                    response, status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cameraserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(
                    response, status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        try:
            pagenumber=int(request.GET.get('pagenumber',None))
            itemcount=int(request.GET.get('itemcount',None))
            gond = camera.objects.filter(locationId=user_data['locationId'])
            if gond:
                aa = json.loads(json_util.dumps(gond.values()))
                aa[0].update({"camera":sorted(aa[0]["camera"], key=lambda d: int(d["cameraId"]))})
                ic = pagenumber*itemcount
                startobj = (ic)-itemcount
                aa[0]["camera"]=aa[0]["camera"][startobj:ic]
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_200_OK)
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)

##camera ends here
##camerafilter starts here
@csrf_exempt
@api_view(["GET"])
def camera_filters(request):
    response={}
    user_data = JSONParser().parse(request)
    if request.method == "GET":
        try:
            gond = camera.objects.filter(locationId=user_data['locationId'])
            cameraId=request.GET.get('cameraId',None)
            serialNumber=request.GET.get('serialNumber',None)
            cameraType=request.GET.get('cameraType',None)
            cameraLocation=request.GET.get('cameraLocation',None)
            calibrationData=request.GET.get('calibrationData',None)
            calibrationData_75=request.GET.get('calibrationData_75',None)
            calibrationLog=request.GET.get('calibrationLog',None)
            gpuIndex=request.GET.get('gpuIndex',None)
            usbPort=request.GET.get('usbPort',None)
            def filters(gond,keys,values):
                if gond:
                    aa = json.loads(json_util.dumps(gond.values()))
                    res1 = aa[0]["camera"]
                    z = []
                    for a in res1:
                        for k,v in a.items():
                            v = str(v)
                            if k == keys:
                                if values in v:
                                    z.append(a)
                    g = ({"camera":sorted(z, key=lambda d: int(d["cameraId"]))})        
                    response["status"]="pass"
                    response["data"]=g
                    return JsonResponse(response,status=status.HTTP_200_OK)
                    
                else:
                    response["status"]="Failed"
                    response["data"]="Data not Found"
                    return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            if cameraId:
                return filters(gond,"cameraId",cameraId)
            if serialNumber:
                return filters(gond,"serialNumber",serialNumber)
            if cameraType:
                return filters(gond,"cameraType",cameraType)
            if cameraLocation:
                return filters(gond,"cameraLocation",cameraLocation)
            if calibrationData:
                return filters(gond,"calibrationData",calibrationData)
            if calibrationData_75:
                return filters(gond,"calibrationData_75",calibrationData_75)
            if calibrationLog:
                return filters(gond,"calibrationLog",calibrationLog)
            if gpuIndex:
                return filters(gond,"gpuIndex",str(gpuIndex))
            if usbPort:
                return filters(gond,"usbPort",str(usbPort))
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)       
##camerafilter ends here

@csrf_exempt
@api_view(["POST","GET"])
def storeDimension_(request):
    response = {}
    user_data = JSONParser().parse(request)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = storeDimension.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = storeDimension.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = storeDimensionserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = storeDimensionserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
     #This will give ALL Gondola data 
    if request.method == "GET": 
        try:
            gond = storeDimension.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            response["status"]="pass"
            response["data"]=aa[0]
            return JsonResponse(response,status=status.HTTP_200_OK)
        except:
            response["status"]="Failed"
            response["data"]= "Data Not Found"
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST","PUT","GET","DELETE"])
def turnstile_(request):
    response = {}
    user_data = JSONParser().parse(request) 
    if request.method == 'PUT':
        try:
            turnstileId = user_data['turnstileId']
            location = turnstile.objects.get(locationId=user_data['locationId'])
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['turnstile']
            fb = next((item for item in res1 if item["turnstileId"] == turnstileId), None)
            gon_dat = user_data
            gon_dat.pop("locationId")
            fb.update(gon_dat)
            tutorial_serializer = turnstileserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="Turntile ID not found"
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
    ##delete turntile by id
    if request.method == 'DELETE':
        try:
            turnstileId = user_data['turnstileId']
            location = turnstile.objects.get(locationId=user_data['locationId'])
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['turnstile']
            print("1111",res1)
            for i in range(len(res1)):
                if res1[i].get('turnstileId') == turnstileId:
                    del res1[i]
                    break
            tutorial_serializer = turnstileserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0] 
                return JsonResponse(response, status=status.HTTP_200_OK) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="Turntile ID not found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    # end of delete
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = turnstile.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = turnstile.objects.get(locationId=user_data['locationId'])
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            c = []
            n = user_data["turnstile"][0]["turnstileId"]
            for i in range(0,len(aa[0]["turnstile"])):
                c.append((aa[0]["turnstile"][i]["turnstileId"]))
            if n in c:
                response["status"]="Failed"
                response["data"]="turnstile id exits"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST )
            else:
                aa[0]["turnstile"].append(user_data["turnstile"][0])

            tutorial_serializer = turnstileserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = turnstileserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data based on pagination
    if request.method == "GET":
        try:
            pagenumber=int(request.GET.get('pagenumber',None))
            itemcount=int(request.GET.get('itemcount',None))
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            if gond:
                aa = json.loads(json_util.dumps(gond.values()))
                aa[0].update({"turnstile":sorted(aa[0]["turnstile"], key=lambda d: int(d["turnstileId"]))})
                ic = pagenumber*itemcount
                startobj = (ic)-itemcount
                aa[0]["turnstile"]=aa[0]["turnstile"][startobj:ic]
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_200_OK)
            response["status"]="Failed"
            response["data"]= "Data Not Found"
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]= "Data Not Found"
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

#turnstile filters starts here
@csrf_exempt
@api_view(["GET"])
def turnstile_filters(request):
    response = {}
    user_data = JSONParser().parse(request)
    if request.method == "GET":
        try:
            gond = turnstile.objects.filter(locationId=user_data['locationId'])
            turnstileId=request.GET.get('turnstileId',None)
            turnstileIp=request.GET.get('turnstileIp',None)
            locationNumber=request.GET.get('locationNumber',None)
            turnstileLocation=request.GET.get('turnstileLocation',None)
            def filters(gond,keys,values):
                if gond:
                    aa = json.loads(json_util.dumps(gond.values()))
                    res1 = aa[0]["turnstile"]
                    z = []
                    for a in res1:
                        for k,v in a.items():
                            if k == keys:
                                if values in v:
                                    z.append(a)
                    g = ({"turnstile":sorted(z, key=lambda d: int(d["turnstileId"]))})
                    response["status"]="pass"
                    response["data"]=g
                    return JsonResponse(response, status=status.HTTP_200_OK)
                    
                else:
                    response["status"]="Failed"
                    response["data"]="Data not Found"
                    return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            if turnstileId:
                return filters(gond,"turnstileId",turnstileId)
            if turnstileIp:
                return filters(gond,"turnstileIp",turnstileIp)
            if locationNumber:
                return filters(gond,"locationNumber",locationNumber)
            if turnstileLocation:
                return filters(gond,"turnstileLocation",turnstileLocation)
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)       
#turnstile filters ends here
@csrf_exempt
@api_view(["POST","GET"])
def cartManager_(request):
    response = {}
    user_data = JSONParser().parse(request)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = cartManager.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = cartManager.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = cartManagerserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cartManagerserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = cartManager.objects.filter(locationId=user_data['locationId'])
        if gond:
            aa = json.loads(json_util.dumps(gond.values()))
            response["status"]="pass"
            response["data"]=aa[0]
            return JsonResponse(response,status=status.HTTP_200_OK)
        else:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST","GET"])
def groundplot_(request):
    response = {}
    user_data = JSONParser().parse(request)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = groundplot.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = groundplot.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = groundplotserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = groundplotserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = groundplot.objects.filter(locationId=user_data['locationId'])
        if gond:
            aa = json.loads(json_util.dumps(gond.values()))
            response["status"]="pass"
            response["data"]=aa[0]
            return JsonResponse(response,status=status.HTTP_200_OK)
        else:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)

@csrf_exempt
@api_view(["POST","GET"])
def cameraandGPU_(request):
    response = {}
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
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = cameraandGPUserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = cameraandGPU.objects.filter(locationId=user_data['locationId'])
        if gond:
            aa = json.loads(json_util.dumps(gond.values()))
            response["status"]="pass"
            response["data"]=aa[0]
            return JsonResponse(response,status=status.HTTP_200_OK)
        else:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)


@csrf_exempt
@api_view(["POST","GET"])
def locationSetup_(request):
    response = {}
    user_data = JSONParser().parse(request)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = locationSetup.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = locationSetup.objects.get(locationId=user_data["locationId"])
            tutorial_serializer = locationSetupserializers(location, data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = locationSetupserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        gond = locationSetup.objects.filter(locationId=user_data['locationId'])
        if gond:
            aa = json.loads(json_util.dumps(gond.values()))
            response["status"]="pass"
            response["data"]=aa[0]
            return JsonResponse(response,status=status.HTTP_200_OK)
        else:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)


#mgondola starts here
@csrf_exempt
@api_view(["POST","GET"])
def mgondola_(request):
    response = {}
    user_data = JSONParser().parse(request)
    aa = json.loads(json_util.dumps(user_data))
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = gondola.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = gondola.objects.get(locationId=user_data["locationId"])
            gond = gondola.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            c = []
            n = user_data["gondola"][0]["gondolaId"]
            for i in range(0,len(aa[0]["gondola"])):
                c.append((aa[0]["gondola"][i]["gondolaId"]))
            if n in c:
                response["status"]="Failed"
                response["data"]="gondola id exits"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST )
            else:
                aa[0]["gondola"].append(user_data["gondola"][0])
            tutorial_serializer = gondolaserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = gondolaserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(response,status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
               response, status=status.HTTP_400_BAD_REQUEST)


        
    #This will give ALL Gondola data 
    if request.method == "GET": 
        try:
            pagenumber=int(request.GET.get('pagenumber',None))
            itemcount=int(request.GET.get('itemcount',None))
            gond = gondola.objects.filter(locationId=user_data['locationId'])
            if gond:
                aa = json.loads(json_util.dumps(gond.values()))
                aa[0].update({"gondola":sorted(aa[0]["gondola"], key=lambda d: int(d["gondolaId"]))})
                ic = pagenumber*itemcount
                startobj = (ic)-itemcount
                aa[0]["gondola"]=aa[0]["gondola"][startobj:ic]
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_200_OK)
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
#mgondola ends here 
#mgondolafilters starts here
@csrf_exempt
@api_view(["GET"])
def mgondolafilters(request):
    response = {}
    user_data = JSONParser().parse(request)
    if request.method == "GET":
        try:
            gond = gondola.objects.filter(locationId=user_data['locationId'])
            gondolaId=request.GET.get('gondolaId',None)
            gondolaDimension=request.GET.get('gondolaDimension',None)
            shelfCount=request.GET.get('shelfCount',None)
            gondolaLocation=request.GET.get('gondolaLocation',None)
            def filters(gond,keys,values):
                if gond:
                    aa = json.loads(json_util.dumps(gond.values()))
                    res1 = aa[0]["gondola"]
                    z = []
                    for a in res1:
                        for k,v in a.items():
                            v = str(v)
                            values=str(values)
                            if k == keys:
                                if values in v:
                                    z.append(a)
                    g = ({"gondola":sorted(z, key=lambda d: int(d["gondolaId"]))})        
                    response["status"] = "pass"
                    response["data"] = g
                    return JsonResponse(response, status=status.HTTP_200_OK)
                    
                else:
                    response["status"]="Failed"
                    response["data"]="Data not Found"
                    return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            if gondolaId:
                return filters(gond,"gondolaId",gondolaId)
            if gondolaDimension:
                return filters(gond,"gondolaDimension",gondolaDimension)
            if shelfCount:
                return filters(gond,"shelfCount",shelfCount)
            if gondolaLocation:
                return filters(gond,"gondolaLocation",gondolaLocation)
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)       
#mgondolafilters ends here
#fgondola starts here 
@csrf_exempt
@api_view(["GET","PUT","DELETE"])
def fgondola_(request):
    response = {}
    user_data = JSONParser().parse(request)
    gond = gondola.objects.filter(locationId=user_data['locationId'])
    gondolaId = user_data['gondolaId']
    aa = json.loads(json_util.dumps(gond.values()))
     # This we are going to send Gondola id wise data 
         
    if request.method == 'GET':
        try:
            res1 = aa[0]['gondola']
            fb = next((item for item in res1 if item["gondolaId"] == gondolaId), None)
            if fb:
                response["status"]="pass"
                response["data"]=fb
                return JsonResponse(response,status=status.HTTP_200_OK)
            else:
                response["status"]="Failed"
                response["data"]="Gondola Id not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="Gondola Id not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)

    # this will update Gandola id wise data
    if request.method == 'PUT':
        try:
            location = gondola.objects.get(locationId=user_data['locationId'])
            res1 = aa[0]['gondola']
            fb = next((item for item in res1 if item["gondolaId"] == gondolaId), None)
            gon_dat = user_data
            gon_dat.pop("locationId")
            fb.update(gon_dat)
            tutorial_serializer = gondolaserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=fb
                return JsonResponse(response,status=status.HTTP_201_CREATED) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]= "Gondola Id not found"
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
    
    if request.method == 'DELETE':
        try:
            location = gondola.objects.get(locationId=user_data['locationId'])
            res1 = aa[0]['gondola']
            for i in range(len(res1)):
                if res1[i].get('gondolaId') == gondolaId:
                    del res1[i]
                    break
            tutorial_serializer = gondolaserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_200_OK) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]= "Gondola Id not found"
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
#fgondola ends here
#digitshelf starts here
@csrf_exempt
@api_view(["POST","PUT","GET","DELETE"])
def smartshelf_(request):
    user_data = JSONParser().parse(request)
    response = {}
    if request.method == 'PUT':
        try:
            shelfId = user_data['shelfId']
            location = smartshelf.objects.get(locationId=user_data['locationId'])
            gond = smartshelf.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['digitshelf']
            fb = next((item for item in res1 if item["shelfId"] == shelfId), None)
            gon_dat = user_data
            gon_dat.pop("locationId")
            fb.update(gon_dat)
            tutorial_serializer = smartshelfserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0] 
                return JsonResponse(response, status=status.HTTP_201_CREATED) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="sheld ID not found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    if request.method == 'DELETE':
        try:
            shelfId = user_data['shelfId']
            location = smartshelf.objects.get(locationId=user_data['locationId'])
            gond = smartshelf.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['digitshelf']
            for i in range(len(res1)):
                if res1[i].get('shelfId') == shelfId:
                    del res1[i]
                    break
            tutorial_serializer = smartshelfserializers(location, data=aa[0])
            if tutorial_serializer.is_valid(): 
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=aa[0] 
                return JsonResponse(response, status=status.HTTP_200_OK) 
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except:
            response["status"]="Failed"
            response["data"]="shelf ID not found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
    # this will come from CREATE Gondala page only mandatory data or all data for indivial gandola 
    if request.method == "POST": 
        gond = smartshelf.objects.filter(locationId=user_data['locationId'])
        if gond:
            location = smartshelf.objects.get(locationId=user_data['locationId'])
            gond = smartshelf.objects.filter(locationId=user_data['locationId'])
            aa = json.loads(json_util.dumps(gond.values()))
            res1 = aa[0]['digitshelf']
            c = []
            n = user_data["digitshelf"][0]["shelfId"]
            for i in range(0,len(aa[0]["digitshelf"])):
                c.append((aa[0]["digitshelf"][i]["shelfId"]))
            if n in c:
                response["status"]="Failed"
                response["data"]="shelfId exits"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            else:
                aa[0]["digitshelf"].append(user_data["digitshelf"][0])

            tutorial_serializer = smartshelfserializers(location, data=aa[0])
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(
                    response, status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)
        else:
            tutorial_serializer = smartshelfserializers(data=user_data)
            if tutorial_serializer.is_valid():
                tutorial_serializer.save()
                response["status"]="pass"
                response["data"]=tutorial_serializer.data
                return JsonResponse(
                    response, status=status.HTTP_201_CREATED)
            response["status"]="Failed"
            response["data"]=tutorial_serializer.errors
            return JsonResponse(
                response, status=status.HTTP_400_BAD_REQUEST)

    #This will give ALL Gondola data 
    if request.method == "GET": 
        try:
            pagenumber=int(request.GET.get('pagenumber',None))
            itemcount=int(request.GET.get('itemcount',None))
            gond = smartshelf.objects.filter(locationId=user_data['locationId'])
            if gond:
                aa = json.loads(json_util.dumps(gond.values()))
                aa[0].update({"digitshelf":sorted(aa[0]["digitshelf"], key=lambda d: int(d["shelfId"]))})
                ic = pagenumber*itemcount
                startobj = (ic)-itemcount
                aa[0]["digitshelf"]=aa[0]["digitshelf"][startobj:ic]
                response["status"]="pass"
                response["data"]=aa[0]
                return JsonResponse(response,status=status.HTTP_200_OK)
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response, status=status.HTTP_400_BAD_REQUEST)

##camera ends here
##camerafilter starts here
@csrf_exempt
@api_view(["GET"])
def shelf_filters(request):
    response = {}
    user_data = JSONParser().parse(request)
    if request.method == "GET":
        try:
            gond = smartshelf.objects.filter(locationId=user_data['locationId'])
            shelfId=request.GET.get('shelfId',None)
            shelfLocation=request.GET.get('shelfLocation',None)
            shelfMAC=request.GET.get('shelfMAC',None)
            shelfTopic=request.GET.get('shelfTopic',None)
            gondolaID=request.GET.get('gondolaID',None)
            gondolaCoordinates=request.GET.get('gondolaCoordinates',None)
            gondolaDimensions=request.GET.get('gondolaDimensions',None)
            statuss=request.GET.get('status',None)
            batterCapacity=request.GET.get('batterCapacity',None)
            def filters(gond,keys,values):
                if gond:
                    aa = json.loads(json_util.dumps(gond.values()))
                    res1 = aa[0]["digitshelf"]
                    z = []
                    for a in res1:
                        for k,v in a.items():
                            v = str(v)
                            values=str(values)
                            if k == keys:
                                if values in v:
                                    z.append(a)
                    g = ({"digitshelf":sorted(z, key=lambda d: int(d["shelfId"]))})       
                    response["status"] = "pass"
                    response["data"] = g
                    return JsonResponse(response, status=status.HTTP_200_OK)
                    
                else:
                    response["status"]="Failed"
                    response["data"]="Data not Found"
                    return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
            if shelfId:
                return filters(gond,"shelfId",shelfId)
            if shelfLocation:
                return filters(gond,"shelfLocation",shelfLocation)
            if shelfMAC:
                return filters(gond,"shelfMAC",shelfMAC)
            if shelfTopic:
                return filters(gond,"shelfTopic",shelfTopic)
            if gondolaID:
                return filters(gond,"gondolaID",gondolaID)
            if gondolaCoordinates:
                return filters(gond,"gondolaCoordinates",gondolaCoordinates)
            if gondolaDimensions:
                return filters(gond,"gondolaDimensions",gondolaDimensions)
            if statuss:
                return filters(gond,"status",str(statuss))
            if batterCapacity:
                return filters(gond,"batterCapacity",str(batterCapacity))
            else:
                response["status"]="Failed"
                response["data"]="Data not Found"
                return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)
        except TypeError as e:
            response["status"]="Failed"
            response["data"]="Data not Found"
            return JsonResponse(response,status=status.HTTP_400_BAD_REQUEST)       
##digitshelf  ends here