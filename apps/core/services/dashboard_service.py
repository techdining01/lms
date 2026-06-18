class DashboardService:
    @staticmethod
    def get_dashboard_context(user):

        context = {
            "role": user.role,
            "first_name": user.first_name,
        }

        if user.role == "STUDENT":
            context["welcome_title"] = "Student Dashboard"

        elif user.role == "TEACHER":
            context["welcome_title"] = "Teacher Dashboard"

        elif user.role == "PARENT":
            context["welcome_title"] = "Parent Dashboard"

        elif user.role == "ADMIN":
            context["welcome_title"] = "Admin Dashboard"

        elif user.role == "INSTRUCTOR":
            context["welcome_title"] = "Instructor Dashboard"

        elif user.role == "LEARNER":
            context["welcome_title"] = "Learning Dashboard"

        return context
