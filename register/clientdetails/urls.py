from django.urls import path
from .views import TestView,claim_here
app_name='claim_here'
urlpatterns=[
    path('api/postdetails/',TestView.as_view(),name='Details'),
    path('api/getdetails/',TestView.as_view(),name='GetDetails'),
    path('client/<int:client_id>/claim-here',claim_here,name='claim_here')
]