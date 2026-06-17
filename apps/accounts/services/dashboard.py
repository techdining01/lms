from apps.accounts.models.user import User



class DashboardRouter:
    @staticmethod
    def get_dashboard(user):

        mapping = {
            "SUPER_ADMIN": "core:super-admin-dashboard",
            "ADMIN": "core:admin-dashboard",
            "TEACHER": "core:teacher-dashboard",
            "STUDENT": "core:student-dashboard",
            "PARENT": "core:parent-dashboard",
        }

        return mapping.get(user.role, "account_login")



def user_statistics():

    return {
        "students": User.objects.filter(role="STUDENT").count(),
        "teachers": User.objects.filter(role="TEACHER").count(),
        "parents": User.objects.filter(role="PARENT").count(),
    }