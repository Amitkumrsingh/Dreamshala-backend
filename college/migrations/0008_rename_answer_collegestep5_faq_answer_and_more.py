# Generated by Django 4.2.1 on 2023-12-22 06:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0007_rename_pan_card_number_collegestep1_college_pan_card_number_and_more'),
    ]

    operations = [
        migrations.RenameField(
            model_name='collegestep5',
            old_name='answer',
            new_name='faq_answer',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='question',
            new_name='faq_question',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='image',
            new_name='photo',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='category',
            new_name='photo_category',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='description',
            new_name='photo_description',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='keywords',
            new_name='photo_keywords_meta_tags',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='link',
            new_name='video_link',
        ),
        migrations.RenameField(
            model_name='collegestep5',
            old_name='thumbnail',
            new_name='video_thumbnail',
        ),
        migrations.RemoveField(
            model_name='collegestep5',
            name='upload_type',
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='excel_file',
            field=models.FileField(blank=True, null=True, upload_to='placement_details_exel/'),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='video_description',
            field=models.TextField(blank=True, max_length=250, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='video_keywords_meta_tags',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
    ]
