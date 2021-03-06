# Generated by Django 2.1.1 on 2018-09-11 12:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('learning', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Menu',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=32)),
                ('url_name', models.CharField(max_length=64)),
            ],
        ),
        migrations.AlterField(
            model_name='customer',
            name='tags',
            field=models.ManyToManyField(blank=True, to='learning.Tag'),
        ),
        migrations.AlterField(
            model_name='userprofile',
            name='roles',
            field=models.ManyToManyField(blank=True, to='learning.Role'),
        ),
        migrations.AddField(
            model_name='role',
            name='menus',
            field=models.ManyToManyField(blank=True, to='learning.Menu'),
        ),
    ]
