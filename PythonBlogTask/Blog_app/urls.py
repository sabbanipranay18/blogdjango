from django.contrib import admin
from django.urls import path, include
from . import views
from Blog_app.views import Listview, blogdetails, addblog, editblog, deleteblog, myblogs

from django.conf import settings
from django.conf.urls.static import static

urlpatterns = [
    # path('', views.home, name="home"),
    path('', Listview.as_view(), name="home"),
    path('blogdetails/<int:pk>', blogdetails.as_view(), name="blogdetails"),
    path('addblog/', addblog.as_view(), name="addblog"),
    path('editblog/<int:pk>', editblog.as_view(), name="editblog"),
    path('deleteblog/<int:pk>', deleteblog.as_view(), name="deleteblog"),
    path('myblogs/', myblogs.as_view(), name="myblogs"),
    
    path('signup', views.signup, name="signup"),
    path('signin', views.signin, name="signin"),
    path('signout', views.signout, name="signout"),
    path('search/', views.search, name="search"),
     
    
    
]+ static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)