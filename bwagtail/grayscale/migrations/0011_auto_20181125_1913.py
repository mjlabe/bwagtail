# Generated by Django 2.1.3 on 2018-11-26 00:13

from django.db import migrations
import wagtail.core.blocks
import wagtail.core.fields
import wagtail.images.blocks


class Migration(migrations.Migration):

    dependencies = [
        ('grayscale', '0010_auto_20181125_1715'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grayscalepage',
            name='body',
            field=wagtail.core.fields.StreamField([('masthead', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('subheading', wagtail.core.blocks.RichTextBlock(required=False)), ('background_image', wagtail.images.blocks.ImageChooserBlock())])), ('about', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock()), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image_with_transparent_background', wagtail.images.blocks.ImageChooserBlock(required=False))])), ('featured', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())])), ('featured_multi_row', wagtail.core.blocks.StreamBlock([('featured_multi_row', wagtail.core.blocks.StreamBlock([('featured_row', wagtail.core.blocks.StructBlock([('heading', wagtail.core.blocks.CharBlock(required=False)), ('paragraph', wagtail.core.blocks.RichTextBlock(required=False)), ('image', wagtail.images.blocks.ImageChooserBlock())]))]))])), ('paragraph', wagtail.core.blocks.RichTextBlock()), ('image', wagtail.images.blocks.ImageChooserBlock())]),
        ),
    ]
