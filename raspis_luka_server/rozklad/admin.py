from django.contrib import admin
from django.utils.translation import ugettext_lazy as _
from .models import Transport, Zupynka


class TransportAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['name', 'type' ]}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('pk',)
    list_display = ('__str__', 'name')


admin.site.register(Transport, TransportAdmin)


class ZupynkaAdmin(admin.ModelAdmin):
    fieldsets = [
            (_('General information'), {'fields': ['name', 'place' ]}),
            (_('Active'), {'fields': ['active'], 'classes': ['collapse']}),
        ]
    readonly_fields = ('pk',)
    list_display = ('__str__', 'name')


admin.site.register(Zupynka, ZupynkaAdmin)
