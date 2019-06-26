from django.contrib import admin
from .models import Food, Festival, Event, EventCompletion, Contact, Planner, FoodReview, FestivalReview
from import_export.admin import ImportExportModelAdmin

admin.site.register(Food)

admin.site.register(Festival)

admin.site.register(Event)

admin.site.register(EventCompletion)

admin.site.register(Contact)

admin.site.register(Planner)

@admin.register(FoodReview)
class ViewAdmin(ImportExportModelAdmin):
	pass

admin.site.register(FestivalReview)
