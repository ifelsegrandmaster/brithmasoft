# Generated by Django 3.1.2 on 2020-10-30 11:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('employment_agent', '0007_auto_20201030_1143'),
    ]

    operations = [
        migrations.AlterField(
            model_name='jobseeker',
            name='email_address',
            field=models.EmailField(max_length=45),
        ),
    ]