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
    json_list = []
    for each in mat:
        item = {'name':each.name, 'percentage':float(each.percent), 'changes':float(each.change), 'month':each.month, 'year':each.year}
        json_list.append(item)
    ret = json.dumps(json_list)
    return ret
