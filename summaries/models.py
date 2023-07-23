from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=150, null=False)
    birth_date = models.DateField(null=False)

    def __str__(self):
        return self.author_name


class SummaryGender(models.Model):
    gender_name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.gender_name


class Summary(models.Model):
    title = models.CharField(max_length=150, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ForeignKey(SummaryGender, on_delete=models.CASCADE)
    text_content = models.TextField(null=False)

    def __str__(self):
        return self.title


class Phrase(models.Model):
    phrase = models.CharField(max_length=255, null=False, unique=True)
    translated_phrase = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.phrase
