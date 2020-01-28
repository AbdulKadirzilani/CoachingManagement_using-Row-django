from django.db import models


class StudentProfile(models.Model):
    name = models.CharField(max_length=50,unique=True)
    roll = models.CharField(max_length=50)
    birthday = models.CharField(max_length=50)
    fathers_name = models.CharField(max_length=50)
    address = models.CharField(max_length=50)

    gender_choice = (

        ('male', 'Male'),
        ('female', 'Female'),
        ('3rd gender', '3rd Gender')
    )
    gender = models.CharField(choices=gender_choice, max_length=6)

    session = models.CharField(max_length=50)
    #std_semester = models.CharField(max_length=50)
    mobile = models.IntegerField()
    email = models.EmailField()

    def __str__(self):
        return self.name  #foreignkey er karone .roll


