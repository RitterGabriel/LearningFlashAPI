# Generated by Django 4.2.1 on 2023-09-17 23:36

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('summaries', '0006_alter_author_table_alter_favorite_table_and_more'),
    ]

    operations = [
        migrations.AlterModelTable(
            name='favorite',
            table='favorites',
        ),
        migrations.AlterModelTable(
            name='phrase',
            table='phrases',
        ),
        migrations.AlterModelTable(
            name='summary',
            table='summaries',
        ),
        migrations.AlterModelTable(
            name='summarygender',
            table='summaries_genders',
        ),
    ]
