# Generated by Django 4.2.2 on 2023-06-10 10:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('admin_panel', '0004_employee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='employee',
            name='email',
            field=models.EmailField(default='None@gmail.com', max_length=254),
        ),
    ]
