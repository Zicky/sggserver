# Author: Ziqi Huang, huang.970@osu.edu
# Date: Feb 29, 2012

from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from matrix.models import Matrix
import json

def get_matrix(request):
    mat = Matrix.objects.all()
    ret = encode(mat)
    return HttpResponse(ret)

def encode(mat):
    ret = {}
    for each in mat:
        if each.name == 'diversion':
            item = {'Percentage':float(each.percent), \
                'Changes':float(each.change), \
                'Month':each.month, \
                'Year':each.year}
        else:
            item = {'Amount':float(each.percent), \
                'Changes':float(each.change), \
                'Month':each.month, \
                'Year':each.year}
        ret[each.name] = item
    ret = json.dumps(ret)
    return ret
