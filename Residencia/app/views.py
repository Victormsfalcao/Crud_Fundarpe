from django.shortcuts import render, redirect
from app.forms import cadastroUsuarioForm, loginForm, transacaoForm, projetoForm, processoForm


# Create your views here.
def home(request):
    return render(request, 'index.html')

def form(request):
    data = {}
    data['form'] = projetoForm()
    return render(request, 'form.html', data)

def create(request):
    form = projetoForm(request.POST or None)
    if form.is_valid():
        form.save()
        return redirect('home')