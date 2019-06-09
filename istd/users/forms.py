from django import forms


class LoginForm(forms.Form):
    email = forms.EmailField(label='Адрес электронной почты', min_length=5, max_length=60,
                             widget=forms.EmailInput({'id': 'input-auth-email', 'class': 'form-control', 'placeholder': 'example@example.com', 'autocomplete': 'new_email'}),
                             required=True)
    password = forms.CharField(label='Пароль', min_length=5, max_length=60,
                               widget=forms.PasswordInput({'id': 'input-auth-password', 'class': 'form-control', 'placeholder': 'Ваш пароль'}),
                               required=True)


class RegisterForm(forms.Form):
    email = forms.EmailField(label='Адрес электронной почты', min_length=5, max_length=60,
                             widget=forms.EmailInput({'id': 'input-reg-email', 'class': 'form-control', 'placeholder': 'example@example.com'}), required=True)
    password = forms.CharField(label='Пароль', min_length=6, max_length=60,
                               widget=forms.PasswordInput({'id': 'input-reg-password', 'class': 'form-control', 'placeholder': 'Ваш пароль'}), required=True,
                               help_text='Ваш пароль должен содержать не менее <b>6</b> символов')


# class ChangeUserInfo(forms.ModelForm):
#     hidden_field = forms.CharField(widget=forms.HiddenInput({'name': 'change', 'value': 'info'}))
#
#     class Meta:
#         model = User
#         fields = ['email', 'password', 'tel', 'first_name']
#         widgets = {
#             'email': forms.EmailInput(attrs={'id': 'users-city', 'class': 'form-control', 'placeholder': 'email'}),
#             'first_name': forms.TextInput(attrs={'id': 'users-city', 'class': 'form-control', 'placeholder': 'email'}),
#             'tel': forms.TextInput(attrs={'id': 'users-street', 'class': 'form-control', 'placeholder': 'Этаж', 'type': 'tel'}),
#         }


# class ChangeUserProfile(forms.ModelForm):
#     hidden_field = forms.CharField(widget=forms.HiddenInput({'name': 'change', 'value': 'profile'}))
#
#     class Meta:
#         model = UserProfile
#         fields = ['city', 'street', 'flat_number', 'etrance', 'floor']
#         widgets = {
#             'city': forms.TextInput(attrs={'class': 'form-control city', 'placeholder': 'Ваш город'}),
#             'street': forms.TextInput(attrs={'id': 'users-street', 'class': 'form-control', 'placeholder': 'Улица'}),
#             'flat_number': forms.NumberInput(attrs={'id': 'users-street', 'class': 'form-control', 'placeholder': 'Номер квартиры'}),
#             'etrance': forms.NumberInput(attrs={'id': 'users-street', 'class': 'form-control', 'placeholder': 'Номер подъезда'}),
#             'floor': forms.NumberInput(attrs={'id': 'users-street', 'class': 'form-control', 'placeholder': 'Этаж'}),
#         }

class AddPhoto(forms.Form):
    file = forms.ImageField(label='file', required=True)
    username = forms.CharField(label='username', required=True)
    email = forms.EmailField(label='email', required=True)

    def clean(self):
        upload_to = 'vote/%Y_%m_%d'
        if not 'avatar' in self.cleaned_data:
            return self.cleaned_data
        upload_to += self.cleaned_data['avatar'].name
        super(AddPhoto, self).clean()
