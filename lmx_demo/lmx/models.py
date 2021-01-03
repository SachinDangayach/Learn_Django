from django.db import models

# Create your models here.
class Course(models.Model):
    courseTag = models.CharField(max_length=6)
    courseName = models.CharField(max_length=40)
    # CAT_NAMES = [('py','Python'),('dl','DNN/CV'),('nlp','NLP')]
    # categoryName = models.CharField(choices=CAT_NAMES, max_length=20)
    # PHASE_NAMES = [('p1','Phase 1'),('p2','Phase 2'),('p3','Phase 3')]
    # phaseName = models.CharField(choices=PHASE_NAMES, max_length=20)
    categoryName = models.CharField(max_length=10)
    phaseName = models.CharField(max_length=3)
    sessionCount = models.IntegerField()
    total_slots = models.IntegerField()
    available_slots = models.IntegerField()
    startDateTime = models.DateTimeField(auto_now_add=True)
    def __str__(self):
        return self.courseTag

class CourseStudentData(models.Model):
    firstName = models.CharField(max_length=20)
    lastName = models.CharField(max_length=20)
    course = models.ForeignKey(Course, on_delete=models.CASCADE)
