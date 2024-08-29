# Generated by Django 4.2.15 on 2024-08-29 17:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_user_managers_remove_user_pnone_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='userprofile',
            old_name='created',
            new_name='created_at',
        ),
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.PositiveSmallIntegerField(blank=True, choices=[(1, 'VENDOR'), (2, 'Customer')], null=True),
        ),
    ]