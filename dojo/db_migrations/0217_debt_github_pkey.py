# Generated by Django 4.1.11 on 2023-11-24 08:32

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('dojo', '0216_debt_cred_mapping'),
    ]

    operations = [
        migrations.CreateModel(
            name='Debt_GITHUB_PKey',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('git_project', models.CharField(blank=True, help_text='Specify your project location. (:user/:repo)', max_length=200, verbose_name='Github project')),
                ('git_push_notes', models.BooleanField(blank=True, default=False, help_text='Notes added to findings will be automatically added to the corresponding github issue')),
                ('debt_context', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='dojo.debt_context')),
                ('git_conf', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='dojo.github_conf', verbose_name='Github Configuration')),
            ],
        ),
    ]