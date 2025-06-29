# Generated by Django 5.2.3 on 2025-06-23 21:02

import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='CallToAction',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(default='Fique por dentro das novidades!', help_text='Digite um título chamativo para a chamada de atenção.', max_length=255, verbose_name='Título')),
                ('description', models.TextField(default='Confira os últimos artigos e não perca as atualizações mais importantes.', help_text='Escreva um texto breve que descreva a chamada.', verbose_name='Descrição')),
                ('btn_texto', models.CharField(default='Ver Artigos →', help_text='Texto que aparecerá no botão de ação (ex: "Ver mais").', max_length=50, verbose_name='Texto do Botão')),
                ('btn_link', models.URLField(default='#blog', help_text='URL de destino ao clicar no botão.', verbose_name='Link do Botão')),
                ('image', models.ImageField(blank=True, help_text='Imagem opcional para ilustrar a chamada.', null=True, upload_to='cta_images/', verbose_name='Imagem')),
                ('active', models.BooleanField(default=True, help_text='Marque para exibir essa chamada no site.', verbose_name='Ativo')),
            ],
        ),
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='Nome da categoria do blog.', max_length=255, verbose_name='Nome')),
                ('description', models.TextField(blank=True, help_text='Descrição opcional sobre a categoria.', null=True, verbose_name='Descrição')),
            ],
            options={
                'verbose_name': 'Categoria',
                'verbose_name_plural': 'Categorias',
            },
        ),
        migrations.CreateModel(
            name='Blog',
            fields=[
                ('name', models.CharField(help_text='Título da postagem.', max_length=255, verbose_name='Título')),
                ('image', models.ImageField(blank=True, help_text='Imagem de capa da postagem.', null=True, upload_to='images/', verbose_name='Imagem')),
                ('short_description', models.CharField(blank=True, help_text='Resumo breve da postagem (aparece em listagens ou destaques).', max_length=2000, null=True, verbose_name='Descrição Curta')),
                ('description', models.TextField(blank=True, help_text='Conteúdo principal da postagem.', null=True, verbose_name='Descrição')),
                ('created', models.DateTimeField(auto_now_add=True, help_text='Data e hora em que a postagem foi criada.', verbose_name='Data de Criação')),
                ('star', models.BooleanField(default=False, help_text='Marque se esta postagem for um destaque ou recomendada.', verbose_name='Especial')),
                ('active', models.BooleanField(default=True, help_text='Marque para que a postagem apareça no site.', verbose_name='Ativo')),
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, help_text='Identificador único da postagem (não editável).', primary_key=True, serialize=False, unique=True, verbose_name='ID')),
                ('owner', models.ForeignKey(blank=True, help_text='Usuário responsável pela publicação.', null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL, verbose_name='Autor')),
                ('categories', models.ManyToManyField(blank=True, help_text='Selecione uma ou mais categorias para classificar a postagem.', to='blog.category', verbose_name='Categorias')),
            ],
            options={
                'verbose_name': 'Postagem',
                'verbose_name_plural': 'Postagens',
            },
        ),
    ]
