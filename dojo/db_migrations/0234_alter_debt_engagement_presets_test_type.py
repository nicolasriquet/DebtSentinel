# Generated by Django 4.1.11 on 2023-12-10 09:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0233_debt_item_impact_type'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt_engagement_presets',
            name='test_type',
            field=models.ManyToManyField(blank=True, default=None, to='dojo.debt_test_type'),
        ),
    ]
