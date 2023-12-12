from django.db import models

class Category(models.Model):
    name = models.CharField(max_length=255)

class State(models.Model):
    name = models.CharField(max_length=255)

class Course(models.Model):
    name = models.CharField(max_length=255)

class Degree(models.Model):
    name = models.CharField(max_length=255)

class College(models.Model):
    # ... other fields ...

    alumni_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='alumni_degrees')
    application_process_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='application_process_degrees')
    cutoffs_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='cutoffs_degrees')
    degree_offered = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='degrees_offered')
    faculties_background = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='faculties_backgrounds')
    placement_degree = models.ForeignKey(Degree, on_delete=models.CASCADE, related_name='placement_degrees')

    course = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='courses')
    faculties_specialisation = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='faculties_specialisations')
    reviews_course_taken = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='reviews_courses_taken')
    subject_wise_cutoffs_subject = models.ForeignKey(Course, on_delete=models.CASCADE, related_name='subject_wise_cutoffs_subjects')

    state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='states')
    locations_state = models.ForeignKey(State, on_delete=models.CASCADE, related_name='locations_states')

    news_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='news_categories')
    subject_wise_cutoffs_category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name='subject_wise_cutoffs_categories')

    # ... other fields ...

    class Meta:
        verbose_name_plural = "Colleges"

class Exam(models.Model):
    # ... other fields ...

    exams_who_can_refer = models.ManyToManyField('self', symmetrical=False)

    # ... other fields ...

    class Meta:
        verbose_name_plural = "Exams"
