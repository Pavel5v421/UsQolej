from django.urls import path
from .views import *

urlpatterns=[
    path('',EnHomeListView.as_view(),name='home_en'),
    path('Proffession_en/<int:id>/',EnProfDetail.as_view(),name='detail_en'),
    path('mijin_masnagitakan/',EnMijinListView.as_view(),name='mijin_en'),
    path('dimord/',DimordDetailView.as_view(),name='dimord_en'),

]