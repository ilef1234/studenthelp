# Generated by Django 5.0.2 on 2024-05-09 22:46

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('Studenthelp', '0011_user_password_user_username_alter_reaction_comment_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='user',
            name='username',
        ),
    ]
