# Generated by Django 4.2.1 on 2023-12-26 07:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('exam', '0008_alter_examstep1_exam_official_website_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='examstep1',
            name='brochure_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='category',
            field=models.CharField(blank=True, choices=[('General', 'General'), ('OBC', 'OBC'), ('SC', 'SC'), ('ST', 'ST')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='detailed_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='exam_frequency',
            field=models.CharField(blank=True, choices=[('Once a year', 'Once a year'), ('Twice a year', 'Twice a year')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='exam_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='exams_who_can_refer',
            field=models.CharField(blank=True, choices=[('Exam 1', 'Exam 1'), ('Exam 2', 'Exam 2')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='keywords_meta_tags',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='payment_modes',
            field=models.CharField(blank=True, choices=[('Credit Card', 'Credit Card'), ('Debit Card', 'Debit Card'), ('Net Banking', 'Net Banking')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='registration_fees',
            field=models.CharField(blank=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='registration_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='short_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep1',
            name='states_applicable',
            field=models.CharField(blank=True, choices=[('Andhra Pradesh', 'Andhra Pradesh'), ('Arunachal Pradesh', 'Arunachal Pradesh'), ('Assam', 'Assam'), ('Bihar', 'Bihar'), ('Chhattisgarh', 'Chhattisgarh'), ('Goa', 'Goa'), ('Gujarat', 'Gujarat'), ('Haryana', 'Haryana'), ('Himachal Pradesh', 'Himachal Pradesh'), ('Jharkhand', 'Jharkhand'), ('Karnataka', 'Karnataka'), ('Kerala', 'Kerala'), ('Madhya Pradesh', 'Madhya Pradesh'), ('Maharashtra', 'Maharashtra'), ('Manipur', 'Manipur'), ('Meghalaya', 'Meghalaya'), ('Mizoram', 'Mizoram'), ('Nagaland', 'Nagaland'), ('Odisha', 'Odisha'), ('Punjab', 'Punjab'), ('Rajasthan', 'Rajasthan'), ('Sikkim', 'Sikkim'), ('Tamil Nadu', 'Tamil Nadu'), ('Telangana', 'Telangana'), ('Tripura', 'Tripura'), ('Uttar Pradesh', 'Uttar Pradesh'), ('Uttarakhand', 'Uttarakhand'), ('West Bengal', 'West Bengal'), ('Andaman and Nicobar Islands', 'Andaman and Nicobar Islands'), ('Chandigarh', 'Chandigarh'), ('Dadra and Nagar Haveli and Daman and Diu', 'Dadra and Nagar Haveli and Daman and Diu'), ('Delhi', 'Delhi'), ('Lakshadweep', 'Lakshadweep'), ('Puducherry', 'Puducherry')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep2',
            name='news_category',
            field=models.CharField(blank=True, choices=[('Very Important', 'Very Important'), ('Important', 'Important'), ('Medium Important', 'Medium Important'), ('Less Important', 'Less Important')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep2',
            name='news_post',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='material_category',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='material_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='material_exam_ref',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_degree_branch',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_duration',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_marking_scheme',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_questions',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_total_marks',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='pattern_type_of_questions',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='question_paper_description',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='question_paper_exam',
            field=models.CharField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='question_paper_mode',
            field=models.CharField(blank=True, choices=[('Online', 'Online'), ('Offline', 'Offline')], null=True),
        ),
        migrations.AlterField(
            model_name='examstep3',
            name='question_paper_year',
            field=models.CharField(blank=True, null=True),
        ),
    ]
