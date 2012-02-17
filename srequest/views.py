from django.http import HttpResponse, HttpResponseRedirect
from django.http import HttpResponseForbidden
from django.core.urlresolvers import reverse
from django.core.mail import send_mail

def get_post(request):
    if request.method == 'POST':
        name = request.POST['name']
        email = request.POST['email']
        request_type = request.POST['type']
        discription = request.POST['discript']
        toemail = ['monnand@gmail.com']
        head = 'Hi,\nThis is a new service request from the SGG iphone app.\n'
        send_mail('Service Request From APP',  head+'Request Type:\t'+request_type+'\n'+'Discription of the request:\t'+discription+'\n', email, toemail, fail_silently=False)
        return HttpResponse('Request has been successfully send.')
