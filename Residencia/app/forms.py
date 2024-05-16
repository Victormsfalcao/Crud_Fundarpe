from django.forms import ModelForm
from app.models import cadastroUsuario, login, transacao, projeto, processo

class cadastroUsuarioForm(ModelForm):
    class Meta:
        model = cadastroUsuario
        fields = ['nome', 'email', 'senha', 'setor']

class loginForm(ModelForm):
    class Meta:
        model = login
        fields = ['usuarioId', 'loginUsuario']

class transacaoForm(ModelForm):
    class Meta:
        model = transacao
        fields = ['dataTransacao', 'statusTransacao', 'userId']

class projetoForm(ModelForm):
    class Meta:
        model = projeto
        fields = ['numeroProjeto', 'numeroSei', 'numeroParcela', 'valorSolicitado', 'tituloProjeto',
        'statusTransacao', 'transacaoId']

class processoForm(ModelForm):
    class Meta:
        model = processo
        fields = ['dataSolicitacao', 'dataConferenciaDocumentos', 'dataAutorizacaoEmpenho', 'dataConfeccaoEmpenho',
        'numeroEmpenho', 'dataConfeccaoTermo', 'dataEnvioTermo', 'numeroTermo', 'responsavelConfeccao', 'dataVistoTermo',
        'dataEnvioTermProponente', 'dataAssinaturaTermo', 'dataEnvioPagamento', 'dataOrdemBancaria',
        'statusTransacao', 'projetoId']