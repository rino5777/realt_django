# Generated by Django 3.2 on 2022-09-29 01:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('advert', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='ads',
            name='rubric',
            field=models.CharField(choices=[('ПОКУПКА', 'покупка'), ('ПРОДАЖА', 'продажа')], default=0, max_length=20, verbose_name='Категория ( покупка\\продажа )'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='ads',
            name='contacts',
            field=models.CharField(max_length=100, verbose_name='Контакты'),
        ),
        migrations.AlterField(
            model_name='ads',
            name='description',
            field=models.TextField(verbose_name='Описание'),
        ),
    ]
