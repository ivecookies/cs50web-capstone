# Generated by Django 5.0.6 on 2024-07-16 16:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('walk_the_dog', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='dog',
            name='picture',
            field=models.URLField(blank=True, max_length=500, null=True),
        ),
    ]