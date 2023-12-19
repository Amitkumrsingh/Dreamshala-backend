# Generated by Django 4.2.1 on 2023-12-19 07:06

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('college', '0003_categorypercentile_entranceexam_location_otherlink_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Alumni',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
            ],
        ),
        migrations.CreateModel(
            name='Checklist',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('students_in_batch', models.CharField(blank=True, max_length=5, null=True)),
                ('total_students', models.CharField(blank=True, max_length=5, null=True)),
                ('number_of_faculty', models.CharField(blank=True, max_length=5, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='EntranceExamChoice',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('choice', models.CharField(choices=[('exam1', 'Exam 1'), ('exam2', 'Exam 2')], max_length=20, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name='Facility',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Faculty',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('specialisation', models.CharField(blank=True, choices=[('specialisation1', 'Specialisation 1'), ('specialisation2', 'Specialisation 2')], max_length=20, null=True)),
                ('background', models.CharField(blank=True, choices=[('background1', 'Background 1'), ('background2', 'Background 2')], max_length=20, null=True)),
                ('experience', models.CharField(blank=True, choices=[('experience1', 'Experience 1'), ('experience2', 'Experience 2')], max_length=20, null=True)),
                ('base_city', models.CharField(blank=True, choices=[('city1', 'City 1'), ('city2', 'City 2')], max_length=20, null=True)),
                ('faculty_links', models.TextField(blank=True, null=True)),
            ],
            options={
                'verbose_name_plural': 'Faculties',
            },
        ),
        migrations.CreateModel(
            name='FAQ',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('question', models.TextField(blank=True, null=True)),
                ('answer', models.TextField(blank=True, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Photo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(blank=True, null=True, upload_to='additional_details/photos/')),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('keywords', models.TextField(blank=True, max_length=200, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='PhotoCategory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Review',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(blank=True, max_length=10, null=True)),
                ('year_of_study', models.CharField(blank=True, choices=[('first_year', 'First Year'), ('second_year', 'Second Year'), ('third_year', 'Third Year'), ('fourth_year', 'Fourth Year')], max_length=20, null=True)),
                ('course_taken', models.CharField(blank=True, choices=[('course1', 'Course 1'), ('course2', 'Course 2')], max_length=20, null=True)),
                ('overall_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('academics_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('faculty_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('infrastructure_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('accommodation_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('placement_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('social_life_rating', models.IntegerField(blank=True, choices=[(1, '1'), (2, '2'), (3, '3'), (4, '4'), (5, '5')], null=True)),
                ('detailed_description', models.TextField(blank=True, max_length=500, null=True)),
                ('links', models.URLField(blank=True, null=True)),
                ('photo_video', models.FileField(blank=True, null=True, upload_to='additional_details/reviews/')),
            ],
        ),
        migrations.CreateModel(
            name='Video',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('upload_type', models.CharField(choices=[('link', 'Link'), ('video/mp4', 'Video (MP4)')], max_length=20)),
                ('link', models.URLField(blank=True, null=True)),
                ('video_file', models.FileField(blank=True, null=True, upload_to='additional_details/videos/')),
                ('description', models.TextField(blank=True, max_length=250, null=True)),
                ('keywords', models.TextField(blank=True, max_length=200, null=True)),
                ('thumbnail', models.ImageField(blank=True, null=True, upload_to='additional_details/videos/thumbnails/')),
            ],
        ),
        migrations.AlterModelOptions(
            name='collegestep2',
            options={'verbose_name_plural': 'CollegeStep2'},
        ),
        migrations.AlterModelOptions(
            name='collegestep4',
            options={'verbose_name_plural': 'People'},
        ),
        migrations.RenameField(
            model_name='collegestep2',
            old_name='application_process_description',
            new_name='important_news',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='application_process_degree_branch',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='batch_strength',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='category_percentile',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='course',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='course_description',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='course_duration',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='course_mode',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='cutoff_parameter',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='degree_offered',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='eligibility_criteria',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='eligibility_criteria_description',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='exams_through_admission',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='news',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='other_entrance_criteria',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='previous_cutoff_degree_branch',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='subject_wise_cutoff',
        ),
        migrations.RemoveField(
            model_name='collegestep2',
            name='total_fees',
        ),
        migrations.RemoveField(
            model_name='collegestep3',
            name='admission_criteria',
        ),
        migrations.RemoveField(
            model_name='collegestep3',
            name='courses_offered',
        ),
        migrations.RemoveField(
            model_name='collegestep3',
            name='facilities_provided',
        ),
        migrations.RemoveField(
            model_name='collegestep4',
            name='average_salary',
        ),
        migrations.RemoveField(
            model_name='collegestep4',
            name='notable_alumni',
        ),
        migrations.RemoveField(
            model_name='collegestep4',
            name='placement_percent',
        ),
        migrations.RemoveField(
            model_name='collegestep5',
            name='college_description',
        ),
        migrations.RemoveField(
            model_name='collegestep5',
            name='college_logo',
        ),
        migrations.AddField(
            model_name='categorypercentile',
            name='college',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college.collegestep3'),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='application_process_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='batch_strength',
            field=models.CharField(blank=True, choices=[('strength1', 'Strength 1'), ('strength2', 'Strength 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='course',
            field=models.CharField(blank=True, choices=[('course1', 'Course 1'), ('course2', 'Course 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='course_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='course_duration',
            field=models.CharField(blank=True, choices=[('duration1', 'Duration 1'), ('duration2', 'Duration 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='course_mode',
            field=models.CharField(blank=True, choices=[('mode1', 'Mode 1'), ('mode2', 'Mode 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='degree_branch_application_process',
            field=models.CharField(blank=True, choices=[('degree1', 'Degree 1'), ('degree2', 'Degree 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='degree_offered',
            field=models.CharField(blank=True, choices=[('degree1', 'Degree 1'), ('degree2', 'Degree 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='eligibility_criteria',
            field=models.CharField(blank=True, choices=[('eligibility1', 'Eligibility 1'), ('eligibility2', 'Eligibility 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='eligibility_criteria_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='other_criteria',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='total_fees',
            field=models.CharField(blank=True, choices=[('fees1', 'Fees 1'), ('fees2', 'Fees 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='degree',
            field=models.CharField(blank=True, choices=[('degree1', 'Degree 1'), ('degree2', 'Degree 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='experience',
            field=models.CharField(blank=True, choices=[('experience1', 'Experience 1'), ('experience2', 'Experience 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='latest_position_achievement',
            field=models.CharField(blank=True, choices=[('experience1', 'Experience 1'), ('experience2', 'Experience 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='links',
            field=models.TextField(blank=True, max_length=10, null=True),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='photo',
            field=models.ImageField(blank=True, null=True, upload_to='people_photos/'),
        ),
        migrations.AddField(
            model_name='collegestep4',
            name='year_of_graduation',
            field=models.CharField(blank=True, choices=[('year1', 'Year 1'), ('year2', 'Year 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='average_package',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='degree_branch',
            field=models.CharField(blank=True, choices=[('degree1', 'Degree 1'), ('degree2', 'Degree 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='highest_package',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='number_of_international_offers',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='number_of_offers',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='number_of_recruiters',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='overall_placement_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='collegestep5',
            name='to_recruiters',
            field=models.CharField(blank=True, choices=[('number1', 'Number 1'), ('number2', 'Number 2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='categorypercentile',
            name='category',
            field=models.CharField(blank=True, choices=[('category1', 'Category 1'), ('category2', 'Category 2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='categorypercentile',
            name='percentile',
            field=models.CharField(blank=True, max_length=5, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep2',
            name='date_description',
            field=models.CharField(blank=True, choices=[('description1', 'Description 1'), ('description2', 'Description 2')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='collegestep2',
            name='news_category',
            field=models.CharField(blank=True, choices=[('very_imp', 'Very Important'), ('imp', 'Important'), ('medium_imp', 'Medium Important'), ('less_imp', 'Less Important')], max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='otherlink',
            name='url',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='weekday',
            name='day',
            field=models.CharField(blank=True, choices=[('Monday', 'Monday'), ('Tuesday', 'Tuesday'), ('Wednesday', 'Wednesday'), ('Thursday', 'Thursday'), ('Friday', 'Friday'), ('Saturday', 'Saturday'), ('Sunday', 'Sunday')], max_length=10, null=True),
        ),
        migrations.DeleteModel(
            name='EntranceExam',
        ),
        migrations.DeleteModel(
            name='SubjectWiseCutoff',
        ),
        migrations.AddField(
            model_name='photo',
            name='category',
            field=models.ManyToManyField(to='college.photocategory'),
        ),
        migrations.AddField(
            model_name='faculty',
            name='person',
            field=models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='college.collegestep4'),
        ),
        migrations.AddField(
            model_name='checklist',
            name='available_facilities',
            field=models.ManyToManyField(to='college.facility'),
        ),
        migrations.AddField(
            model_name='alumni',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='college.collegestep4'),
        ),
        migrations.AddField(
            model_name='collegestep3',
            name='entrance_exams',
            field=models.ManyToManyField(blank=True, to='college.entranceexamchoice'),
        ),
    ]
