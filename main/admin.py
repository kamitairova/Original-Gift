from django.contrib import admin
from django.contrib.admin import AdminSite
from main.models import Card, Setting, Example, Offer, Calendar, Review, Manual
from django.contrib.auth.models import User, Group
from django.contrib.auth.admin import UserAdmin, GroupAdmin

class MyAdminSite(AdminSite):
    site_header = "кастом админ панель"
    site_title = "Панель управления"
    index_title = "Добро пожаловать"

    def get_app_list(self, request):
        app_list = super().get_app_list(request)

        # Пример сортировки моделей
        for app in app_list:
            if app['app_label'] == 'main':  # Укажите название вашего приложения
                app['models'].sort(key=lambda x: ['Setting', 'Card', 'Example', 'Offer', 'Calendar', 'Review', 'Manual'].index(x['object_name']))

        return app_list


my_admin_site = MyAdminSite(name='myadmin')


class SettingsAdmin(admin.ModelAdmin):
    fieldsets = (
        ("head", {
            'fields': (('title', 'title_image'), ('subtitle_1', 'subtitle_2'))
        }),
        ('titles', {
            'fields': (('cards','is_active_cards'), ('examples','is_active_examples'), ('offers','is_active_offers'), ('calendars','is_active_calendars'), ('reviews','is_active_reviews'), ('manual','is_active_manual'))
        }),
    )


class ExampleAdmin(admin.ModelAdmin):
    fieldsets = (
        ("first example", {
            'fields': ('is_active_1', 'number_1','image_1', 'title_1', 'text_1')
        }),
        ('second example', {
            'fields': ('is_active_2', 'number_2','image_2', 'title_2', 'text_2')
        }),
    )



class ManualAdmin(admin.ModelAdmin):
    fieldsets = (
        ("calendar image", {
            'fields': ('calendar',)
        }),
        ('texts', {
            'fields': (("title_1","text_1",), ('title_2','text_2',), ('title_3', 'text_3'))
        }),
        ('description', {
            'fields': (('ico_1', 'name_1', 'description_1',), ('ico_2', 'name_2', 'description_2'),('ico_3', 'name_3', 'description_3'))
        })
    )


my_admin_site.register(Card)
my_admin_site.register(Setting, SettingsAdmin)
my_admin_site.register(Example, ExampleAdmin)
my_admin_site.register(Offer)
my_admin_site.register(Calendar)
my_admin_site.register(Review)
my_admin_site.register(Manual, ManualAdmin)

my_admin_site.register(User, UserAdmin)
my_admin_site.register(Group, GroupAdmin)




