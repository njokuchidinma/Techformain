# Generated by Django 3.2.4 on 2021-06-10 20:40

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('home', '0002_auto_20210610_0748'),
    ]

    operations = [
        migrations.RenameField(
            model_name='techform',
            old_name='username',
            new_name='name',
        ),
        migrations.RenameField(
            model_name='techform',
            old_name='profession',
            new_name='program',
        ),
        migrations.AddField(
            model_name='techform',
            name='country',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='techform',
            name='message',
            field=models.CharField(default='', max_length=500),
        ),
        migrations.AddField(
            model_name='techform',
            name='number',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AddField(
            model_name='techform',
            name='state',
            field=models.CharField(default='', max_length=200),
        ),
        migrations.AlterField(
            model_name='techform',
            name='location',
            field=models.CharField(default='', max_length=200),
        ),
    ]
