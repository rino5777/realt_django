# Generated by Django 3.2 on 2022-09-26 09:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_profile', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='email',
            field=models.EmailField(blank=True, default=0, max_length=254),
            preserve_default=False,
        ),
    ]
