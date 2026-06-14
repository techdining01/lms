from django.contrib import admin

from .models.session import AcademicSession
from .models.term import Term
from .models.department import Department
from .models.school_class import SchoolClass
from .models.subject import Subject
from .models.class_subject import ClassSubject

admin.site.register(AcademicSession)
admin.site.register(Term)
admin.site.register(Department)
admin.site.register(SchoolClass)
admin.site.register(Subject)
admin.site.register(ClassSubject)