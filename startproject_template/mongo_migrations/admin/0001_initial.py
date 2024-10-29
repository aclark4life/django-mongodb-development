# Generated by Django 5.0.9 on 2024-10-04 20:15

import django.contrib.admin.models
import django.db.models.deletion
import django.utils.timezone
import django_mongodb.fields.auto
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):
    initial = True

    dependencies = [
        ("contenttypes", "0001_initial"),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name="LogEntry",
            fields=[
                (
                    "id",
                    django_mongodb.fields.auto.ObjectIdAutoField(
                        auto_created=True,
                        db_column="_id",
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "action_time",
                    models.DateTimeField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="action time",
                    ),
                ),
                (
                    "object_id",
                    models.TextField(blank=True, null=True, verbose_name="object id"),
                ),
                (
                    "object_repr",
                    models.CharField(max_length=200, verbose_name="object repr"),
                ),
                (
                    "action_flag",
                    models.PositiveSmallIntegerField(
                        choices=[(1, "Addition"), (2, "Change"), (3, "Deletion")],
                        verbose_name="action flag",
                    ),
                ),
                (
                    "change_message",
                    models.TextField(blank=True, verbose_name="change message"),
                ),
                (
                    "content_type",
                    models.ForeignKey(
                        blank=True,
                        null=True,
                        on_delete=django.db.models.deletion.SET_NULL,
                        to="contenttypes.contenttype",
                        verbose_name="content type",
                    ),
                ),
                (
                    "user",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to=settings.AUTH_USER_MODEL,
                        verbose_name="user",
                    ),
                ),
            ],
            options={
                "verbose_name": "log entry",
                "verbose_name_plural": "log entries",
                "db_table": "django_admin_log",
                "ordering": ["-action_time"],
            },
            managers=[
                ("objects", django.contrib.admin.models.LogEntryManager()),
            ],
        ),
    ]
