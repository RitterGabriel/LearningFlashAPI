# Generated by Django 4.2.1 on 2023-05-14 22:16

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('decks', '0002_alter_flashcard_domain_level_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='flashcard',
            name='last_time_checked',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
