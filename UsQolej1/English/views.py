from django.shortcuts import render
from django.views.generic import ListView,DetailView
from .models import *


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