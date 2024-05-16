from django.db import models

class cadastroUsuario(models.Model):
    nome = models.CharField(max_length=100)
    email = models.EmailField(max_length=100)
    senha = models.CharField(max_length=10)
    setor = models.CharField(max_length=20)


class login(models.Model):
    usuarioId = models.ForeignKey(cadastroUsuario, on_delete=models.CASCADE)
    loginUsuario = models.CharField(max_length=100)


class transacao(models.Model):
    dataTransacao = models.DateTimeField()
    statusTransacao = models.CharField(max_length=100)
    userId = models.ForeignKey(login, on_delete=models.CASCADE)


class projeto(models.Model):
    numeroProjeto = models.CharField(max_length=30)
    numeroSei = models.CharField(max_length=21)
    numeroParcela = models.CharField(max_length=20)
    valorSolicitado =models.FloatField()
    tituloProjeto = models.CharField(max_length=100)
    statusTransacao = models.CharField(max_length=100)
    transacaoId = models.ForeignKey(transacao, on_delete=models.CASCADE)


class processo(models.Model):
    dataSolicitacao = models.DateTimeField()
    dataConferenciaDocumentos = models.DateTimeField()
    dataAutorizacaoEmpenho = models.DateTimeField()
    dataConfeccaoEmpenho = models.DateTimeField()
    numeroEmpenho = models.CharField(max_length=30)
    dataConfeccaoTermo = models.DateTimeField()
    dataEnvioTermo = models.DateTimeField()
    numeroTermo = models.CharField(max_length=30)
    responsavelConfeccao = models.CharField(max_length=100)
    dataVistoTermo = models.DateTimeField()
    dataEnvioTermProponente = models.DateTimeField()
    dataAssinaturaTermo = models.DateTimeField()
    dataEnvioPagamento = models.DateTimeField()
    dataOrdemBancaria = models.DateTimeField()
    statusTransacao = models.CharField(max_length=100)
    projetoId = models.ForeignKey(projeto, on_delete=models.CASCADE)