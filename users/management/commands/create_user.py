import getpass
from django.core.management.base import BaseCommand
from django.contrib.auth import get_user_model

User = get_user_model()

class Command(BaseCommand):
    help = 'Creates a user for system'

    def handle(self, *args, **kwargs):
        username =  email = first_name = middle_name = last_name = password = confirm_password = str()
        while True:
            username = input("Username: ")
            try:
                if username != "":
                    user = User.objects.get(username=username)
                    self.stdout.write(self.style.ERROR("That Username already exists."))
                    continue
                else:
                    continue
            except User.DoesNotExist:
                while True:
                    first_name = input("First name: ")
                    if first_name == "":
                        continue
                    else:
                        middle_name = input("Middle name: ")
                        while True:
                            last_name = input("Last name: ")
                            if last_name == "":
                                continue
                            else:
                                while True:
                                    email = input("Email: ")
                                    try:
                                        user = User.objects.get(email=email)
                                        self.stdout.write(self.style.ERROR("That Email already exists."))
                                        continue
                                    except User.DoesNotExist:
                                        while True:
                                            password = getpass.getpass("Password: ")
                                            confirm_password = getpass.getpass("Confirm password: ")
                                            if password == confirm_password:
                                                user = User.objects.create_user(
                                                        first_name=first_name,
                                                        last_name=last_name,
                                                        username=username,
                                                        email=email,
                                                        password=password
                                                    )
                                                user.middle_name = middle_name
                                                user.save()
                                                self.stdout.write(self.style.SUCCESS('%s was successfully registered.' % first_name))
                                                break
                                            else:
                                                self.stdout.write(self.style.ERROR("Passwords did not match."))
                                                continue
                                    break
                            break
                    break
            break