from django.shortcuts import render
from django.views.decorators.csrf import csrf_exempt
from rest_framework.parsers import JSONParser
from django.http.response import JsonResponse

from AtlantisAPI.models import *
from AtlantisAPI.serializers import *


# Create your views here.
@csrf_exempt
def actuatorsAPI(request, id=0):
    if request.method =='GET':
        actuators = TblActuators.objects.all()
        actuators_serializers = ActuatorsSerializers(actuators, many=True)
        return JsonResponse(actuators_serializers.data, safe=False)

@csrf_exempt
def greenhousemAPI(request, id=0):
    if request.method == 'GET':
        greenhouse_monitoring = TblGreenhouseMonitoring.objects.all()
        greenhousem_serializers = GreenhouseMSerializers(greenhouse_monitoring, many=True)
        return JsonResponse(greenhousem_serializers.data, safe=False)
@csrf_exempt
def watersensingAPI(request, id=0):
    if request.method == 'GET':
        water_sensing = TblWaterSensingtank.objects.all()
        water_sensing_serializers = WaterSensingtankSerializers(water_sensing, many=True)
        return JsonResponse(water_sensing_serializers.data, safe=False)
@csrf_exempt
def watertestbedAPI(request, id=0):
    if request.method == 'GET':
        watertestbed = TblWaterTestbed.objects.all()
        watertestbed_serializers = WaterTestBedSerializers(watertestbed, many=True)
        return JsonResponse(watertestbed_serializers.data, safe=False)

@csrf_exempt
def waterbiofilterAPI(request, id=0):
    if request.method =='GET':
        waterbiofilter = TblWaterBiofilter.objects.all()
        waterbiofilter_serializers = WaterBiofilterSerializers(waterbiofilter, many=True)
        return JsonResponse(waterbiofilter_serializers.data, safe=False)