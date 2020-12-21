from django.db import models

# Create your models here.

 
SEMESTER_CHOICES = ( 
    ("SPR 21", "SPR 21"), 
    ("FA 21", "FA 21"), 
    ("SPR 22", "SPR 22"), 
    ("FA 22", "FA 22"), 
    ("SPR 23", "SPR 23"), 
    ("FA 23", "FA 23"), 
    ("SPR 24 ", "SPR 24"), 
    ("FA 24", "FA 24"), 
) 
# declaring a Student Model 



class Architectural_Science_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()


	def __str__ (self):
		return self.courseName

class Civil_Engineering_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()


	def __str__ (self):
		return self.courseName

class Computer_Information_Technology_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()


	def __str__ (self):
		return self.courseName

class Computer_Science_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

	def __str__ (self):
		return self.courseName

class Construction_Management_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

	def __str__ (self):
		return self.courseName


class Electrical_Engineering_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

class Engineering_Technology_Management_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

	def __str__ (self):
		return self.courseName


class Manufacturing_Engineering_Technology_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

	def __str__ (self):
		return self.courseName


class Mechanical_Engineering_Courses_Offered(models.Model):

	courseName = models.CharField(max_length=250)

	semester = models.CharField( 
        max_length = 20, 
        choices = SEMESTER_CHOICES, 
        default = 'SPR 21'
        )

	preRequisites = models.TextField()

	def __str__ (self):
		return self.courseName

