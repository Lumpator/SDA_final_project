# Generated by Django 4.1.1 on 2022-10-12 21:24

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_permission'),
    ]

    operations = [
        migrations.AlterField(
            model_name='customuser',
            name='permission',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, to='accounts.userpermissions'),
        ),
    ]
