# -*- coding: utf-8 -*-
from __future__ import unicode_literals

from django.contrib import admin
from TestModel.models import Test,Contact,Tag

class TagInline(admin.TabularInline):
    model = Tag

class ContactAdmin(admin.ModelAdmin):
    list_display = ('name', 'age', 'email')  # list
    search_fields = ('name',)
    inlines = [TagInline]    # Inline
    # fields = ('name','email')
    fieldsets = (
        ['Main', {
            'fields': ('name', 'email'),
        }],
        ['Advance', {
            'classes': ('collapse',),  # CSS
            'fields': ('age',),
        }]
    )

admin.site.register(Contact, ContactAdmin)
admin.site.register([Test])
