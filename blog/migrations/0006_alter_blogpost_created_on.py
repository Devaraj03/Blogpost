# Generated by Django 4.2.11 on 2024-04-17 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_blogpost_content2'),
    ]

    operations = [
        migrations.AlterField(
            model_name='blogpost',
            name='created_on',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
