from django.conf.urls import url
from . import views
from django.conf.urls.static import static
from django.conf import settings
from django.conf.urls import include,url

urlpatterns = [

    url(r'^$', views.index,name='index'),
    url(r'^main/', views.main,name='main'),
    url(r'^main1/', views.main1,name='main1'),
    url(r'^main2/', views.main2,name='main2'),

    url(r'^H_req_for_managers/', views.H_req_for_managers, name='H_req_for_managers'),
    url(r'^Today_req_for_managers/', views.Today_req_for_managers, name='Today_req_for_managers'),

    url(r'^Request_to_Leave_V/', views.Request_to_Leave_V,name='Request_to_Leave_V'),
    url(r'^H_req_for_employees/', views.H_req_for_employees,name='H_req_for_employees'),
    url(r'^Today_req_for_employees/', views.Today_req_for_employees,name='Today_req_for_employees'),
   
    url(r'^(?P<id>[0-9a-f-]+)/Approved/$', views.Approve, name='Approve'),
    url(r'^(?P<id>[0-9a-f-]+)/Reject/$', views.Reject, name='Reject'),

    url(r'^Admision/', views.Request_to_Leave_V, name='Request_to_Leave_V'),

    url(r'^success/', views.success, name='success'),
    url(r'^addition_Forbidden/', views.addition_Forbidden, name='addition_Forbidden'),




    
# ===========================================================================================

# ==================================================================================================
# ==========================================================================================
#     
]
urlpatterns += static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
#(?P<pk>\d+)
