from django.db import migrations


DEFAULT_SITE_CONTENT = {
    "hero_title": "Welcome to Recovery",
    "hero_subtitle": "Empowering journeys to wellness.",
    "our_story": "",
    "our_team_intro": "",
    "our_partners_intro": "",
    "mission_statement": "",
    "housing_support": "",
    "programs_intro": "",
    "contact_phone": "",
    "contact_email": "",
    "contact_address": "",
    "get_involved": "",
}


def seed_site_content(apps, schema_editor):
    SiteContent = apps.get_model("recoveryapi", "SiteContent")
    for key, default_value in DEFAULT_SITE_CONTENT.items():
        SiteContent.objects.get_or_create(
            content_type=key, defaults={"content": default_value}
        )


class Migration(migrations.Migration):

    dependencies = [
        ("recoveryapi", "0005_partner_teammember"),
    ]

    operations = [
        migrations.RunPython(
            seed_site_content, migrations.RunPython.noop
        ),
    ]
