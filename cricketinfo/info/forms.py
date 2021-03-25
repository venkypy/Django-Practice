from django import forms
from info.models import Player2


class Player2Form(forms.ModelForm):

    class Meta:
        model = Player2
        fields = "__all__"

    def clean_name(self, value=None):
        name = self.data.get("name")
        if not name.isalnum():
            raise forms.ValidationError("Special symbols are not allowed in the Name....")
        return name
