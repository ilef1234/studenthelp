# Generated by Django 5.0.2 on 2024-04-24 20:55

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Studenthelp', '0008_alter_poste_type_alter_stage_duree_and_more'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'verbose_name': 'Utilisateur', 'verbose_name_plural': 'Utilisateurs'},
        ),
        migrations.RenameField(
            model_name='poste',
            old_name='img',
            new_name='image',
        ),
    ]