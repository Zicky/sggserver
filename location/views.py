# Create your views here.
from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from location.models import BinLocation
import json

def nearest_bin(self_lng, self_lat):
    loc_lng = sele_lng + 1
    loc_lat = self_lat + 1
    ret = json.dumps({'longitude': loc_lng, 'latitude': loc_lat})
    return HttpResponse(ret)

def test_def(request):
    return HttpResponseForbidden('First Step Succeed\r\n')

def bin_locs(request):
    loc = BinLocation.objects.all()
    ret = encode(loc)
    return HttpResponse(ret)

def encode(loc):
    json_list = []
    for each in loc:
        item = {'id':each.id, 'longitude':float(each.loc_lng), 'latitude':float(each.loc_lat), 'building':each.building, 'room':each.room}
        json_list.append(item)
    ret = json.dumps(json_list)
    return ret
