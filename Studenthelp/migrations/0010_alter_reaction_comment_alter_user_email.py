# Generated by Django 5.0.2 on 2024-04-28 21:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Studenthelp', '0009_alter_user_options_rename_img_poste_image'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reaction',
            name='comment',
            field=models.TextField(),
        ),
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(max_length=254),
        ),
    ]
