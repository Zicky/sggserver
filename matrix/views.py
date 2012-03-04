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
        item = {'percentage':float(each.percent), \
                'changes':float(each.change), \
                'month':each.month, \
                'year':each.year}
        ret[each.name] = item
    ret = json.dumps(ret)
    return ret
