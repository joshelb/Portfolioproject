from django.urls import path
from . import  views
from priceimpact.plotlygraphs import test
from priceimpact.scrapingmodule import orderimpact

urlpatterns=[
    #path('<char:symbol_id>/', views.trackerview, name = 'trackerview'),
    path('', views.mainview, name = 'mainview'),
    path('dataview/<str:symbol_id>/', views.dataview, name = 'dataview')
]



