# Author: Ziqi Huang, huang.970@osu.edu
# Date: Mar 1st, 2012

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from zerow.models import Zerow
import json

def get_text(request):
    t = Zerow.objects.all()
    ret = encode(t)
    return HttpResponse(ret)

def encode(t):
    ret = {}
    i = 0
    for each in t:
        ret[i] = each.text
        i += 1
    ret = json.dumps(ret)

