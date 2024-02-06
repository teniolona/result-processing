from django.db import models

# Create your models here.

class Student(models.Model):
    matricno = models.CharField(max_length=10, primary_key=True)
    first_name = models.CharField(max_length=32, verbose_name="First Name")
    last_name = models.CharField(max_length=32, verbose_name="Last Name")
    level = models.IntegerField(null=True)
    college = models.CharField(max_length=100, null=True, blank=False)
    programme = models.CharField(max_length=100, null=True, blank=False)
    #profile = models.ImageField(upload_to="student/", null=True, verbose_name="Profile Picture")
    
    
    def __str__(self):
        return f"My name is {self.first_name} {self.last_name} with matric number {self.matricno}"

class CourseList(models.Model):
    coursecode = models.CharField(max_length = 16, verbose_name="Course Code")
    coursetitle = models.CharField(max_length = 64, verbose_name="Course Title")
    coursecredit = models.IntegerField()
    coursemark = models.IntegerField()
    # lettergrade = models.CharField(max_length=16, verbose_name="Letter Grade")
    gp = models.IntegerField()
    weightedgp = models.IntegerField()
    
    def __str__(self):
        return f"The Score you got in course {self.id}, {self.coursecode} is {self.coursemark}"

#Set the format for the LG and GP of the reult table.
    @property
    def lettergrade(self):
        if self.coursemark >= 70:
            return "A"
        elif 60 <= self.coursemark <= 69:
            return "B"
        elif 50 <= self.coursemark <= 59:
            return "C"
        elif 45 <= self.coursemark <= 49:
            return "D"
        elif 40 <= self.coursemark <= 44:
            return "E"
        elif self.coursemark <= 39:
            return "F"