from django.db import models
from django.utils import timezone


class Project(models.Model):
    title = models.CharField(max_length=10)
    icon = models.TextField()
    summary = models.TextField()
    description = models.TextField()
    link = models.URLField()
    tag = models.TextField()

    def __str__(self):
        return self.title



class PersonalInfo(models.Model):
    
    surname = models.CharField(max_length=25)
    firstname = models.CharField(max_length=25)
    date_of_birth = models.DateField()
    job_title = models.TextField()
    address = models.TextField()
    phone_number = models.IntegerField()
    email = models.EmailField()
    summary = models.TextField()
    intro_url = models.URLField()

    def full_name(self):
        return "%(firstname)s %(surname)s" %({'firstname' : self.firstname, 'surname' : self.surname })

    def __str__(self):
        return self.full_name()



class Language(models.Model):
    
    name = models.CharField(max_length=25)
    level = models.CharField(max_length=25)
    start_date = models.DateField()
    description = models.TextField()

    def __str__(self):
        return self.name



class Interest(models.Model):
    
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name



class Membership(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name


class Job(models.Model):
    title = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    company = models.CharField(max_length=25)
    summary = models.TextField()
    description = models.TextField()
    image = models.URLField()
    link = models.URLField()

    def __str__(self):
        return self.title


class Education(models.Model):
    name = models.CharField(max_length=25)
    start_date = models.DateField()
    end_date = models.DateField()
    is_current = models.BooleanField(default=False)
    school = models.CharField(max_length=25)
    summary = models.TextField()
    description = models.TextField()
    image = models.URLField()
    link = models.URLField()


    def __str__(self):
        return self.name


class Skill(models.Model):
    name = models.CharField(max_length=25)
    description = models.TextField()
    image = models.URLField()

    def __str__(self):
        return self.name
