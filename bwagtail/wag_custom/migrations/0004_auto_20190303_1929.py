# Generated by Django 2.1.5 on 2019-03-03 19:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('wag_custom', '0003_sitesettings_site_logo'),
    ]

    operations = [
        migrations.AddField(
            model_name='sitesettings',
            name='google_analytics_id',
            field=models.CharField(blank=True, help_text='Google Analytics Tracking ID', max_length=50, null=True),
        ),
        migrations.AlterField(
            model_name='footer',
            name='contact_type',
            field=models.CharField(choices=[('fas fa-phone', 'Phone'), ('fas fa-envelope', 'Email'), ('fab fa-facebook-f', 'Facebook'), ('fab-instagram', 'Instagram'), ('fab fa-linkedin', 'LinkedIn'), ('fab fa-twitter', 'Twitter'), ('fab fa-pinterest', 'Pinterest'), ('fab fa-youtube', 'Youtube'), ('fab fa-github', 'GitHub'), ('fab fa-gitlab', 'GitLab')], max_length=50),
        ),
    ]
