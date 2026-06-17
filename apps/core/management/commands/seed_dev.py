from django.core.management.base import BaseCommand
from django.db import transaction
from django.utils import timezone

from django.contrib.auth import get_user_model

from apps.accounts.models import StudentProfile
from apps.academics.models.school_class import SchoolClass
from apps.academics.models.subject import Subject
from apps.academics.models.session import AcademicSession
from apps.academics.models.term import Term


class Command(BaseCommand):
    help = "Seed development data: users, classes, subjects, session, term"

    def handle(self, *args, **options):
        User = get_user_model()

        with transaction.atomic():
            self.stdout.write("Seeding academic session and term...")
            today = timezone.localdate()
            session_name = f"{today.year}/{today.year + 1}"
            session, _ = AcademicSession.objects.get_or_create(
                name=session_name,
                defaults={
                    "start_date": today,
                    "end_date": today.replace(year=today.year + 1),
                },
            )

            term, _ = Term.objects.get_or_create(
                session=session,
                name=Term.TermChoices.FIRST,
                defaults={
                    "is_current": True,
                    "start_date": today,
                    "end_date": today.replace(month=12, day=31),
                },
            )

            self.stdout.write("Seeding subjects...")
            subjects = []
            for i in range(1, 11):
                name = f"Subject {i}"
                code = f"SUB{i:02d}"
                subj, _ = Subject.objects.get_or_create(
                    name=name, defaults={"code": code}
                )
                subjects.append(subj)

            self.stdout.write("Seeding classes...")
            classes = []
            for i in range(1, 4):
                name = f"Class {i}"
                cls, _ = SchoolClass.objects.get_or_create(name=name)
                classes.append(cls)

            self.stdout.write("Seeding users...")

            # Super Admin
            sa_username = "superadmin"
            if not User.objects.filter(username=sa_username).exists():
                User.objects.create_superuser(
                    sa_username, "superadmin@example.com", "password"
                )

            # Admin
            admin_username = "admin"
            admin, created = User.objects.get_or_create(
                username=admin_username,
                defaults={
                    "email": "admin@example.com",
                    "role": User.Role.ADMIN,
                    "is_staff": True,
                },
            )
            if created:
                admin.set_password("password")
                admin.save()

            # Teachers
            teachers = []
            for i in range(1, 6):
                uname = f"teacher{i}"
                user, created = User.objects.get_or_create(
                    username=uname,
                    defaults={
                        "email": f"{uname}@example.com",
                        "role": User.Role.TEACHER,
                        "is_staff": True,
                    },
                )
                if created:
                    user.set_password("password")
                    user.save()
                teachers.append(user)

            # Students
            students = []
            for i in range(1, 21):
                uname = f"student{i}"
                user, created = User.objects.get_or_create(
                    username=uname,
                    defaults={
                        "email": f"{uname}@example.com",
                        "role": User.Role.STUDENT,
                    },
                )
                if created:
                    user.set_password("password")
                    user.save()

                # Create StudentProfile
                admission = f"S{i:04d}"
                StudentProfile.objects.get_or_create(
                    user=user, defaults={"admission_number": admission}
                )
                students.append(user)

            self.stdout.write(self.style.SUCCESS("Seeding complete."))
