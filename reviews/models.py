from django.db import models

class Review(models.Model):
    title = models.CharField(max_length=64)
    author = models.CharField(max_length=64)
    code = models.TextField()
    lang_type = models.CharField(
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