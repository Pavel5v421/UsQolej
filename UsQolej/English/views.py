from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *
import os
from django.http import FileResponse, HttpResponseNotFound
from django.conf import settings




class EnHomeListView(ListView):
    template_name='index_en.html'


    def get(self,request):
        enaboutcollege=EnAboutCollege.objects.get()
        enprofessions=EnProfessions.objects.all()
        staffs=EnStaffs.objects.all()
        questions=EnQuestions.objects.all()
        contactus=EnContactUs.objects.get()
        context={
            'link':'Vardenis Badeyan State College',
            'enaboutcollege':enaboutcollege,
            'enprofessions':enprofessions,
            'staffs':staffs,
            'questions':questions,
            'contactus':contactus,
            


                }

        return render(request,self.template_name,context)
    
class EnProfDetail(DetailView):
    template_name='detail_en.html'

    def get(self,request,id):
        enprofessions=EnProfessions.objects.all()
        ensubprofessions=EnProfessions.objects.filter(pk=id)
        for i in ensubprofessions:
            k=str(i.name)

        context={
            'link':k,
            'enprofessions':enprofessions,
            'ensubprofessions':ensubprofessions,
                }
        
        return render(request,self.template_name,context)

class EnMijinListView(ListView):
    template_name='Mijin_en.html'


    def get(self,request):
        professions=EnProfessions.objects.all()

        context={
            'link':'professions',
            'professions':professions,
            
                }
        
        return render(request,self.template_name,context)
    
class DimordDetailView(DetailView):
    template_name='Dimord_en.html'

    def get(self,request):
        dimord=EnDimord.objects.get()

        context={
            'link':'Applicant',
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
    template_name='download_en.html'

    def get(self,request):
        pdfiles=EnPDFiles.objects.all()

        context={
            'link':'library',
            'pdfiles':pdfiles,

                }
        
        return render(request,self.template_name,context)