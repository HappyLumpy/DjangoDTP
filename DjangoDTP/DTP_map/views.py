from django.db.models import Q
from django.shortcuts import render
import yandex_geocoder
from decouple import config
from django.contrib.gis.geos import Point
from django.contrib.gis.measure import Distance
from django.shortcuts import render
from yandex_geocoder import Client

from DTP_map.models import Roadaccidents, Roadaccidentlocations, Roadaccidenttypes
from .forms import DTPForm


def mapbox_map(request):
    regions_list = ["Выберите регион"]
    years_list = ["Быберите год"]
    center = [94.298231, 66.3858021]
    zoom = 3
    regions = Roadaccidentlocations.objects.distinct('region')
    years = Roadaccidents.objects.dates('datetime', 'year')
    geo_json = {
        "type": "FeatureCollection",
        "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
        "features": None
    }
    for region in regions:
        regions_list.append(region.region)
    for year in years:
        years_list.append(year.year)
    if request.method == 'GET':
        return render(request, 'DTP_map/mapbox.html',
                      {'geo_json': geo_json,
                       'regions': regions_list, 'years': years_list, 'center': center, 'zoom': zoom})
    else:
        form = DTPForm(request.POST)
        region = form.data['region']
        year = form.data['year']
        died = form.data['died']
        zoom = 7
        if region == "Выберите регион" or year == "Быберите год":
            return render(request, 'DTP_map/mapbox.html',
                          {'geo_json': geo_json,
                           'regions': regions_list, 'years': years_list, 'center': center, 'zoom': zoom})
        features = []
        if died == "died":
            road_accidents = Roadaccidents.objects.filter(
                datetime__year=year,
                died__gt=0,
                roadaccidentlocations__region=region,
                roadaccidentvalidations__isvalid=True)
        else:
            road_accidents = Roadaccidents.objects.filter(
                datetime__year=year,
                roadaccidentlocations__region=region,
                roadaccidentvalidations__isvalid=True)
        if len(road_accidents) == 0:
            return render(request, 'DTP_map/mapbox.html',
                          {'geo_json': geo_json,
                           'regions': regions_list, 'years': years_list, 'center': center, 'zoom': zoom})
        for road_accident in road_accidents:
            road_accident_type = road_accident.roadaccidenttypeid.type
            if road_accident.roadaccidentroadtypeid:
                road_accident_road_type = road_accident.roadaccidentroadtypeid.roadtype
            else:
                road_accident_road_type = "Нет значения"
            died = road_accident.died
            wounded = road_accident.wounded
            road_accident_carriageway_condition = road_accident.roadaccidentcarriagewayconditionid.conditioncarriageway
            road_accident_lightning = road_accident.roadaccidentlightningid.lighting
            data = {"type": "Feature",
                    "properties": {"id": str(road_accident.id),
                                   "type": road_accident_type,
                                   "road_type": road_accident_road_type,
                                   "died": died,
                                   "wounded": wounded,
                                   "carriageway_condition": road_accident_carriageway_condition,
                                   "lightning": road_accident_lightning},
                    "geometry": {"type": "Point",
                                 "coordinates": [road_accident.geom.x, road_accident.geom.y, 0.0]}}
            features.append(data)
        center = [road_accident.geom.x, road_accident.geom.y]
        geo_json = {
            "type": "FeatureCollection",
            "crs": {"type": "name", "properties": {"name": "urn:ogc:def:crs:OGC:1.3:CRS84"}},
            "features": features
        }
        return render(request, 'DTP_map/mapbox.html',
                      {'geo_json': geo_json,
                       'regions': regions_list, 'years': years_list, 'center': center, 'zoom': zoom})
