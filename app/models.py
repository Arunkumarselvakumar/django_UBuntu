from djongo import models


class storeFloorPlan(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    planId = models.CharField(max_length=100, blank=False, default="")
    planName = models.CharField(max_length=100, blank=False, default="")
    length = models.FloatField(blank=False)
    width = models.FloatField(blank=False)
    height = models.FloatField(blank=False)
    entryCount = models.IntegerField(blank=False)
    exitCount = models.IntegerField(blank=False)
    entryId = models.CharField(max_length=100, blank=False, default="")
    exitid = models.CharField(max_length=100, blank=False, default="")
    entryPoint = models.FloatField(blank=False)
    exitPoint = models.FloatField(blank=False)
    gondolaCount = models.IntegerField(blank=False)
    cameraCount = models.IntegerField(blank=False)
    turnstileCount = models.IntegerField(blank=False)
    turnstileId = models.CharField(max_length=200, blank=False, default="")
    turnstileIP = models.CharField(max_length=100, blank=False, default="")


class storeFixtures(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    gondolaID = models.CharField(max_length=100, blank=False, default="")
    gondolaLocation = models.ListField(models.DictField(blank=False))
    gondolaDimension = models.FloatField(blank=False)
    shelfCount = models.IntegerField(blank=False)
    shelfId = models.ListField()
    boardID = models.CharField(max_length=200, blank=False, default="")
    boardIP_MAC = models.CharField(max_length=100, blank=False, default="")
    boardTopicName = models.CharField(max_length=100, blank=False, default="")
    boardProductName = models.CharField(max_length=100, blank=False, default="")


class cameraService(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    redisTableName = models.CharField(max_length=100, blank=False, default="")
    redisTableOpenpose = models.CharField(max_length=200, blank=False, default="")
    weights = models.CharField(max_length=200, blank=True, default="")
    weights_Head = models.CharField(max_length=200, blank=True, default="")
    xLim = models.IntegerField(blank=False)
    yLim = models.IntegerField(blank=False)


class cameraInfo(models.Model):
    locationId = models.CharField(max_length=100, unique=True, primary_key=True)
    CameraInfo = models.DictField(blank=False)


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
