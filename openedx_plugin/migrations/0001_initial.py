# Generated by Django 2.2.25 on 2022-01-15 18:29

from django.db import migrations, models
import django.utils.timezone
import model_utils.fields


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="Configuration",
            fields=[
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "type",
                    models.CharField(
                        choices=[
                            ("dev", "Development"),
                            ("test", "Testing / QA"),
                            ("prod", "Production"),
                        ],
                        default="dev",
                        help_text="Type of Open edX environment in which this configuration will be used.",
                        max_length=24,
                        primary_key=True,
                        serialize=False,
                        unique=True,
                    ),
                ),
                (
                    "example_host",
                    models.URLField(
                        blank=True,
                        help_text="the URL pointing to some server.",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "abstract": False,
            },
        ),
        migrations.CreateModel(
            name="MarketingSites",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "English"),
                            ("en-uk", "English (United Kingdom)"),
                            ("en@lolcat", "LOLCAT English"),
                            ("en@pirate", "Pirate English"),
                            ("es-419", "Español (Latinoamérica)"),
                            ("es-ar", "Español (Argentina)"),
                            ("es-ec", "Español (Ecuador)"),
                            ("es-es", "Español (España)"),
                            ("es-mx", "Español (México)"),
                            ("es-pe", "Español (Perú)"),
                            ("pt-br", "Português (Brasil)"),
                            ("pt-pt", "Português (Portugal)"),
                            ("it-it", "Italiano (Italia)"),
                            ("fr", "Français"),
                        ],
                        help_text="A language code. Examples: en, en-US, es, es-419, es-MX",
                        max_length=20,
                    ),
                ),
                (
                    "province",
                    models.CharField(
                        blank=True,
                        help_text="A sub-region for the language code. Example: for language code en-US valid possibles include TX, FL, CA, DC, KY, etc.",
                        max_length=20,
                    ),
                ),
                (
                    "site_url",
                    models.URLField(
                        default="https://example.org",
                        help_text="URL for for anchor tag for this language. Example: https://example.org/contact/",
                    ),
                ),
            ],
            options={
                "unique_together": {("language", "province")},
            },
        ),
        migrations.CreateModel(
            name="Locale",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "created",
                    model_utils.fields.AutoCreatedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="created",
                    ),
                ),
                (
                    "modified",
                    model_utils.fields.AutoLastModifiedField(
                        default=django.utils.timezone.now,
                        editable=False,
                        verbose_name="modified",
                    ),
                ),
                (
                    "element_id",
                    models.CharField(
                        help_text="An html element id. Example: example-locale-contact",
                        max_length=255,
                    ),
                ),
                (
                    "language",
                    models.CharField(
                        choices=[
                            ("en", "English"),
                            ("es-419", "Español (Latinoamérica)"),
                            ("pt-pt", "Português (Portugal)"),
                        ],
                        help_text="A language code. Examples: en, en-US, es, es-419, es-MX",
                        max_length=20,
                    ),
                ),
                (
                    "url",
                    models.URLField(
                        help_text="URL for for anchor tag for this language. Example: https://example.org/contact/"
                    ),
                ),
                (
                    "value",
                    models.CharField(
                        help_text="The text value of this html element. Example: Contacto",
                        max_length=255,
                    ),
                ),
            ],
            options={
                "unique_together": {("element_id", "language")},
            },
        ),
    ]
