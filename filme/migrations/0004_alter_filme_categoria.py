# Generated by Django 5.2 on 2025-04-09 18:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('filme', '0003_rename_episodios_episodio'),
    ]

    operations = [
        migrations.AlterField(
            model_name='filme',
            name='categoria',
            field=models.CharField(choices=[('acao', 'Ação'), ('comedia', 'Comedia'), ('fantasia', 'Fantasia'), ('outros', 'Outros')], max_length=100),
        ),
    ]
