# Generated by Django 4.0.7 on 2022-11-19 22:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_customuser_favorite_fish_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='favorite_fish',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='customuser',
            name='favorite_phish_song',
            field=models.IntegerField(choices=[('1', 'Lushington'), ('2', 'You Enjoy Myself'), ('3', 'Divided Sky'), ('4', 'Tweezer'), ('5', 'Reba'), ('6', 'Harry Hood'), ('7', 'Fluffhead'), ('8', 'The Lizards'), ('9', 'Run Like an Antelope'), ('10', 'Farmhouse')], default='1'),
        ),
    ]
