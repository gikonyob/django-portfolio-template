from django.forms import ModelForm
from users.models import Profile


class UpdateProfileForm(ModelForm):
    class Meta:
        model = Profile
        fields = (
            "secondary_email",
            "mobile_no",
            "secondary_mobile_no",
            "date_of_birth",
            "profile_picture",
            "bio",
        )