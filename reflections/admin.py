from django.contrib import admin
from .models import Question, Configuration, Reflection, Answer
# Register your models here.

admin.site.register(Question)
admin.site.register(Configuration)
admin.site.register(Reflection)
admin.site.register(Answer)
