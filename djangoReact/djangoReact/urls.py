from django.contrib import admin
from django.urls import path, include
from mainApp.views import index
from mainApp.views import category_detail
from mainApp.views import post_detail



urlpatterns = [
    path('admin/', admin.site.urls),
    path('', index),
    path('category/<int:id>', category_detail),
    path('post/<int:id>', post_detail),
    path('api/', include('mainApp.api.urls'))
]
