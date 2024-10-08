# Generated by Django 4.2.1 on 2023-12-19 09:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0004_examstep1_examstep2_examstep3_delete_exam_and_more'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='examstep1',
            name='description',
        ),
        migrations.RemoveField(
            model_name='examstep1',
            name='exam_date',
        ),
        migrations.RemoveField(
            model_name='examstep1',
            name='exam_time',
        ),
        migrations.RemoveField(
            model_name='examstep1',
            name='name',
        ),
        migrations.RemoveField(
            model_name='examstep2',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='examstep2',
            name='passing_marks',
        ),
        migrations.RemoveField(
            model_name='examstep2',
            name='subject',
        ),
        migrations.RemoveField(
            model_name='examstep2',
            name='total_marks',
        ),
        migrations.RemoveField(
            model_name='examstep3',
            name='answer_key',
        ),
        migrations.RemoveField(
            model_name='examstep3',
            name='exam',
        ),
        migrations.RemoveField(
            model_name='examstep3',
            name='question_paper',
        ),
        migrations.AddField(
            model_name='examstep1',
            name='brochure_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='brochure_links',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='category',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='contact_number',
            field=models.CharField(blank=True, max_length=15, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='detailed_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='email',
            field=models.EmailField(blank=True, max_length=254, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='exam_frequency',
            field=models.CharField(blank=True, choices=[('Once a year', 'Once a year'), ('Twice a year', 'Twice a year')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='exam_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='exam_official_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='exams_who_can_refer',
            field=models.CharField(blank=True, choices=[('Exam 1', 'Exam 1'), ('Exam 2', 'Exam 2')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='fee',
            field=models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='keywords_meta_tags',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='logo',
            field=models.ImageField(blank=True, null=True, upload_to='exam/logos/'),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='other_links',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='payment_modes',
            field=models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Net Banking', 'Net Banking')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='registration_fees',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='registration_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='registration_website',
            field=models.URLField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='short_description',
            field=models.TextField(blank=True, max_length=200, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='states_applicable',
            field=models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Delhi', 'Delhi'), ('Lakshadweep', 'Lakshadweep'), ('Puducherry', 'Puducherry')], max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='examstep1',
            name='upload_brochure',
            field=models.FileField(blank=True, null=True, upload_to='exam/brochures/'),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='admit_card_release_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='exam_dates',
            field=models.DateField(blank=True, default=None, help_text='Click + button to add more exam dates', null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='news_category',
            field=models.CharField(blank=True, choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Medium Important', 'Medium Important'), ('Less Important', 'Less Important')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='news_post',
            field=models.TextField(blank=True, max_length=5000, null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='registration_end_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='registration_start_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep2',
            name='result_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='excel_file',
            field=models.FileField(blank=True, null=True, upload_to='exam_patterns/'),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_category',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_exam_ref',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_file',
            field=models.FileField(blank=True, null=True, upload_to='study_material/'),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_keywords',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='material_links',
            field=models.TextField(blank=True, help_text='Separated by comma', null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_degree_branch',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_duration',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_marking_scheme',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_medium',
            field=models.TextField(blank=True, help_text='Separated by comma', null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_questions',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_subjects_sections',
            field=models.TextField(blank=True, help_text='Separated by comma', null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_total_marks',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='pattern_type_of_questions',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_date',
            field=models.DateField(blank=True, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_description',
            field=models.TextField(blank=True, max_length=500, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_exam',
            field=models.CharField(blank=True, max_length=50, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_files',
            field=models.FileField(blank=True, null=True, upload_to='question_papers/'),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_links',
            field=models.TextField(blank=True, help_text='Separated by comma', null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], max_length=20, null=True),
        ),
        migrations.AddField(
            model_name='examstep3',
            name='question_paper_year',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
