from django.contrib.gis.db import models


class Admindivisionlevels(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    level = models.IntegerField(db_column='Level', unique=True)

    class Meta:
        managed = False
        db_table = 'AdminDivisionLevels'


class Admindivisionroadaccident(models.Model):
    admindivisionsid = models.OneToOneField('Admindivisions', models.DO_NOTHING, db_column='AdminDivisionsId',
                                            primary_key=True)
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING, db_column='RoadAccidentsId')

    class Meta:
        managed = False
        db_table = 'AdminDivisionRoadAccident'
        unique_together = (('admindivisionsid', 'roadaccidentsid'),)


class Admindivisionstatuses(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    status = models.TextField(db_column='Status', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AdminDivisionStatuses'


class Admindivisions(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    regioncode = models.TextField(db_column='RegionCode', blank=True, null=True)
    admindivisionstatusid = models.ForeignKey(Admindivisionstatuses, models.DO_NOTHING,
                                              db_column='AdminDivisionStatusId', blank=True,
                                              null=True)
    admindivisionlevelid = models.ForeignKey(Admindivisionlevels, models.DO_NOTHING, db_column='AdminDivisionLevelId',
                                             blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AdminDivisions'


class Associatedtrafficviolationroadaccidentparticipant(models.Model):
    associatedtrafficviolationsid = models.OneToOneField('Associatedtrafficviolations', models.DO_NOTHING,
                                                         db_column='AssociatedTrafficViolationsId',
                                                         primary_key=True)
    roadaccidentparticipantsid = models.ForeignKey('Roadaccidentparticipants', models.DO_NOTHING,
                                                   db_column='RoadAccidentParticipantsId')

    class Meta:
        managed = False
        db_table = 'AssociatedTrafficViolationRoadAccidentParticipant'
        unique_together = (('associatedtrafficviolationsid', 'roadaccidentparticipantsid'),)


class Associatedtrafficviolations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    violation = models.TextField(db_column='Violation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'AssociatedTrafficViolations'


class Roadaccidentcarriagewayconditions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    conditioncarriageway = models.TextField(db_column='ConditionCarriageway', blank=True,
                                            null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentCarriagewayConditions'


class Roadaccidentconcentrations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentscount = models.IntegerField(db_column='RoadAccidentsCount', blank=True,
                                             null=True)
    roadaccidentnducount = models.IntegerField(db_column='RoadAccidentNduCount', blank=True,
                                               null=True)
    roadaccidentconcentrationyear = models.IntegerField(db_column='RoadAccidentConcentrationYear', blank=True,
                                                        null=True)
    died = models.IntegerField(db_column='Died', blank=True, null=True)
    wounded = models.IntegerField(db_column='Wounded', blank=True, null=True)
    inlocality = models.BooleanField(db_column='InLocality', blank=True, null=True)
    roadaccidentconcentrationlength = models.IntegerField(db_column='RoadAccidentConcentrationLength', blank=True,
                                                          null=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentConcentrations'


class Roadaccidentdrivingfactors(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    drivingfactor = models.TextField(db_column='DrivingFactor', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentDrivingFactors'


class Roadaccidentlightnings(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    lighting = models.TextField(db_column='Lighting', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentLightnings'


class Roadaccidentlocationroadlevels(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    roadlevel = models.TextField(db_column='RoadLevel', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentLocationRoadLevels'


class Roadaccidentlocations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentid = models.OneToOneField('Roadaccidents', models.DO_NOTHING,
                                          db_column='RoadAccidentId')
    roadname = models.TextField(db_column='RoadName', blank=True, null=True)
    roadcategory = models.IntegerField(db_column='RoadCategory', blank=True, null=True)
    roadaccidentlocationroadlevelid = models.ForeignKey(Roadaccidentlocationroadlevels, models.DO_NOTHING,
                                                        db_column='RoadAccidentLocationRoadLevelId', blank=True,
                                                        null=True)
    region = models.TextField(db_column='Region', blank=True, null=True)
    settlement = models.TextField(db_column='Settlement', blank=True, null=True)
    district = models.TextField(db_column='District', blank=True, null=True)
    street = models.TextField(db_column='Street', blank=True, null=True)
    housenumber = models.TextField(db_column='HouseNumber', blank=True, null=True)
    measurekm = models.TextField(db_column='MeasureKm', blank=True, null=True)
    measurem = models.TextField(db_column='MeasureM', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentLocations'


class Roadaccidentndus(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    ndu = models.TextField(db_column='Ndu', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentNdus'


class Roadaccidentparticipantconditions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    condition = models.TextField(db_column='Condition', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipantConditions'


class Roadaccidentparticipanthidingfromroadaccidentplaces(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    hidingfromroadaccidentplace = models.TextField(db_column='HidingFromRoadAccidentPlace', blank=True,
                                                   null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipantHidingFromRoadAccidentPlaces'


class Roadaccidentparticipantsexes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    sex = models.TextField(db_column='Sex', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipantSexes'


class Roadaccidentparticipanttrafficviolation(models.Model):
    roadaccidentparticipantsid = models.OneToOneField('Roadaccidentparticipants', models.DO_NOTHING,
                                                      db_column='RoadAccidentParticipantsId',
                                                      primary_key=True)
    trafficviolationsid = models.ForeignKey('Trafficviolations', models.DO_NOTHING,
                                            db_column='TrafficViolationsId')

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipantTrafficViolation'
        unique_together = (('roadaccidentparticipantsid', 'trafficviolationsid'),)


class Roadaccidentparticipanttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    type = models.TextField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipantTypes'


class Roadaccidentparticipants(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                       db_column='RoadAccidentId')
    roadaccidentvehicleid = models.ForeignKey('Roadaccidentvehicles', models.DO_NOTHING,
                                              db_column='RoadAccidentVehicleId', blank=True,
                                              null=True)
    roadaccidentparticipanttypeid = models.ForeignKey(Roadaccidentparticipanttypes, models.DO_NOTHING,
                                                      db_column='RoadAccidentParticipantTypeId', blank=True,
                                                      null=True)
    roadaccidentparticipantconditionid = models.ForeignKey(Roadaccidentparticipantconditions, models.DO_NOTHING,
                                                           db_column='RoadAccidentParticipantConditionId', blank=True,
                                                           null=True)
    roadaccidentparticipantsexid = models.ForeignKey(Roadaccidentparticipantsexes, models.DO_NOTHING,
                                                     db_column='RoadAccidentParticipantSexId', blank=True,
                                                     null=True)
    drivingexperience = models.IntegerField(db_column='DrivingExperience', blank=True,
                                            null=True)
    alcoholcount = models.TextField(db_column='AlcoholCount', blank=True, null=True)
    safetybelt = models.BooleanField(db_column='SafetyBelt', blank=True, null=True)
    roadaccidentparticipanthidingfromroadaccidentplaceid = models.ForeignKey(
        Roadaccidentparticipanthidingfromroadaccidentplaces, models.DO_NOTHING,
        db_column='RoadAccidentParticipantHidingFromRoadAccidentPlaceId', blank=True,
        null=True)
    seatgroup = models.TextField(db_column='SeatGroup', blank=True, null=True)
    injuredcartid = models.TextField(db_column='InjuredCartId', blank=True, null=True)
    number = models.IntegerField(db_column='Number', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentParticipants'


class Roadaccidentroadaccidentdrivingfactor(models.Model):
    roadaccidentdrivingfactorsid = models.OneToOneField(Roadaccidentdrivingfactors, models.DO_NOTHING,
                                                        db_column='RoadAccidentDrivingFactorsId',
                                                        primary_key=True)
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                        db_column='RoadAccidentsId')

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadAccidentDrivingFactor'
        unique_together = (('roadaccidentdrivingfactorsid', 'roadaccidentsid'),)


class Roadaccidentroadaccidentndu(models.Model):
    roadaccidentndusid = models.OneToOneField(Roadaccidentndus, models.DO_NOTHING, db_column='RoadAccidentNdusId',
                                              primary_key=True)  # Field name made lowercase. The composite primary key (RoadAccidentNdusId, RoadAccidentsId) found, that is not supported. The first column is selected.
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                        db_column='RoadAccidentsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadAccidentNdu'
        unique_together = (('roadaccidentndusid', 'roadaccidentsid'),)


class Roadaccidentroadaccidentudsnearobject(models.Model):
    roadaccidentudsnearobjectsid = models.OneToOneField('Roadaccidentudsnearobjects', models.DO_NOTHING,
                                                        db_column='RoadAccidentUdsNearObjectsId',
                                                        primary_key=True)  # Field name made lowercase. The composite primary key (RoadAccidentUdsNearObjectsId, RoadAccidentsId) found, that is not supported. The first column is selected.
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                        db_column='RoadAccidentsId')  # Field name made lowercase.

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadAccidentUdsNearObject'
        unique_together = (('roadaccidentudsnearobjectsid', 'roadaccidentsid'),)


class Roadaccidentroadaccidentudsplaceobject(models.Model):
    roadaccidentudsplaceobjectsid = models.OneToOneField('Roadaccidentudsplaceobjects', models.DO_NOTHING,
                                                         db_column='RoadAccidentUdsPlaceObjectsId',
                                                         primary_key=True)
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                        db_column='RoadAccidentsId')

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadAccidentUdsPlaceObject'
        unique_together = (('roadaccidentudsplaceobjectsid', 'roadaccidentsid'),)


class Roadaccidentroadaccidentweathercondition(models.Model):
    roadaccidentweatherconditionsid = models.OneToOneField('Roadaccidentweatherconditions', models.DO_NOTHING,
                                                           db_column='RoadAccidentWeatherConditionsId',
                                                           primary_key=True)
    roadaccidentsid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                        db_column='RoadAccidentsId')

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadAccidentWeatherCondition'
        unique_together = (('roadaccidentweatherconditionsid', 'roadaccidentsid'),)


class Roadaccidentroadmotionchanges(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    roadmotionchange = models.TextField(db_column='RoadMotionChange', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadMotionChanges'


class Roadaccidentroadtypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    roadtype = models.TextField(db_column='RoadType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentRoadTypes'


class Roadaccidentschemaimagecodes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    schemaimagecode = models.TextField(db_column='SchemaImageCode', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentSchemaImageCodes'


class Roadaccidenttypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    type = models.TextField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentTypes'


class Roadaccidentudsnearobjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    udsnearobject = models.TextField(db_column='UdsNearObject', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentUdsNearObjects'


class Roadaccidentudsplaceobjects(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    udsobjectsplace = models.TextField(db_column='UdsObjectsPlace', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentUdsPlaceObjects'


class Roadaccidentvalidations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentid = models.OneToOneField('Roadaccidents', models.DO_NOTHING,
                                          db_column='RoadAccidentId')
    onroad = models.BooleanField(db_column='OnRoad', blank=True, null=True)
    isregionmatch = models.BooleanField(db_column='IsRegionMatch', blank=True, null=True)
    isaccurate = models.BooleanField(db_column='IsAccurate', blank=True, null=True)
    inwater = models.BooleanField(db_column='InWater', blank=True, null=True)
    isvalid = models.BooleanField(db_column='IsValid', blank=True, null=True)
    validpercent = models.IntegerField(db_column='ValidPercent', blank=True, null=True)
    matchingregion = models.TextField(db_column='MatchingRegion', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentValidations'


class Roadaccidentvehiclebrands(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    brand = models.TextField(db_column='Brand', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleBrands'


class Roadaccidentvehicledrivetypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    drivetype = models.TextField(db_column='DriveType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleDriveTypes'


class Roadaccidentvehiclemodels(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    model = models.TextField(db_column='Model', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleModels'


class Roadaccidentvehicleownertypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    ownertype = models.TextField(db_column='OwnerType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleOwnerTypes'


class Roadaccidentvehicleownershiptypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    ownershiptype = models.TextField(db_column='OwnershipType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleOwnershipTypes'


class Roadaccidentvehicleroadaccidentplacelivings(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    roadaccidentplaceliving = models.TextField(db_column='RoadAccidentPlaceLiving', blank=True,
                                               null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleRoadAccidentPlaceLivings'


class Roadaccidentvehicletechissues(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    techissue = models.TextField(db_column='TechIssue', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleTechIssues'


class Roadaccidentvehicletypes(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    type = models.TextField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicleTypes'


class Roadaccidentvehicles(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentid = models.ForeignKey('Roadaccidents', models.DO_NOTHING,
                                       db_column='RoadAccidentId')
    number = models.IntegerField(db_column='Number', blank=True, null=True)
    roadaccidentvehicletypeid = models.ForeignKey(Roadaccidentvehicletypes, models.DO_NOTHING,
                                                  db_column='RoadAccidentVehicleTypeId', blank=True,
                                                  null=True)
    roadaccidentvehiclebrandid = models.ForeignKey(Roadaccidentvehiclebrands, models.DO_NOTHING,
                                                   db_column='RoadAccidentVehicleBrandId', blank=True,
                                                   null=True)
    roadaccidentvehiclemodelid = models.ForeignKey(Roadaccidentvehiclemodels, models.DO_NOTHING,
                                                   db_column='RoadAccidentVehicleModelId', blank=True,
                                                   null=True)
    color = models.TextField(db_column='Color', blank=True, null=True)
    roadaccidentvehicledrivetypeid = models.ForeignKey(Roadaccidentvehicledrivetypes, models.DO_NOTHING,
                                                       db_column='RoadAccidentVehicleDriveTypeId', blank=True,
                                                       null=True)
    manufactureyear = models.IntegerField(db_column='ManufactureYear', blank=True,
                                          null=True)
    destruction = models.TextField(db_column='Destruction', blank=True, null=True)
    roadaccidentvehicletechissueid = models.ForeignKey(Roadaccidentvehicletechissues, models.DO_NOTHING,
                                                       db_column='RoadAccidentVehicleTechIssueId', blank=True,
                                                       null=True)
    roadaccidentvehicleownershiptypeid = models.ForeignKey(Roadaccidentvehicleownershiptypes, models.DO_NOTHING,
                                                           db_column='RoadAccidentVehicleOwnershipTypeId', blank=True,
                                                           null=True)
    roadaccidentvehicleownertypeid = models.ForeignKey(Roadaccidentvehicleownertypes, models.DO_NOTHING,
                                                       db_column='RoadAccidentVehicleOwnerTypeId', blank=True,
                                                       null=True)
    roadaccidentvehicleroadaccidentplacelivingid = models.ForeignKey(Roadaccidentvehicleroadaccidentplacelivings,
                                                                     models.DO_NOTHING,
                                                                     db_column='RoadAccidentVehicleRoadAccidentPlaceLivingId',
                                                                     blank=True,
                                                                     null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentVehicles'


class Roadaccidentweatherconditions(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    weathercondition = models.TextField(db_column='WeatherCondition', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidentWeatherConditions'


class Roadaccidents(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    kartid = models.IntegerField(db_column='KartId')
    datetime = models.DateTimeField(db_column='DateTime')
    roadaccidenttypeid = models.ForeignKey(Roadaccidenttypes, models.DO_NOTHING, db_column='RoadAccidentTypeId',
                                           blank=True, null=True)
    roadaccidentroadtypeid = models.ForeignKey(Roadaccidentroadtypes, models.DO_NOTHING,
                                               db_column='RoadAccidentRoadTypeId', blank=True,
                                               null=True)
    died = models.IntegerField(db_column='Died')
    wounded = models.IntegerField(db_column='Wounded')
    vehiclenumber = models.IntegerField(db_column='VehicleNumber')
    participantnumber = models.IntegerField(db_column='ParticipantNumber')
    roadaccidentcarriagewayconditionid = models.ForeignKey(Roadaccidentcarriagewayconditions, models.DO_NOTHING,
                                                           db_column='RoadAccidentCarriagewayConditionId', blank=True,
                                                           null=True)
    roadaccidentlightningid = models.ForeignKey(Roadaccidentlightnings, models.DO_NOTHING,
                                                db_column='RoadAccidentLightningId', blank=True,
                                                null=True)
    roadaccidentroadmotionchangeid = models.ForeignKey(Roadaccidentroadmotionchanges, models.DO_NOTHING,
                                                       db_column='RoadAccidentRoadMotionChangeId', blank=True,
                                                       null=True)
    roadaccidentschemaimagecodeid = models.ForeignKey(Roadaccidentschemaimagecodes, models.DO_NOTHING,
                                                      db_column='RoadAccidentSchemaImageCodeId', blank=True,
                                                      null=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)
    originalgeom = models.GeometryField(db_column='OriginalGeom', blank=True, null=True)
    roadaccidentconcentrationid = models.ForeignKey(Roadaccidentconcentrations, models.DO_NOTHING,
                                                    db_column='RoadAccidentConcentrationId', blank=True,
                                                    null=True)

    class Meta:
        managed = False
        db_table = 'RoadAccidents'


class Roadgraphroadtypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadtype = models.TextField(db_column='RoadType', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadGraphRoadTypes'


class Roadgraphs(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    maxspeed = models.IntegerField(db_column='MaxSpeed')
    isbridge = models.BooleanField(db_column='IsBridge')
    istunnel = models.BooleanField(db_column='IsTunnel')
    isoneway = models.BooleanField(db_column='IsOneway')
    roadgraphroadtypeid = models.ForeignKey(Roadgraphroadtypes, models.DO_NOTHING, db_column='RoadGraphRoadTypeId',
                                            blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'RoadGraphs'


class Trafficviolations(models.Model):
    id = models.AutoField(db_column='Id', primary_key=True)
    violation = models.TextField(db_column='Violation', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'TrafficViolations'


class Waterzonetypes(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    type = models.TextField(db_column='Type', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'WaterZoneTypes'


class Waterzones(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)
    name = models.TextField(db_column='Name', blank=True, null=True)
    waterzonetypeid = models.ForeignKey(Waterzonetypes, models.DO_NOTHING, db_column='WaterZoneTypeId', blank=True,
                                        null=True)

    class Meta:
        managed = False
        db_table = 'WaterZones'


class Yandexgeocodervalidations(models.Model):
    id = models.UUIDField(db_column='Id', primary_key=True)
    roadaccidentid = models.OneToOneField(Roadaccidents, models.DO_NOTHING,
                                          db_column='RoadAccidentId')
    distancedifference = models.FloatField(db_column='DistanceDifference', blank=True,
                                           null=True)
    addresstext = models.TextField(db_column='AddressText', blank=True, null=True)
    addresstype = models.TextField(db_column='AddressType', blank=True, null=True)
    geom = models.GeometryField(db_column='Geom', blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'YandexGeocoderValidations'


class Efmigrationshistory(models.Model):
    migrationid = models.CharField(db_column='MigrationId', primary_key=True,
                                   max_length=150)
    productversion = models.CharField(db_column='ProductVersion', max_length=32)

    class Meta:
        managed = False
        db_table = '__EFMigrationsHistory'
