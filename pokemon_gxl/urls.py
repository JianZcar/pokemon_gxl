"""
URL configuration for pokemon_gxl project.

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/4.2/topics/http/urls/
Examples:
Function views
    1. Add an import:  from my_app import views
    2. Add a URL to urlpatterns:  path('', views.home, name='home')
Class-based views
    1. Add an import:  from other_app.views import Home
    2. Add a URL to urlpatterns:  path('', Home.as_view(), name='home')
Including another URLconf
    1. Import the include() function: from django.urls import include, path
    2. Add a URL to urlpatterns:  path('blog/', include('blog.urls')
"""
from django.contrib import admin
from django.urls import path
from cardquest.views import home_page_view, trainers_view, cards_view, collections_view, trainers_create_view
from django.conf import settings
from django.conf.urls.static import static
from cardquest.views import trainer_edit_view, trainer_delete_view
from cardquest import views


urlpatterns = [
    path('admin/', admin.site.urls),
    path('', home_page_view, name='home'),
    path('trainers/', trainers_view, name='trainers'),
    path('cards/', cards_view, name='cards'),
    path('collections/', collections_view, name='collections'),
    path('trainer_list/add', trainers_create_view, name='trainer_add'),
    path('trainer_list/<int:id>/edit', trainer_edit_view, name='trainer_edit'),
    path('trainer_list/<int:id>/delete', trainer_delete_view, name='trainer_delete'),
] + static(settings.STATIC_URL, document_root=settings.STATIC_ROOT)
