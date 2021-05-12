from django.db import models
from django.forms import ModelForm

class Review(models.Model):
    title = models.CharField(max_length=64)
    user = models.ForeignKey(User, on_delete=models.CASCADE)
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
        fields = ['title', 'code', 'language', 'date']

