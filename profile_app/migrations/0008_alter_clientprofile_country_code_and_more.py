# Generated by Django 4.2.17 on 2024-12-30 07:29

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('profile_app', '0007_alter_captainprofile_country_code_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='clientprofile',
            name='country_code',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='CaptainProfile',
        ),
    ]
