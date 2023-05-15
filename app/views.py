from django.shortcuts import render
# Create your views here.
from django.http import HttpResponse
from django.views.generic import TemplateView
from app.forms import *
class cbv_context(TemplateView):
    template_name='cbv_context.html'

    def get_context_data(self, **kwargs) :
        EDCO=super().get_context_data(**kwargs)
        
        EDCO['name']="mouni"
        EDCO['age']=21
        return EDCO

class cbv_form(TemplateView):
    template_name='cbv_form.html'
    def get_context_data(self,**kwargs):
        EDFO=super().get_context_data(**kwargs)
        FO=StudentForm()
        EDFO['FO']=FO
        return EDFO

    def post(self,request):
        SFD=StudentForm(request.POST)
        if SFD.is_valid():
            SFD.save()
            return HttpResponse('data is inserted successfully')

