# Generated by Django 4.2.14 on 2024-07-18 10:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_rename_birthdate_author_birth_date'),
    ]

    operations = [
        migrations.AlterField(
            model_name='author',
            name='birth_date',
            field=models.DateField(null=True),
        ),
    ]
