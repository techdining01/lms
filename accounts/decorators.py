from django.contrib.auth.decorators import user_passes_test


def student_required():

    return user_passes_test(lambda u: u.role == "STUDENT")
