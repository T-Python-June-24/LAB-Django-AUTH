from crispy_forms.helper import FormHelper
from crispy_forms.layout import Submit

class UserRegisterForm(forms.ModelForm):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.helper = FormHelper()
        self.helper.form_method = 'post'
        self.helper.add_input(Submit('submit', 'Register'))

    class Meta:
        model = User
        fields = ['username', 'email', 'password']
