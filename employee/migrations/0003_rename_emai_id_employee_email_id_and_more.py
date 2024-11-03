# Generated by Django 5.1.2 on 2024-11-01 08:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employee', '0002_rename_emoloyee_employee'),
    ]

    operations = [
        migrations.RenameField(
            model_name='employee',
            old_name='emai_id',
            new_name='email_id',
        ),
        migrations.AlterField(
            model_name='employee',
            name='gender',
            field=models.CharField(choices=[('female', 'female'), ('male', 'male')], default='male', max_length=200),
        ),
    ]