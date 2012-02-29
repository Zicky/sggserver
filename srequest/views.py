from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.mail import send_mail
from django.http import HttpRequest
from django.views.decorators.csrf import csrf_exempt, csrf_protect
import pdb

@csrf_exempt
def get_post(request):
    if request.method == 'POST':
        if request.POST.has_key('name'):
            name = request.POST['name']
        if request.POST.has_key('email'):
            email = request.POST['email']
        if request.POST.has_key('type'):
            request_type = request.POST['type']
        if request.POST.has_key('discript'):
            discription = request.POST['discript']
            toemail = ['monnand@gmail.com','sarah.huangzq@gmail.com']
            head = 'Hi,\nThis is a new service request from the SGG iphone app.\n'
            #send_mail('test', 'This is a test for forwarding mails', email,toemail)
            ret = send_mail('Service Request From APP',  head+'Request Type:\t'+request_type+'\n'+'Discription of the request:\t'+discription+'\n', email, toemail)
            if ret:
                return HttpResponse(name+'\n'+email+'\n'+request_type+'\n'+discription)
        else:
            return HttpResponseForbidden("Fail on sending Service Request.\r\n")

