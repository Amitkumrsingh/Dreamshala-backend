# Generated by Django 4.2.1 on 2023-12-26 08:13

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0014_alter_collegestep2_event_description'),
    ]

    operations = [
        migrations.AlterField(
            model_name='collegestep3',
            name='course',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep3',
            name='total_fees',
            field=models.TextField(blank=True, null=True),
        ),
    ]
