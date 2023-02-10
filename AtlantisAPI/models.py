from django.db import models

# Models in Django are used to represent the structure of data that is being stored in your application. 

# Create your models here.
class TblActuators(models.Model):
    actuators_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey('TblGreenhouse', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    exhaust_fan = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    evaporator_cooler = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    greenhouse_light = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    warmer_lamps = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    ac_motors = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    water_pump = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    aeration_pump = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    automatic_baiting_system = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    water_heater = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    water_aerator = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    water_blender = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    solenoid_valve_1 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    solenoid_valve_2 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    solenoid_valve_3 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)
    solenoid_valve_4 = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_actuators'


class TblFishData(models.Model):
    fd_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey('TblGreenhouse', models.DO_NOTHING)
    timestamp = models.DateTimeField()
    fish_width = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fish_height = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    fish_weight = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_fish_data'


class TblGreenhouse(models.Model):
    greenhouse_id = models.AutoField(primary_key=True)
    location = models.CharField(max_length=50, blank=True, null=True)
    user = models.ForeignKey('TblUserData', models.DO_NOTHING)

    class Meta:
        managed = False
        db_table = 'tbl_greenhouse'


class TblGreenhouseMonitoring(models.Model):
    gm_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    air_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    relative_humidity = models.IntegerField(blank=True, null=True)
    co2_level = models.IntegerField(blank=True, null=True)
    intensity_illumination = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_greenhouse_monitoring'


class TblPlantData(models.Model):
    pd_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    plant_health = models.DecimalField(max_digits=1, decimal_places=0, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_plant_data'


class TblUserData(models.Model):
    user_id = models.AutoField(primary_key=True)
    username = models.CharField(max_length=25, blank=True, null=True)
    password = models.TextField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_user_data'


class TblWaterBiofilter(models.Model):
    wbf_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    nitrite = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nitrate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ammonia = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_water_biofilter'


class TblWaterSensingtank(models.Model):
    wst_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    ph_level = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    water_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    elec_conductivity = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    total_dissolved_solids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_water_sensingtank'


class TblWaterTestbed(models.Model):
    wtb_id = models.AutoField(primary_key=True)
    greenhouse = models.ForeignKey(TblGreenhouse, models.DO_NOTHING)
    timestamp = models.DateTimeField()
    ph_level = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    water_temperature = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    dissolved_o2_level = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    elec_conductivity = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    total_dissolved_solids = models.DecimalField(max_digits=5, decimal_places=2, blank=True, null=True)
    nitrite = models.DecimalField(max_digits=6, decimal_places=2, blank=True, null=True)
    nitrate = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)
    ammonia = models.DecimalField(max_digits=4, decimal_places=2, blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'tbl_water_testbed'