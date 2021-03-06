# Generated by Django 3.0.6 on 2021-06-20 20:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0005_auto_20210620_2304'),
    ]

    operations = [
        migrations.CreateModel(
            name='Userdata',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(max_length=50)),
                ('email', models.EmailField(max_length=254)),
                ('transaction', models.IntegerField(default=0)),
                ('choice', models.ManyToManyField(to='ticketapp.Movie')),
            ],
        ),
    ]
