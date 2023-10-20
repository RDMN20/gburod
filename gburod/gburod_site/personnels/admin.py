from django.contrib import admin

from .models import (
    Persona,
    Seat,
    Speciality,
    Biography,
    Department,
    AcademicDegree,
    Rating,
    Comment,
)


admin.site.register(Persona)
admin.site.register(Seat)
admin.site.register(Speciality)
admin.site.register(Biography)
admin.site.register(Department)
admin.site.register(AcademicDegree)
admin.site.register(Rating)
admin.site.register(Comment)
