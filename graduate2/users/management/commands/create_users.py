from django.core.management import BaseCommand

from users.models import User


class Command(BaseCommand):

    def handle(self, *args, **options):
        check_admin = User.objects.filter(phone_number=1111111111)

        if check_admin:
            return 'We already have users!'

        admin = User.objects.create(
            phone_number=1111111111,
            is_community=True,
            is_superuser=True,
            is_staff=True,
            is_active=True
        )

        admin.set_password('12345')
        admin.save()

        society_user = User.objects.create(
            phone_number=2222222222,
            is_community=False,
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        society_user.set_password('12345')
        society_user.save()

        community_user = User.objects.create(
            phone_number=3333333333,
            is_community=True,
            is_superuser=False,
            is_staff=False,
            is_active=True
        )

        community_user.set_password('12345')
        community_user.save()
