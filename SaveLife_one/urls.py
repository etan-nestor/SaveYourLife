from django.urls import path
from .views import Events, Home,About,Contact,List, News, Projects, Services, detailView, increment_shares



urlpatterns = [
    path('',Home,name='home'),
    path('about/',About,name='about'),
    path('contact/',Contact,name='contact'),
    path('events/',Events,name='events'),
    path('services/',Services,name='services'),
    path('projects/',Projects,name='projects'),
    path('news/',News,name='news'),
    path('blog/',List.as_view(),name='blog'),
    path('detail/<slug:slug>',detailView,name='detail'),
    path('increment_shares/<slug:slug>/', increment_shares, name='increment_shares')
]
