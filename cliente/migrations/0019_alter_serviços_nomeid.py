# Generated by Django 5.0.1 on 2024-02-15 22:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cliente', '0018_alter_serviços_nomeid'),
    ]

    operations = [
        migrations.AlterField(
            model_name='serviços',
            name='nomeID',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
