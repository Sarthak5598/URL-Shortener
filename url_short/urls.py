
from django.contrib import admin
from django.urls import path
from .views import home,redirect_to_original,registration_page,login_page,logoutUser
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home,name='home'),
    path("register/",registration_page,name="registration"),
    path("login/",login_page,name="login"),
    path("logout/",logoutUser,name="logout"),
    path('<short_code>/', redirect_to_original, name='redirect'),
]