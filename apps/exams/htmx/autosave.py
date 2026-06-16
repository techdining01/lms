from django.http import HttpResponse

from apps.exams.services.autosave import save_answer

def autosave_answer(
    request,
):

    save_answer(...)

    return HttpResponse("saved")