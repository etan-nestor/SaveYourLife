from django.urls import path
from .views import Home,About,Contact,List, detailView, increment_shares



urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('events/',Contact,name='events'),
    path('blog/',List.as_view(),name='blog'),
    path('detail/<slug:slug>',detailView,name='detail'),
    path('increment_shares/<slug:slug>/', increment_shares, name='increment_shares')
]
