"""animes URL Configuration

The `urlpatterns` list routes URLs to views. For more information please see:
    https://docs.djangoproject.com/en/2.2/topics/http/urls/
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
from api.views import *

urlpatterns = [
    path('admin/', admin.site.urls),
    path('index/', index, name='index'),
    path('autenticar/',do_login,name='login'),
    path('',do_logout,name='logout'),

    path('categoria/',listaCategorias,name='lista_de_categorias'),
    path('categoria/add',addCategorias,name='adicionar_categorias'),
    path('categoria/salvar',salvarCategorias,name='salvar_categorias'),
    path('categoria/editar/<int:id>/',editarCategorias,name='editar_categorias'),
    path('categoria/excluir/<int:id>/',excluirCategorias,name='excluir_categorias'),

    path('status/',listaStatus,name='lista_status'),
    path('status/add',adicionarStatus,name='adicionar_status'),
    path('status/salvar',salvarStatus,name='salvar_status'),
    path('status/editar/<int:id>/',editarStatus,name='editar_status'),
    path('status/excluir/<int:id>/',excluirStatus,name='excluir_status'),

    path('autor/',listaAutor,name='lista_autor'),
    path('autor/add',adicionarAutor,name='adicionar_autor'),
    path('autor/salvar',salvarAutor,name='salvar_autor'),
    path('autor/editar/<int:id>/',editarAutor,name='editar_autor'),
    path('autor/excluir/<int:id>/',excluirAutor,name='excluir_autor'),

    path('anime/',listaAnime,name='lista_anime'),
    path('anime/add',adicionarAnime,name='adicionar_anime'),
    path('anime/salvar',salvarAnime,name='salvar_anime'),
    path('anime/editar/<int:id>/',editarAnime,name='editar_anime'),
    path('anime/excluir/<int:id>/',excluirAnime,name='excluir_anime'),
]
