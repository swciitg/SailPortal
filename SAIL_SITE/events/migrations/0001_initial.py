# Generated by Django 3.2.5 on 2021-07-24 18:08

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=50)),
                ('bg_image_id', models.CharField(blank=True, max_length=50)),
                ('yt_link', models.URLField(blank=True, max_length=300, null=True)),
                ('content', models.TextField()),
            ],
        ),
    ]
