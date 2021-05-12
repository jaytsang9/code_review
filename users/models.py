from django.db import models
from django.forms import ModelForm

# Create your models here.
class User(models.Model):
    email = models.CharField(max_length=64)
    

class Review(models.Model):
    title = models.CharField(max_length=64)
    user = models.CharField(max_length=64)
    code = models.TextField()
    language = models.CharField(
        max_length = 12,
        choices=[
            ('Python', 'Python'),
            ('JavaScript', 'JavaScript'),
            ('PHP', 'PHP'),
            ('Java', 'Java'),
            ('C++', 'C++'),
            ('C', 'C'),
            ('SQL', 'SQL')
        ]
    )
    date = models.DateTimeField()

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'user', 'code', 'language', 'date']