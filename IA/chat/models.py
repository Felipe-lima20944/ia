from django.db import models
import uuid
from django.conf import settings

# Se você for associar conversas a usuários, importe o modelo de usuário do Django
# from django.contrib.auth.models import User

class Conversa(models.Model):
    """
    Representa uma única conversa de chat.
    Inclui campos para metadados relevantes.
    """
    id = models.UUIDField(
        primary_key=True,
        default=uuid.uuid4,
        editable=False,
        help_text="Identificador único da conversa."
    )
    # Adicionamos um título para a conversa, que pode ser gerado automaticamente
    # ou definido pelo usuário.
    titulo = models.CharField(
        max_length=255,
        blank=True,
        default="Nova Conversa",
        help_text="Título da conversa para exibição na interface."
    )
    # Relaciona a conversa a um usuário, se o seu sistema tiver autenticação.
    # Usamos settings.AUTH_USER_MODEL para a melhor compatibilidade.
    # user = models.ForeignKey(
    #     settings.AUTH_USER_MODEL,
    #     on_delete=models.CASCADE,
    #     null=True,
    #     blank=True,
    #     related_name='conversas',
    #     help_text="O usuário proprietário desta conversa."
    # )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        help_text="Data e hora em que a conversa foi criada."
    )
    modificado_em = models.DateTimeField(
        auto_now=True,
        help_text="Data e hora da última atualização da conversa."
    )

    class Meta:
        verbose_name = "conversa"
        verbose_name_plural = "conversas"
        ordering = ['-modificado_em'] # Ordena as conversas pelas mais recentes

    def __str__(self):
        return self.titulo or f"Conversa {self.id}"

class Mensagem(models.Model):
    """
    Representa uma única mensagem dentro de uma conversa.
    Adicionamos um campo para metadados adicionais.
    """
    # Usamos os papéis 'user' e 'model' para manter a compatibilidade com a API.
    ROLES = [
        ('user', 'Usuário'),
        ('model', 'Modelo'),
    ]

    conversa = models.ForeignKey(
        Conversa,
        on_delete=models.CASCADE,
        related_name='mensagens',
        help_text="A conversa à qual esta mensagem pertence."
    )
    papel = models.CharField(
        max_length=10,
        choices=ROLES,
        help_text="O papel de quem enviou a mensagem (ex: 'user' ou 'model')."
    )
    texto = models.TextField(
        help_text="O conteúdo da mensagem."
    )
    criado_em = models.DateTimeField(
        auto_now_add=True,
        help_text="Data e hora em que a mensagem foi criada."
    )
    # Adicionamos um campo JSON para armazenar informações extra, como tokens usados,
    # feedback do usuário, ou qualquer outro dado não estruturado.
    metadados = models.JSONField(
        default=dict,
        blank=True,
        help_text="Metadados adicionais em formato JSON."
    )

    def __str__(self):
        # Apenas os primeiros 50 caracteres do texto para uma representação amigável.
        return f"{self.get_papel_display()}: {self.texto[:50]}"

    class Meta:
        verbose_name = "mensagem"
        verbose_name_plural = "mensagens"
        ordering = ['criado_em']