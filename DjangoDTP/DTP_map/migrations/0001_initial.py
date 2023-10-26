# Generated by Django 4.2.6 on 2023-10-05 12:27

import django.contrib.gis.db.models.fields
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Admindivisionlevels',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('level', models.IntegerField(db_column='Level', unique=True)),
            ],
            options={
                'db_table': 'AdminDivisionLevels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admindivisions',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('regioncode', models.TextField(blank=True, db_column='RegionCode', null=True)),
            ],
            options={
                'db_table': 'AdminDivisions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admindivisionstatuses',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('status', models.TextField(blank=True, db_column='Status', null=True)),
            ],
            options={
                'db_table': 'AdminDivisionStatuses',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Associatedtrafficviolations',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('violation', models.TextField(blank=True, db_column='Violation', null=True)),
            ],
            options={
                'db_table': 'AssociatedTrafficViolations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Efmigrationshistory',
            fields=[
                ('migrationid', models.CharField(db_column='MigrationId', max_length=150, primary_key=True, serialize=False)),
                ('productversion', models.CharField(db_column='ProductVersion', max_length=32)),
            ],
            options={
                'db_table': '__EFMigrationsHistory',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentcarriagewayconditions',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('conditioncarriageway', models.TextField(blank=True, db_column='ConditionCarriageway', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentCarriagewayConditions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentconcentrations',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('roadaccidentscount', models.IntegerField(blank=True, db_column='RoadAccidentsCount', null=True)),
                ('roadaccidentnducount', models.IntegerField(blank=True, db_column='RoadAccidentNduCount', null=True)),
                ('roadaccidentconcentrationyear', models.IntegerField(blank=True, db_column='RoadAccidentConcentrationYear', null=True)),
                ('died', models.IntegerField(blank=True, db_column='Died', null=True)),
                ('wounded', models.IntegerField(blank=True, db_column='Wounded', null=True)),
                ('inlocality', models.BooleanField(blank=True, db_column='InLocality', null=True)),
                ('roadaccidentconcentrationlength', models.IntegerField(blank=True, db_column='RoadAccidentConcentrationLength', null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
            ],
            options={
                'db_table': 'RoadAccidentConcentrations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentdrivingfactors',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('drivingfactor', models.TextField(blank=True, db_column='DrivingFactor', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentDrivingFactors',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentlightnings',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('lighting', models.TextField(blank=True, db_column='Lighting', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentLightnings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentlocationroadlevels',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('roadlevel', models.TextField(blank=True, db_column='RoadLevel', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentLocationRoadLevels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentlocations',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('roadname', models.TextField(blank=True, db_column='RoadName', null=True)),
                ('roadcategory', models.IntegerField(blank=True, db_column='RoadCategory', null=True)),
                ('region', models.TextField(blank=True, db_column='Region', null=True)),
                ('settlement', models.TextField(blank=True, db_column='Settlement', null=True)),
                ('district', models.TextField(blank=True, db_column='District', null=True)),
                ('street', models.TextField(blank=True, db_column='Street', null=True)),
                ('housenumber', models.TextField(blank=True, db_column='HouseNumber', null=True)),
                ('measurekm', models.TextField(blank=True, db_column='MeasureKm', null=True)),
                ('measurem', models.TextField(blank=True, db_column='MeasureM', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentLocations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentndus',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('ndu', models.TextField(blank=True, db_column='Ndu', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentNdus',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipantconditions',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('condition', models.TextField(blank=True, db_column='Condition', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentParticipantConditions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipanthidingfromroadaccidentplaces',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('hidingfromroadaccidentplace', models.TextField(blank=True, db_column='HidingFromRoadAccidentPlace', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentParticipantHidingFromRoadAccidentPlaces',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipants',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('drivingexperience', models.IntegerField(blank=True, db_column='DrivingExperience', null=True)),
                ('alcoholcount', models.TextField(blank=True, db_column='AlcoholCount', null=True)),
                ('safetybelt', models.BooleanField(blank=True, db_column='SafetyBelt', null=True)),
                ('seatgroup', models.TextField(blank=True, db_column='SeatGroup', null=True)),
                ('injuredcartid', models.TextField(blank=True, db_column='InjuredCartId', null=True)),
                ('number', models.IntegerField(blank=True, db_column='Number', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentParticipants',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipantsexes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('sex', models.TextField(blank=True, db_column='Sex', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentParticipantSexes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipanttypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentParticipantTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadmotionchanges',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('roadmotionchange', models.TextField(blank=True, db_column='RoadMotionChange', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentRoadMotionChanges',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadtypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('roadtype', models.TextField(blank=True, db_column='RoadType', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentRoadTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidents',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('kartid', models.IntegerField(db_column='KartId')),
                ('datetime', models.DateTimeField(db_column='DateTime')),
                ('died', models.IntegerField(db_column='Died')),
                ('wounded', models.IntegerField(db_column='Wounded')),
                ('vehiclenumber', models.IntegerField(db_column='VehicleNumber')),
                ('participantnumber', models.IntegerField(db_column='ParticipantNumber')),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
                ('originalgeom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='OriginalGeom', null=True, srid=4326)),
            ],
            options={
                'db_table': 'RoadAccidents',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentschemaimagecodes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('schemaimagecode', models.TextField(blank=True, db_column='SchemaImageCode', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentSchemaImageCodes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidenttypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentudsnearobjects',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('udsnearobject', models.TextField(blank=True, db_column='UdsNearObject', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentUdsNearObjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentudsplaceobjects',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('udsobjectsplace', models.TextField(blank=True, db_column='UdsObjectsPlace', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentUdsPlaceObjects',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvalidations',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('onroad', models.BooleanField(blank=True, db_column='OnRoad', null=True)),
                ('isregionmatch', models.BooleanField(blank=True, db_column='IsRegionMatch', null=True)),
                ('isaccurate', models.BooleanField(blank=True, db_column='IsAccurate', null=True)),
                ('inwater', models.BooleanField(blank=True, db_column='InWater', null=True)),
                ('isvalid', models.BooleanField(blank=True, db_column='IsValid', null=True)),
                ('validpercent', models.IntegerField(blank=True, db_column='ValidPercent', null=True)),
                ('matchingregion', models.TextField(blank=True, db_column='MatchingRegion', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentValidations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehiclebrands',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('brand', models.TextField(blank=True, db_column='Brand', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleBrands',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicledrivetypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('drivetype', models.TextField(blank=True, db_column='DriveType', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleDriveTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehiclemodels',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('model', models.TextField(blank=True, db_column='Model', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleModels',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicleownershiptypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('ownershiptype', models.TextField(blank=True, db_column='OwnershipType', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleOwnershipTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicleownertypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('ownertype', models.TextField(blank=True, db_column='OwnerType', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleOwnerTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicleroadaccidentplacelivings',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('roadaccidentplaceliving', models.TextField(blank=True, db_column='RoadAccidentPlaceLiving', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleRoadAccidentPlaceLivings',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicles',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('number', models.IntegerField(blank=True, db_column='Number', null=True)),
                ('color', models.TextField(blank=True, db_column='Color', null=True)),
                ('manufactureyear', models.IntegerField(blank=True, db_column='ManufactureYear', null=True)),
                ('destruction', models.TextField(blank=True, db_column='Destruction', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicles',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicletechissues',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('techissue', models.TextField(blank=True, db_column='TechIssue', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleTechIssues',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentvehicletypes',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentVehicleTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentweatherconditions',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('weathercondition', models.TextField(blank=True, db_column='WeatherCondition', null=True)),
            ],
            options={
                'db_table': 'RoadAccidentWeatherConditions',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadgraphroadtypes',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('roadtype', models.TextField(blank=True, db_column='RoadType', null=True)),
            ],
            options={
                'db_table': 'RoadGraphRoadTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadgraphs',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
                ('maxspeed', models.IntegerField(db_column='MaxSpeed')),
                ('isbridge', models.BooleanField(db_column='IsBridge')),
                ('istunnel', models.BooleanField(db_column='IsTunnel')),
                ('isoneway', models.BooleanField(db_column='IsOneway')),
            ],
            options={
                'db_table': 'RoadGraphs',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Trafficviolations',
            fields=[
                ('id', models.AutoField(db_column='Id', primary_key=True, serialize=False)),
                ('violation', models.TextField(blank=True, db_column='Violation', null=True)),
            ],
            options={
                'db_table': 'TrafficViolations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waterzones',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
                ('name', models.TextField(blank=True, db_column='Name', null=True)),
            ],
            options={
                'db_table': 'WaterZones',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Waterzonetypes',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('type', models.TextField(blank=True, db_column='Type', null=True)),
            ],
            options={
                'db_table': 'WaterZoneTypes',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Yandexgeocodervalidations',
            fields=[
                ('id', models.UUIDField(db_column='Id', primary_key=True, serialize=False)),
                ('distancedifference', models.FloatField(blank=True, db_column='DistanceDifference', null=True)),
                ('addresstext', models.TextField(blank=True, db_column='AddressText', null=True)),
                ('addresstype', models.TextField(blank=True, db_column='AddressType', null=True)),
                ('geom', django.contrib.gis.db.models.fields.GeometryField(blank=True, db_column='Geom', null=True, srid=4326)),
            ],
            options={
                'db_table': 'YandexGeocoderValidations',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Admindivisionroadaccident',
            fields=[
                ('admindivisionsid', models.OneToOneField(db_column='AdminDivisionsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.admindivisions')),
            ],
            options={
                'db_table': 'AdminDivisionRoadAccident',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Associatedtrafficviolationroadaccidentparticipant',
            fields=[
                ('associatedtrafficviolationsid', models.OneToOneField(db_column='AssociatedTrafficViolationsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.associatedtrafficviolations')),
            ],
            options={
                'db_table': 'AssociatedTrafficViolationRoadAccidentParticipant',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentparticipanttrafficviolation',
            fields=[
                ('roadaccidentparticipantsid', models.OneToOneField(db_column='RoadAccidentParticipantsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentparticipants')),
            ],
            options={
                'db_table': 'RoadAccidentParticipantTrafficViolation',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadaccidentdrivingfactor',
            fields=[
                ('roadaccidentdrivingfactorsid', models.OneToOneField(db_column='RoadAccidentDrivingFactorsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentdrivingfactors')),
            ],
            options={
                'db_table': 'RoadAccidentRoadAccidentDrivingFactor',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadaccidentndu',
            fields=[
                ('roadaccidentndusid', models.OneToOneField(db_column='RoadAccidentNdusId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentndus')),
            ],
            options={
                'db_table': 'RoadAccidentRoadAccidentNdu',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadaccidentudsnearobject',
            fields=[
                ('roadaccidentudsnearobjectsid', models.OneToOneField(db_column='RoadAccidentUdsNearObjectsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentudsnearobjects')),
            ],
            options={
                'db_table': 'RoadAccidentRoadAccidentUdsNearObject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadaccidentudsplaceobject',
            fields=[
                ('roadaccidentudsplaceobjectsid', models.OneToOneField(db_column='RoadAccidentUdsPlaceObjectsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentudsplaceobjects')),
            ],
            options={
                'db_table': 'RoadAccidentRoadAccidentUdsPlaceObject',
                'managed': False,
            },
        ),
        migrations.CreateModel(
            name='Roadaccidentroadaccidentweathercondition',
            fields=[
                ('roadaccidentweatherconditionsid', models.OneToOneField(db_column='RoadAccidentWeatherConditionsId', on_delete=django.db.models.deletion.DO_NOTHING, primary_key=True, serialize=False, to='DTP_map.roadaccidentweatherconditions')),
            ],
            options={
                'db_table': 'RoadAccidentRoadAccidentWeatherCondition',
                'managed': False,
            },
        ),
    ]