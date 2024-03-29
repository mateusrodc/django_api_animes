from django.shortcuts import render,redirect
from .models import *
from django.contrib.auth.models import User
from django.contrib.auth import authenticate, login, logout
from django.contrib.auth.decorators import login_required

# Create your views here.
def do_login(request):
    if request.method == 'POST':
        user = authenticate(username=request.POST.get('usuario'), password=request.POST.get('senha'))
        if user is not None:
            login(request, user)
            return redirect('/index')
    return render(request, 'login.html')

def do_logout(request):
	logout(request)
	return render(request, 'login.html')

@login_required
def index(request):
    return render(request, 'index.html', context={})
@login_required
def listaCategorias(request):

    categoria= Categoria.objects.all()
    return render(request,'listaCategoria.html',context={'categoria':categoria})
@login_required
def addCategorias(request):

    return render(request,'adicionarCategoria.html',context=None)
@login_required
def editarCategorias(request,id):
    categoria= Categoria.objects.get(pk=id)
    return render(request,'adicionarCategoria.html',context={'categoria':categoria})
@login_required
def excluirCategorias(request,id):
    categoria= Categoria.objects.get(pk=id)
    categoria.delete()
    return redirect('/categoria')
@login_required
def salvarCategorias(request):

    nome_categoria= request.POST.get('nome_categoria')
    id_categoria = request.POST.get('id_categoria')

    if id_categoria:
        categoria= Categoria.objects.get(pk=id_categoria)
    else:
        categoria= Categoria()

    categoria.nome_categoria=nome_categoria
    categoria.save()
    return redirect('/categoria')
@login_required
def listaStatus(request):
    stats= Status.objects.all()
    return render(request,'listaStatus.html',context={'stats': stats})
@login_required
def adicionarStatus(request):
    return render(request,'adicionarStatus.html',context=None)
@login_required
def salvarStatus(request):
    situacao= request.POST.get('situacao')
    observacao= request.POST.get('observacao')
    id_stats= request.POST.get('id_stats')

    if id_stats:
        statss= Status.objects.get(pk=id_stats)
    else:
        statss= Status()

    statss.situacao=situacao
    statss.observacao=observacao
    statss.save()
    return redirect('/status')
@login_required
def editarStatus(request, id):
    stats= Status.objects.get(pk=id)
    return render(request,'adicionarStatus.html',context={'stats':stats})
@login_required
def excluirStatus(request,id):
    stats= Status.objects.get(pk=id)
    stats.delete()
    return redirect('/status')
@login_required
def listaAutor(request):

    autor= Autor.objects.all()
    return render(request,'listaAutor.html',context={'autor': autor})
@login_required
def adicionarAutor(request):

    return render(request,'adicionarAutor.html',context=None)
@login_required
def salvarAutor(request):

    nome= request.POST.get('nome')
    sobrenome= request.POST.get('sobrenome')
    idade= request.POST.get('idade')
    sexo= request.POST.get('sexo')
    cpf= request.POST.get('cpf')
    id_autor= request.POST.get('id_autor')
    if id_autor:
        autor= Autor.objects.get(pk=id_autor)
    else:
        autor= Autor()
    autor.nome=nome
    autor.sobrenome=sobrenome
    autor.idade=idade
    autor.sexo=sexo
    autor.cpf=cpf
    autor.save()
    return redirect('/autor')
@login_required
def editarAutor(request,id):
    autor= Autor.objects.get(pk=id)
    return render(request,'adicionarAutor.html',context={'autor':autor})
@login_required
def excluirAutor(request,id):
    autor= Autor.objects.get(pk=id)
    autor.delete()
    return redirect('/autor')
@login_required
def listaAnime(request):
    anime= Anime.objects.all()
    return render(request,'listaAnime.html',context={'anime':anime})
@login_required
def adicionarAnime(request):
    autores= Autor.objects.all()
    categorias= Categoria.objects.all()
    stats= Status.objects.all()

    context={
        'autores':autores,
        'categorias':categorias,
        'stats':stats
    }
    return render(request,'adicionarAnime.html',context)
@login_required
def editarAnime(request,id):
    anime= Anime.objects.get(pk=id)
    autores= Autor.objects.all()
    categorias= Categoria.objects.all()
    stats= Status.objects.all()

    context={
        'anime':anime,
        'autores':autores,
        'categorias':categorias,
        'stats':stats
    }

    return render(request,'adicionarAnime.html',context)
@login_required
def salvarAnime(request):
    nome= request.POST.get('nome')
    autor= request.POST.get('autor_anime')
    categoria = request.POST.get('categoria_anime')
    stats = request.POST.get('stats_anime')
    ano_lancamento= request.POST.get('ano_lancamento')
    qt_episodio= request.POST.get('qt_episodios')
    duracao_episodio= request.POST.get('duracao_episodio')
    sinopse= request.POST.get('sinopse')
    classificacao= request.POST.get('classificacao')
    id_anime= request.POST.get('id_anime')
    if id_anime:
        anime= Anime.objects.get(pk=id_anime)
    else:
        anime=Anime()

    anime.nome=nome
    anime.autor_id=autor
    anime.categoria_id=categoria
    anime.status_id=stats
    anime.ano_lancamento=ano_lancamento
    anime.qt_episodio=qt_episodio
    anime.duracao_episodio=duracao_episodio
    anime.sinopse=sinopse
    anime.classificacao=classificacao
    anime.save()
    return redirect('/anime')
@login_required
def excluirAnime(request,id):
    anime= Anime.objects.get(pk=id)
    anime.delete()
    return redirect('/anime')
