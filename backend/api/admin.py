from django.contrib import admin

from api.models import UserProfile, Model, Criterion, Option, PairsOfOptions, Value

admin.site.register(UserProfile)
admin.site.register(Model)
admin.site.register(Criterion)
admin.site.register(Option)
admin.site.register(PairsOfOptions)
admin.site.register(Value)