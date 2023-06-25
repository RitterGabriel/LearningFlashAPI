from django.contrib import admin
from .models import Summary, SummaryGender, Audio, Author, Phrase


admin.site.register(Summary)
admin.site.register(SummaryGender)
admin.site.register(Audio)
admin.site.register(Author)
admin.site.register(Phrase)