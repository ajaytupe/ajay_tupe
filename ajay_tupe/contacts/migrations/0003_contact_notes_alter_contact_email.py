# Generated by Django 4.2.7 on 2023-11-29 03:03

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("contacts", "0002_remove_contact_description_remove_contact_is_done_and_more"),
    ]

    operations = [
        migrations.AddField(
            model_name="contact",
            name="notes",
            field=models.TextField(default="", max_length=200),
        ),
        migrations.AlterField(
            model_name="contact",
            name="email",
            field=models.EmailField(max_length=254),
        ),
    ]