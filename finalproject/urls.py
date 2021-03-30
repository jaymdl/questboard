"""finalproject URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.1/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls'))
"""
from django.contrib import admin
from django.urls import path
from questboard import views as qb_views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', qb_views.home_view, name='home'),
    path('signup/', qb_views.signup_view, name='signup'),
    path('login/', qb_views.login_view, name='login'),
    path('logout/', qb_views.logout_view, name='logout'),
    path('create_questboard/', qb_views.create_questboard, name='create_questboard'),
    path('questboard_detail/<str:pk>', qb_views.questboard_detail_view, name='questboard_detail'),
    path('create_quest/<str:pk>', qb_views.create_quest, name='create_quest'),
    path('add_member_one/<str:quest_pk>', qb_views.add_member_one, name='add_member_one'),
    path('add_member_two/<str:quest_pk>', qb_views.add_member_two, name='add_member_two'),
    path('add_member_three/<str:quest_pk>', qb_views.add_member_three, name='add_member_three'),
    path('update_questboard/<str:pk>', qb_views.update_questboard, name='update_questboard'),
    path('update_quest/<str:pk>', qb_views.update_quest, name='update_quest'),
    
]
