# Generated by Django 4.1.11 on 2023-11-28 11:11

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0219_remove_stub_debt_item_test_stub_debt_item_debt_test'),
    ]

    operations = [
        migrations.AddField(
            model_name='debt_item',
            name='attitude',
            field=models.CharField(default=1, help_text='The attitude that lead to the creation of this Debt Item (Prudent, Reckless).', max_length=200, verbose_name='Attitude'),
            preserve_default=False,
        ),
        migrations.AddField(
            model_name='debt_item',
            name='intentionality',
            field=models.CharField(default='', help_text='The level of intentionality of this Debt Item (Deliberate, Inadvertent).', max_length=200, verbose_name='Intentionality'),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='debt_item',
            name='debt_endpoints',
            field=models.ManyToManyField(blank=True, help_text='The hosts within the debt_context that are susceptible to this flaw. + The status of the debt_endpoint associated with this flaw (Vulnerable, Mitigated, ...).', through='dojo.Debt_Endpoint_Status', to='dojo.debt_endpoint', verbose_name='Debt Endpoints'),
        ),
        migrations.AlterField(
            model_name='debt_item',
            name='debt_test',
            field=models.ForeignKey(editable=False, help_text='The debt_test that is associated with this flaw.', on_delete=django.db.models.deletion.CASCADE, to='dojo.debt_test', verbose_name='Debt Test'),
        ),
    ]