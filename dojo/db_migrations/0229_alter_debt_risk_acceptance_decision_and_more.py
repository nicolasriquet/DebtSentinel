# Generated by Django 4.1.11 on 2023-12-04 16:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0228_alter_debt_risk_acceptance_accepted_by_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='decision',
            field=models.CharField(choices=[('A', 'Accept (The debt is acknowledged but remains, i.e., the risk is accepted)'), ('P', 'Pay (The debt is eliminated)'), ('M', 'Mitigate (The debt still exists but compensating actions make it less of a problem, i.e., less severe)'), ('T', 'Transfer (the debt payment or mitigation is transferred to a dedicated project or to a 3rd party)')], default='A', help_text='Risk treatment decision by risk owner', max_length=2),
        ),
        migrations.AlterField(
            model_name='debt_risk_acceptance',
            name='recommendation',
            field=models.CharField(choices=[('A', 'Accept (The debt is acknowledged but remains, i.e., the risk is accepted)'), ('P', 'Pay (The debt is eliminated)'), ('M', 'Mitigate (The debt still exists but compensating actions make it less of a problem, i.e., less severe)'), ('T', 'Transfer (the debt payment or mitigation is transferred to a dedicated project or to a 3rd party)')], default='P', help_text='Recommendation from the team.', max_length=2, verbose_name='Recommendation'),
        ),
    ]
