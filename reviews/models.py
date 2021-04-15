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
    votes = models.IntegerField()
    date = models.DateField()
    def __str__(self):
            return self.get_language_display()

class ReviewForm(ModelForm):
    class Meta:
        model = Review
        fields = ['title', 'author', 'code', 'language', 'votes', 'date']