# Generated by Django 4.2.11 on 2024-04-19 05:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0008_rename_thumbnail_img_image'),
    ]

    operations = [
        migrations.RenameField(
            model_name='img',
            old_name='image',
            new_name='image1',
        ),
        migrations.AddField(
            model_name='img',
            name='title',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]
