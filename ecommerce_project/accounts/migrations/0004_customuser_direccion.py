# Generated by Django 5.1.3 on 2024-12-16 18:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_customuser_birth_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='customuser',
            name='direccion',
            field=models.TextField(blank=True, null=True),
        ),
    ]
