# Generated by Django 5.0.2 on 2024-03-24 01:07

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studenthelp', '0003_alter_poste_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='poste',
            name='type',
            field=models.CharField(choices=[('offre', '0'), ('1', 'demande')], default='0', max_length=100),
        ),
    ]
