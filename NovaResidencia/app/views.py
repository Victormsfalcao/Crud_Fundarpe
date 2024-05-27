from django.shortcuts import render, redirect
from django.contrib import messages
from django.urls import reverse
from .forms import (
    CadastroUsuarioForm,
    LoginForm,
    TransacaoForm,
    ProcessoForm,
    ProjetoForm,
)
from .models import Projeto, Processo, CadastroUsuario, Transacao


def home(request, setor):
    projetos = Projeto.objects.all()
    usuarios = CadastroUsuario.objects.all()
    transacoes = Transacao.objects.all()
    processos = Processo.objects.all()
    return render(
        request,
        "index.html",
        {
            "projetos": projetos,
            "usuarios": usuarios,
            "transacoes": transacoes,
            "processos": processos,
            "setor" : setor
        },
    )


def form_login(request):
    if request.method == "POST":
        form = LoginForm(request.POST)
        if form.is_valid():
            email = form.cleaned_data.get("email")
            senha = form.cleaned_data.get("senha")
            try:
                usuario = CadastroUsuario.objects.get(email=email)
                if usuario.senha == senha:
                    return redirect(reverse('home', kwargs={'setor': usuario.setor}))
                else:
                    messages.error(request, "Senha incorreta")
            except CadastroUsuario.DoesNotExist:
                messages.error(request, "Usuário não encontrado")
    else:
        form = LoginForm()
    return render(request, "login.html", {"form": form})


def form_cadastro_usuario(request):
    if request.method == "POST":
        form = CadastroUsuarioForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = CadastroUsuarioForm()
    return render(request, "form_cadastro_usuario.html", {"form": form})


def form_transacao(request):
    if request.method == "POST":
        form = TransacaoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = TransacaoForm()
    return render(request, "form_transacao.html", {"form": form})


def form_projeto(request):
    if request.method == "POST":
        form = ProjetoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProjetoForm()
    return render(request, "form_projeto.html", {"form": form})


def form_processo(request):
    if request.method == "POST":
        form = ProcessoForm(request.POST)
        if form.is_valid():
            form.save()
            return redirect("home")
    else:
        form = ProcessoForm()
    return render(request, "form_processo.html", {"form": form})
