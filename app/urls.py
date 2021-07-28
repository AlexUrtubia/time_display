from django.urls import path
from . import views

urlpatterns = [
    #path('admin/', admin.site.urls),
    #path('', include('time_display_proj.urls')),
    path('', views.index),
]