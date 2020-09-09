from django.shortcuts import render
from django.http import HttpResponseRedirect
from django.urls import reverse
from first_app.models import AccessRecord, Topic, Webpage, User
from . import forms
# Create your views here.

def index(request):
    webpage_list = AccessRecord.objects.order_by('date')
    date_dict = {'access_records': webpage_list}
    return render(request, 'first_app/index.html', context=date_dict)

def usr_view(request):
    sgnp_frm = forms.SignupForm()
    if request.method == "POST":
        sgnp_frm = forms.SignupForm(request.POST)
        if sgnp_frm.is_valid():
            sgnp_frm.save()
            return HttpResponseRedirect(reverse('index'))
    return render(request, 'first_app/users.html', {'form': sgnp_frm})