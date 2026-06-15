from django.shortcuts import render

from apps.course_delivery.models.module import Module


def module_list(request, course_id):

    modules = Module.objects.filter(course_id=course_id)

    return render(
        request,
        "course_delivery/partials/module_list.html",
        {"modules": modules},
    )
