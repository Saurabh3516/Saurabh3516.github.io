# Generated by Django 3.0.6 on 2021-06-18 09:21

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('ticketapp', '0002_remove_movie_promo'),
    ]

    operations = [
        migrations.AddField(
            model_name='movie',
            name='promo',
            field=models.URLField(default=1),
            preserve_default=False,
        ),
    ]
