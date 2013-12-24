from django.contrib import admin

# Register your models here.
from polls.models import Poll, Choice

class ChoiceInline(admin.StackedInline):
  model = Choice
  extra = 3

class PollAdmin(admin.ModelAdmin):
  fieldsets = [
      (None,  {'fields': ['question']}),
      ('Date information', {'fields': ['pub_data'], 'classes': ['collapse']}),
      ]
  inlines = [ChoiceInline]

  list_display = ('question', 'pub_data', 'was_published_recently')

admin.site.register(Poll, PollAdmin)
admin.site.register(Choice)
