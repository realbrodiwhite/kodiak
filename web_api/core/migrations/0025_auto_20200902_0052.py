# Generated by Django 3.0.3 on 2020-09-02 00:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("core", "0024_auto_20200726_0316"),
    ]

    operations = [
        migrations.AddField(
            model_name="account",
            name="contact_emails",
            field=models.TextField(
                blank=True,
                help_text="emails to contact about Kodiak issues. This is in addition to billing email from Stripe.",
                max_length=2000,
            ),
        ),
        migrations.AddConstraint(
            model_name="account",
            constraint=models.CheckConstraint(
                check=models.Q(contact_emails__length__lt=2000),
                name="contact_emails_max_length_2000",
            ),
        ),
    ]
