# Generated by Django 4.2.11 on 2024-04-24 17:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0009_rename_image_img_image1_img_title'),
    ]

    operations = [
        migrations.CreateModel(
            name='crew',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=200, null=True)),
                ('content', models.TextField(blank=True, max_length=5000, null=True)),
            ],
        ),
    ]
