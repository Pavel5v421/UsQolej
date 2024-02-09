from django.urls import path
from .views import *

urlpatterns=[
    path('',HomeListView.as_view(),name='home_hy'),
    path('professions/<int:id>/',ProfDetail.as_view(),name='detail_hy'),
    path('mijin_masnagitakan/',MijinListView.as_view(),name='mijin_hy'),
    path('dimord/',DimordDetailView.as_view(),name='dimord_hy'),
    
    
]