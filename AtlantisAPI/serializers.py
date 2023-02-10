from rest_framework import serializers
from AtlantisAPI.models import *

#Serializers are used in REST APIs to control the format of the data being sent and received between the client and the server. 


# serializing the the TblActuators in models.py
class ActuatorsSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblActuators
        fields=(
            'greenhouse_id','actuators_id', 'timestamp', 
            'exhaust_fan', 'evaporator_cooler', 'greenhouse_light', 
            'warmer_lamps', 'ac_motors', 'water_pump', 
            'ac_motors', 'water_pump', 'aeration_pump',
            'automatic_baiting_system', 'water_heater', 'water_aerator',
            'water_blender', 'solenoid_valve_1', 'solenoid_valve_2',
            'solenoid_valve_3'
            )

class GreenhouseMSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblGreenhouseMonitoring
        fields=('greenhouse_id', 'gm_id', 'timestamp', 'air_temperature', 'relative_humidity', 'co2_level', 'intensity_illumination')

class WaterSensingtankSerializers (serializers.ModelSerializer):
    class Meta:
        model=TblWaterSensingtank
        fields=('greenhouse_id', 'wst_id', 'timestamp','ph_level', 'elec_conductivity', 'total_dissolved_solids','water_temperature')

class WaterTestBedSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblWaterTestbed
        fields=('greenhouse_id', 'wtb_id', 'timestamp',
        'water_temperature', 'dissolved_o2_level', 'elec_conductivity',
        'total_dissolved_solids', 'nitrite', 'nitrate',
        'ammonia', 'ph_level' )

class WaterBiofilterSerializers(serializers.ModelSerializer):
    class Meta:
        model=TblWaterBiofilter
        fields=('greenhouse_id', 'wbf_id', 'nitrite', 'nitrate', 'ammonia')