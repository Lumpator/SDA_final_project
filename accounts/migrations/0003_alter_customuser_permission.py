# Generated by Django 4.1.1 on 2022-10-03 20:34

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0002_userpermissions_customuser_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='permission',
            field=models.ForeignKey(default=1, null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userpermissions'),
        ),
    ]
