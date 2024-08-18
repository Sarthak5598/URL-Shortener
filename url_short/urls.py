
from django.contrib import admin
from django.urls import path
from .views import home,redirect_to_original
urlpatterns = [
    path("admin/", admin.site.urls),
    path("", home,name='home'),
    path('<short_code>/', redirect_to_original, name='redirect'),
]