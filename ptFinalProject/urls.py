from django.contrib import admin
from django.urls import path, include
from users import views as users_views

urlpatterns = [
    path('admin/', admin.site.urls),
    path('registation/', users_views.register, name="registation"),
    path('', include('blog.urls')),
]
