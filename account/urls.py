from django.urls import path
from . import views

urlpatterns = [
  path('register/', views.register , name='register'),
  path('login/', views.login_page , name='login'),
  path('editprofile/<int:id>/',views.editprofile ,name='editprofile'),
  path('profile/',views.profile ,name='profile'),
  path('change/<int:id>/',views.change ,name='change'),
  path('profiles/',views.profiles ,name='profiles'),
  path('logout/',views.logout_page ,name='logout'),
  path('createprofile/', views.createprofile , name='createprofile'),
  
]