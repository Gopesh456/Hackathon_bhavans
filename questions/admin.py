from django.contrib import admin
from .models import Questions, TotalPoints,answer,Messages

# Register your models here.
admin.site.register(Questions)
admin.site.register(answer)
admin.site.register(TotalPoints)
admin.site.register(Messages)