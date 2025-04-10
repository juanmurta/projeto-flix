from .models import Filme


def lista_filmes_recentes(request):
    lista_filmes = Filme.objects.all().order_by('-data_criacao')[0:8]
    return {"lista_filmes_recentes": lista_filmes}


def lista_filmes_emalta(request):
    lista_filmes = Filme.objects.all().order_by('-visualizacoes')[0:8]
    return {"lista_filmes_emalta": lista_filmes}


def filme_destaque(request):
    if Filme.objects.count() == 0:
        return {"filme_destaque": None}
    else:
        filme = Filme.objects.order_by('-data_criacao')[0]
        return {"filme_destaque": filme}
