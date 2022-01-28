from djongo import models

class smartshelf(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    digitshelf = models.ListField(blank=False)
    
class gondola(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    gondola = models.ListField(blank=False)

class camera(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    camera = models.ListField(blank=False)
    # serialNumber = models.CharField(max_length=100, blank=False, default="")
    # cameraId = models.CharField(max_length=100, blank=False, default="")
    # cameraType = models.CharField(max_length=100, blank=False, default="")
    # cameraLocation = models.CharField(max_length=100, blank=True, default="")
    # calibrationData = models.CharField(max_length=100, blank=True, default="")
    # calibrationData_75 = models.CharField(max_length=100, blank=True, default="")
    # calibrationLog = models.CharField(max_length=100, blank=True, default="")
    # gpuIndex = models.IntegerField(blank=True)
    # usbPort = models.IntegerField(blank=True)

class turnstile(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    turnstile = models.ListField(blank=False)
    # turunstileId = models.CharField(max_length=200,blank=False, default="")
    # turnstileIp = models.CharField(max_length=200,blank=False, default="")
    # locationNumber = models.CharField(max_length=200,blank=True, default="")
    # turnstileLocation = models.CharField(max_length=200,blank=True, default="")
class storeDimension(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    planId = models.CharField(max_length=100, blank=False, default="")
    planName = models.CharField(max_length=100, blank=False, default="")
    length = models.FloatField(blank=False)
    width = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    entry = models.ListField(blank=False)
    exits = models.ListField(blank=False)
class locationSetup(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    storeType = models.CharField(max_length=200,blank=False, default="")
    nameOfTheRetailBrand = models.CharField(max_length=200,blank=False, default="")

class cameraandGPU(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    redisTableName = models.CharField(max_length=100, blank=False, default="")
    redisTableOpenpose = models.CharField(max_length=200, blank=False, default="")
    weights = models.CharField(max_length=200, blank=True, default="")
    weights_Head = models.CharField(max_length=200, blank=True, default="")
    xLim = models.IntegerField(blank=False)
    yLim = models.IntegerField(blank=False)

class groundplot(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    redisTableName = models.CharField(max_length=200)
    redisOutboundName = models.CharField(max_length=200)
    gpMemoLength = models.IntegerField(blank=False)
    routerBoundary = models.DictField(blank=False)
    calibrationTargets = models.ListField(models.FloatField(blank=False))
    entryGateLocation = models.ListField(blank=False)
    exitGateLocation = models.ListField(blank=False)
    waypoint = models.DictField(blank=False)


class cartManager(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    gPRedisPersonsName = models.CharField(max_length=200)
    productCounterRedisName = models.CharField(max_length=200)
    productUPCTokenFile = models.CharField(max_length=200)
    redisTableOpenpose = models.CharField(max_length=200)
    cameraLocation = models.ListField(blank=False)
    targetedClass = models.ListField(blank=False)
