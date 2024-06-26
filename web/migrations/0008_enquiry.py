# Generated by Django 5.0.6 on 2024-05-14 08:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0007_blog_description"),
    ]

    operations = [
        migrations.CreateModel(
            name="Enquiry",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=250)),
                ("email", models.EmailField(max_length=254)),
                ("address", models.CharField(max_length=250)),
                ("phone_number", models.CharField(max_length=20)),
                (
                    "qualification",
                    models.CharField(
                        choices=[
                            ("10th", "10th"),
                            ("12th", "12th"),
                            ("Degree", "Degree"),
                            ("Diploma/ITI", "Diploma/ITI"),
                        ],
                        max_length=20,
                    ),
                ),
            ],
        ),
    ]
