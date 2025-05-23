from django.shortcuts import render, redirect, reverse
from .models import Filme, Usuario
from .forms import CriarContaForm, FormHomepage
from django.views.generic import TemplateView, ListView, DetailView, FormView, UpdateView
from django.contrib.auth.mixins import LoginRequiredMixin


# Create your views here.

class Homepage(TemplateView):
    template_name = 'homepage.html'
    form_class = FormHomepage

    def get(self, request, *args, **kwargs):
        # se o usuario estiver logado, redireciona para a homefilmes
        if request.user.is_authenticated:
            # redireciona para a homefilmes
            return redirect('filme:homefilmes')
        else:
            # se o usuario não estiver logado, redireciona para a homepage
            return super().get(request, *args, **kwargs)

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        context["form"] = self.form_class()
        return context

    def post(self, request, *args, **kwargs):
        form = self.form_class(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get('email')
            usuarios = Usuario.objects.filter(email=email)
            if usuarios:
                return redirect('filme:login')
            else:
                return redirect('filme:criarconta')
        return render(request, self.template_name, {'form': form})

    def get_success_url(self):
        email = self.request.POST.get('email')
        usuarios = Usuario.objects.filter(email=email)
        if usuarios:
            return reverse('filme:login')
        else:
            return reverse('filme:criarconta')


class Homefilmes(LoginRequiredMixin, ListView):
    template_name = 'homefilmes.html'
    model = Filme
    # object_list -> lista de itens do modelo


class Detalhesfilme(LoginRequiredMixin, DetailView):
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
        # adicionar o filme na lista de filmes vistos do usuario
        usuario = request.user
        usuario.filmes_vistos.add(filme)
        return super().get(request, *args, **kwargs)  # redireciona o usuario para a url final

    def get_context_data(self, **kwargs):
        context = super(Detalhesfilme, self).get_context_data(**kwargs)
        # filtrar a minha tabela de filmes pegando a mesma categoria desses filmes
        filmes_relacionados = Filme.objects.filter(categoria=self.get_object().categoria)[0:5]
        context["filmes_relacionados"] = filmes_relacionados
        return context


class Pesquisafilme(LoginRequiredMixin, ListView):
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


class Paginaperfil(LoginRequiredMixin, UpdateView):
    template_name = 'editarperfil.html'
    model = Usuario
    fields = ['first_name', 'last_name', 'email']

    def get_success_url(self):
        return reverse('filme:homefilmes')


class Criarconta(FormView):
    template_name = 'criarconta.html'
    form_class = CriarContaForm

    def form_valid(self, form):
        # salva o usuario no banco de dados
        form.save()
        # redireciona para a pagina de login
        return super().form_valid(form)

    def get_success_url(self):
        return reverse('filme:login')





# criando view por meio de função, você gerencia tudo e faz manual
# def homepage(request):
#     return render(request, 'homepage.html')

# def homefilmes(request):
#     # Aqui você pode adicionar a lógica para buscar os filmes do banco de dados
#     # context = {} ou declare primeiro e depois passe a variavel ou faça diretamente
#     # lista_filmes = Filme.objects.all()
#     # context['lista_filmes'] = lista_filmes
#     return render(request, 'homefilmes.html', {'lista_filmes': Filme.objects.all()})
