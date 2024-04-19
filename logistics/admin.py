from django.contrib import admin
from modeltranslation.admin import TranslationAdmin

from logistics.models import Category, Company, Contract


class CategoryAdmin(TranslationAdmin):
    list_display = ('title',)


class CompanyAdmin(TranslationAdmin):
    list_display = ('title',)


class ContractAdmin(TranslationAdmin):
    list_display = ('title',)


admin.site.register(Category, CategoryAdmin)
admin.site.register(Company, CompanyAdmin)
admin.site.register(Contract, ContractAdmin)
