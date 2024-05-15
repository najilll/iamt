# Generated by Django 5.0.6 on 2024-05-13 11:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("web", "0002_course"),
    ]

    operations = [
        migrations.CreateModel(
            name="CourseDetail",
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
                ("first", models.CharField(blank=True, max_length=250, null=True)),
                ("second", models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
        migrations.CreateModel(
            name="CourseFeactures",
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
                ("title", models.CharField(blank=True, max_length=250, null=True)),
            ],
        ),
    ]