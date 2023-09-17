from django.db import models
from users.models import Account


class Author(models.Model):
    author_name = models.CharField(max_length=150, null=False)
    birth_date = models.DateField(null=False)

    def __str__(self):
        return self.author_name

    class Meta:
        db_table = 'authors'


class SummaryGender(models.Model):
    gender_name = models.CharField(max_length=120, null=False)

    def __str__(self):
        return self.gender_name

    class Meta:
        db_table = 'summaries_genders'


class Summary(models.Model):
    title = models.CharField(max_length=150, null=False)
    author = models.ForeignKey(Author, on_delete=models.CASCADE)
    gender = models.ForeignKey(SummaryGender, on_delete=models.CASCADE)
    text_content = models.TextField(null=False)
    image = models.ImageField(upload_to='book-images', null=False)

    def __str__(self):
        return self.title

    class Meta:
        db_table = 'summaries'


class Phrase(models.Model):
    phrase = models.CharField(max_length=255, null=False, unique=True)
    translated_phrase = models.CharField(max_length=255, null=False)

    def __str__(self):
        return self.phrase

    class Meta:
        db_table = 'phrases'


class Favorite(models.Model):
    user = models.ForeignKey(to=Account, on_delete=models.CASCADE, null=False)
    summary = models.ForeignKey(to=Summary, on_delete=models.CASCADE, null=False)

    class Meta:
        db_table = 'favorites'
        unique_together = 'user', 'summary'
