# Generated by Django 4.2.1 on 2023-12-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('coaching', '0011_alter_coachingstep1_days_of_operation'),
    ]

    operations = [
        migrations.RenameField(
            model_name='coachingstep3',
            old_name='total_students_in_coaching',
            new_name='total_students',
        ),
        migrations.RemoveField(
            model_name='coachingstep3',
            name='available_facilities',
        ),
        migrations.AddField(
            model_name='coachingstep3',
            name='available_facilities',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
    ]
