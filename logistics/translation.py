from modeltranslation.translator import translator, TranslationOptions

from logistics.models import Category, Company, Contract


class CategoryTranslationOptions(TranslationOptions):
    fields = ('title',)


class CompanyTranslationOptions(TranslationOptions):
    fields = ('title', 'address', "inn", "kpp", "okpo", "bank", "kor_shot", "bike")


class ContractTranslationOptions(TranslationOptions):
    fields = ('title',)


translator.register(Category, CategoryTranslationOptions)
translator.register(Company, CompanyTranslationOptions)
translator.register(Contract, ContractTranslationOptions)
