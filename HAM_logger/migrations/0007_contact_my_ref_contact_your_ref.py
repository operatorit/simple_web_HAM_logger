# Generated by Django 5.1 on 2024-08-24 21:46

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("HAM_logger", "0006_rename_qso_no_contact_activity"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="my_ref",
            field=models.CharField(max_length=15, null=True),
        ),
        migrations.AddField(
            model_name="contact",
            name="your_ref",
            field=models.CharField(max_length=15, null=True),
        ),
    ]
