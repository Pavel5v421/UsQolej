from django.shortcuts import redirect
from django.shortcuts import render
from .models import *
from django.views.generic import ListView,DetailView
from django.conf import settings
from django.http import FileResponse, HttpResponseNotFound
import os


class HomeListView(ListView):
    template_name='index.html'

    def get(self,request):
        aboutcollege=AboutCollege.objects.get()
        professions=Professions.objects.all()
        staffs=Staffs.objects.all()
        questions=Questions.objects.all()
        contactus=ContactUs.objects.get()

        context={
            'link':'Վարդենիսի Բադեյան Պետական Քոլեջ',
            'aboutcollege':aboutcollege,
            'professions':professions,
            'staffs':staffs,
            'questions':questions,
            'contactus':contactus,
            

                }

        return render(request,self.template_name,context)
    


class ProfDetail(DetailView):
    template_name='detail.html'

    def get(self,request,id):
        professions=Professions.objects.all()
        subprofessions=Professions.objects.filter(pk=id)
        for i in subprofessions:
            k=str(i.name)

        context={
            'link':k,
            'professions':professions,
            'subprofessions':subprofessions,

                }
        
        return render(request,self.template_name,context)
    

class MijinListView(ListView):
    template_name='Mijin.html'


    def get(self,request):
        professions=Professions.objects.all()

        context={
            'link':'Մասնագիտություններ',
            'professions':professions,

                }
        
        return render(request,self.template_name,context)
    
class DimordDetailView(DetailView):
    template_name='Dimord.html'

    def get(self,request):
        dimord=Dimord.objects.get()

        context={
            'link':'Դիմորդ',
            'dimord':dimord,

                }
        
        return render(request,self.template_name,context)
    

def download_pdf(request, filename):
    pdf_path = os.path.join(settings.MEDIA_ROOT, 'pdf', filename)
    if os.path.exists(pdf_path):
        with open(pdf_path, 'rb') as pdf_file:
            response = FileResponse(pdf_file, content_type='application/pdf')
            response['Content-Disposition'] = 'attachment; filename=' + filename
            return response
    else:
        return HttpResponseNotFound("The requested PDF was not found.")
    


class DownloadListView(ListView):
    template_name='download.html'

    def get(self,request):
        pdfiles=PDFiles.objects.all()

        context={
            'link':'Գրադարան',
            'pdfiles':pdfiles,

                }
        
        return render(request,self.template_name,context)


