from django.shortcuts import render
from .models import Filme
from django.views.generic import TemplateView, ListView, DetailView


# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'


class Homefilmes(ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list -> lista de itens do modelo


class Detalhesfilme(DetailView):
    template_name = 'detalhesfilme.html'
    model = Filme
    # object -> 1 item do nosso modelo

    def get(self, request, *args, **kwargs):
        # descobrir o filme que ele esta acessando
        filme = self.get_object()
        # somar a visualizacao do filme
        filme.visualizacoes += 1
        # salvar o filme no banco de dados
        filme.save()

        return super().get(request, *args, **kwargs) # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando a mesma categoria desses filmes
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Pesquisafilme(ListView):
    template_name = 'pesquisa.html'
    model = Filme

    def get_queryset(self):
        termo_pesquisa = self.request.GET.get('query')
        if termo_pesquisa:
            # Se o termo de pesquisa não for vazio, filtra os filmes
            object_list = Filme.objects.filter(titulo__icontains=termo_pesquisa)
            return object_list
        else:
            # Caso contrário, não retorna filme
            return None


# criando view por meio de função, você gerencia tudo e faz manual
# def homepage(request):
#     return render(request, 'homepage.html')

# def homefilmes(request):
#     # Aqui você pode adicionar a lógica para buscar os filmes do banco de dados
#     # context = {} ou declare primeiro e depois passe a variavel ou faça diretamente
#     # lista_filmes = Filme.objects.all()
#     # context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', {'lista_filmes': Filme.objects.all()})
