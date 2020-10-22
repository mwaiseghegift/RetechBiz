# Generated by Django 3.0.6 on 2020-10-21 16:33

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0005_auto_20201013_0657'),
    ]

    operations = [
        migrations.AlterField(
            model_name='manager',
            name='category',
            field=models.CharField(choices=[('CEO', 'Chief Executive Office'), ('PM', 'Production Manager'), ('CTO', 'CTO'), ('Acc', 'Accountant'), ('Member', 'Member'), ('Admin', 'Admin')], max_length=100),
        ),
        migrations.AlterField(
            model_name='profile',
            name='category',
            field=models.CharField(choices=[('CEO', 'Chief Executive Office'), ('PM', 'Production Manager'), ('CTO', 'CTO'), ('Acc', 'Accountant'), ('Member', 'Member'), ('Admin', 'Admin')], default='Member', max_length=50),
        ),
    ]
