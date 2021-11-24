from django.db import models

# Create your models here.

class Category (models.Model):
    name = models.CharField(max_length=200)
    image = models.URLField()

    def __str__(self):
        return self.name

class Todo (models.Model):
    title = models.CharField(max_length=200)
    details = models.CharField(max_length=200)
    has_been_done= models.BooleanField(default=False)
    date_creation= models.DateTimeField(auto_now_add = True)
    date_completion = models.DateField(auto_now= True)
    deadline_date = models.DateField(null= True)
    category= models.ForeignKey(Category, on_delete= models.CASCADE)

