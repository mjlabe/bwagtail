# Generated by Django 2.1.3 on 2018-12-03 01:31

from django.conf import settings
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('wagtailmenus', '0022_auto_20170913_2125'),
        ('wagtailcore', '0040_page_draft_title'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('wagtailforms', '0003_capitalizeverbose'),
        ('wagtailredirects', '0006_redirect_increase_max_length'),
        ('contenttypes', '0002_remove_content_type_name'),
        ('bootstrap_grayscale', '0001_initial'),
    ]

    operations = [
        migrations.RenameModel(
            old_name='GrayscalePage',
            new_name='BootstrapGrayscalePage',
        ),
    ]
