# Generated by Django 5.0.1 on 2024-02-02 13:23

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0002_remove_cliente_telefone_cliente_celular_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='cliente',
            old_name='Celular',
            new_name='celular',
        ),
        migrations.RenameField(
            model_name='serviços',
            old_name='Serviços',
            new_name='serviços',
        ),
    ]
