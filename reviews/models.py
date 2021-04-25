from django.db import models
from django.forms import ModelForm

class Review(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    code = models.TextField()
    language = models.CharField(
        max_length = 12,
        choices=[
            ('PY', 'Python'),
            ('JS', 'JavaScript'),
            ('PHP', 'PHP'),
            ('JAVA', 'Java'),
            ('CPP', 'C++'),
            ('C', 'C'),
            ('SQL', 'SQL')
        ]
    )
    date = models.DateField()

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'author', 'code', 'language', 'date']