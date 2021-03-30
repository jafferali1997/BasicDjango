from .views import index,UserInfoView, SignupForm,LoginForm,user_logout,special
from django.urls import path

urlpatterns = [
    path('', index,name='index'),
    path('user/', UserInfoView,name='user'),
    path('signup/', SignupForm,name='signup'),
    path('login/',LoginForm,name='login'),
    path('logout/',user_logout,name='logout'),
    path('special/',special,name='special'),
]
