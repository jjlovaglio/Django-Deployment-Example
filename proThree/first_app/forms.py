from django import forms
from first_app.models import User

class SignupForm(forms.ModelForm):
    # first_name = forms.CharField()
    # last_name = forms.CharField()
    # email = forms.EmailField()

    class Meta:
        model = User
        fields = "__all__"