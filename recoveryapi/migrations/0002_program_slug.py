from django.db import migrations, models
from django.utils.text import slugify


def populate_program_slugs(apps, schema_editor):
    Program = apps.get_model("recoveryapi", "Program")

    for program in Program.objects.all():
        base_slug = slugify(program.name) or f"program-{program.pk}"
        slug = base_slug
        index = 1

        while Program.objects.filter(slug=slug).exclude(pk=program.pk).exists():
            slug = f"{base_slug}-{index}"
            index += 1

        program.slug = slug
        program.save(update_fields=["slug"])


class Migration(migrations.Migration):

    dependencies = [
        ("recoveryapi", "0001_initial"),
    ]

    operations = [
        migrations.AddField(
            model_name="program",
            name="slug",
            field=models.SlugField(
                blank=True,
                null=True,
                max_length=120,
                help_text="URL-friendly slug used on the client application.",
            ),
        ),
        migrations.RunPython(
            populate_program_slugs,
            reverse_code=migrations.RunPython.noop,
        ),
        migrations.AlterField(
            model_name="program",
            name="slug",
            field=models.SlugField(
                max_length=120,
                unique=True,
                help_text="URL-friendly slug used on the client application.",
            ),
        ),
    ]
