# Generated by Django 5.0.6 on 2024-05-13 10:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Testimonial",
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
                ("position", models.CharField(max_length=250)),
                ("image", models.ImageField(upload_to="testimonial/")),
                ("description", models.TextField()),
                ("is_active", models.BooleanField(default=True)),
            ],
        ),
    ]
