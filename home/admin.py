from wagtail.contrib.modeladmin.options import ModelAdmin, modeladmin_register, ModelAdminGroup

from home.models import Activity, Inspiration, MentalHealthResource, HealthAssessment


class ActivityAdmin(ModelAdmin):
    model = Activity
    menu_label = "Activity"
    menu_icon = "tick-inverse"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    empty_value_display = 'N/A'
    search_fields = ("title",)


class InspirationAdmin(ModelAdmin):
    model = Inspiration
    menu_label = "Inspiration"
    menu_icon = "pick"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    empty_value_display = 'N/A'
    search_fields = ("title",)


class HealthAssessmentAdmin(ModelAdmin):
    model = HealthAssessment
    menu_label = "Health Assessment"
    menu_icon = "form"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    empty_value_display = 'N/A'
    search_fields = ("title",)


class MentalHealthResourceAdmin(ModelAdmin):
    model = MentalHealthResource
    menu_label = "Mental Health Resource"
    menu_icon = "plus"
    add_to_settings_menu = False
    exclude_from_explorer = False
    list_display = ("title",)
    empty_value_display = 'N/A'


modeladmin_register(ActivityAdmin)
modeladmin_register(InspirationAdmin)
modeladmin_register(HealthAssessmentAdmin)
modeladmin_register(MentalHealthResourceAdmin)
