# Generated by Django 5.1.5 on 2025-02-15 16:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('JOLPECAPP', '0003_ejecsmodel_delete_jolpec'),
    ]

    operations = [
        migrations.AlterField(
            model_name='ejecsmodel',
            name='logo',
            field=models.ImageField(blank=True, default='fallback.png', upload_to=''),
        ),
    ]
