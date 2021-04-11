"""breaking_bad URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/3.2/topics/http/urls/
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
from api.views import inicio, show_bb, show_bcs, show_episode, show_character

urlpatterns = [
    path('admin/', admin.site.urls),
    path('', inicio, name ='index'),
    path('episodes_bb<int:n>', show_bb, name='episodes_bb'),
    path('detail_episode<int:id>', show_episode, name='show_episode'),
    path('episodes_bcs<int:n>', show_bcs, name='episodes_bcs'),
    path('show_character<str:name>', show_character, name='show_character')
]
    # path('episodes_bcs/<int:id>', show_bcs, name='episodes_bcs'),