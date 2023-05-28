from django.contrib import admin
from summaries.models import Summary, SummaryGender, Audio, Author


admin.site.register(Summary)
admin.site.register(SummaryGender)
admin.site.register(Audio)
admin.site.register(Author)
