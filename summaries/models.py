from django.db import models


class Author(models.Model):
    author_name = models.CharField(max_length=150, null=False)
    borned_at = models.DateField(null=False)


class SummaryGender(models.Model):
    gender_name = models.CharField(max_length=120, null=False)


class Summary(models.Model):
    title = models.CharField(max_length=150, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ForeignKey(SummaryGender, on_delete=models.CASCADE)
    text_content = models.TextField(null=False)


class Audio(models.Model):
    audio_name = models.CharField(max_length=255, unique=True, null=False)
    audio_content = models.BinaryField()