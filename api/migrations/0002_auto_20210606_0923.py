# Generated by Django 3.0.5 on 2021-06-06 09:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='user',
            options={'ordering': ('username',)},
        ),
        migrations.AddField(
            model_name='title',
            name='rating',
            field=models.FloatField(default=None, null=True),
        ),
    ]