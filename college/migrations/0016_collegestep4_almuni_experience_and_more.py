# Generated by Django 4.2.1 on 2023-12-26 08:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0015_alter_collegestep3_course_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='collegestep4',
            name='almuni_experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep4',
            name='background',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep4',
            name='base_city_faculty',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep4',
            name='experience',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep4',
            name='faculty_name',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep4',
            name='specialization',
            field=models.TextField(blank=True, null=True),
        ),
    ]
