# Generated by Django 5.2.4 on 2025-07-14 02:04

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=200)),
                ('description', models.TextField()),
                ('image', models.ImageField(blank=True, null=True, upload_to='project_images/')),
                ('github_url', models.URLField(blank=True, null=True)),
                ('demo_url', models.URLField(blank=True, null=True)),
                ('tech_stack', models.CharField(blank=True, max_length=200, null=True)),
            ],
        ),
    ]
