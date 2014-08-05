from django.contrib import admin

# Register your models here.
from polls.models import Poll  # Poll class inside model.py under polls directory
from polls.models import Choice


#class ChoiceInline(admin.StackedInline):
class ChoiceInline(admin.TabularInline):
    model = Choice
    extra = 3


class PollAdmin(admin.ModelAdmin):
    # fieldsets = [
    #     (None, {'fields': ['question']}),
    #     ('Date information', {'fields': ['pub_date'], 'classes': ['collapse']}),
    # ]
    list_display = ('question', 'pub_date', 'was_published_recently')
    inlines = [ChoiceInline]
    list_filter = ['pub_date']
    search_fields = ['question']

admin.site.register(Poll, PollAdmin)
#admin.site.register(Choice)
