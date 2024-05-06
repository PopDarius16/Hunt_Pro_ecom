from django.contrib.auth.models import User
from django.contrib.auth.forms import UserCreationForm, UserChangeForm, SetPasswordForm
from django import forms
from .models import Profile


class UserInfoForm(forms.ModelForm):
    phone = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Telefon'}),
                            required=False)
    address1 = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa 1'}),
                               required=False)
    address2 = forms.CharField(label="",
                               widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa 2'}),
                               required=False)
    city = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Orașul'}),
                           required=False)
    state = forms.CharField(label="", widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Județul'}),
                            required=False)
    zipcode = forms.CharField(label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Cod poștal'}),
                              required=False)
    country = forms.CharField(label="",
                              widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Țara'}),
                              required=False)

    class Meta:
        model = Profile
        fields = ('phone', 'address1', 'address2', 'city', 'state', 'zipcode', 'country',)


class ChangePasswordForm(SetPasswordForm):
    class Meta:
        model = User
        fields = ['new_password1', 'new_password2']

    def __init__(self, *args, **kwargs):
        super(ChangePasswordForm, self).__init__(*args, **kwargs)

        self.fields['new_password1'].widget.attrs['class'] = 'form-control'
        self.fields['new_password1'].widget.attrs['placeholder'] = 'Parola'
        self.fields['new_password1'].label = ''
        self.fields[
            'new_password1'].help_text = ('<ul class="form-text text-muted small">'
                                          '<li>Parola dvs. nu poate fi prea '
                                          'asemănătoare cu celelalte informații personale.'
                                          '</li><li>Parola dvs. trebuie să conțină cel puțin 8 caractere.'
                                          '</li><li>Parola dvs. nu poate fi o parolă folosită în mod obișnuit.'
                                          '</li><li>Parola dvs. nu poate fi în întregime numerică.')

        self.fields['new_password2'].widget.attrs['class'] = 'form-control'
        self.fields['new_password2'].widget.attrs['placeholder'] = 'Confirmă parola'
        self.fields['new_password2'].label = ''
        self.fields[
            'new_password2'].help_text = ('<span class="form-text text-muted">'
                                          '<small>Introduceți aceeași parolă ca înainte, '
                                          'pentru verificare.</small></span>')


class UpdateUserForm(UserChangeForm):
    # Hide Password stuff
    password = None
    # Get other fields
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa de mail'}),
                             required=False)
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}),
                                 required=False)
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}),
                                required=False)

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email')

    def __init__(self, *args, **kwargs):
        super(UpdateUserForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nume utilizator'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = ('<span class="form-text text-muted">'
                                     '<small>Necesar. 30 de caractere sau mai puțin. Numai litere, cifre și @/./+/-/_.'
                                     '</small></span>')


class SignUpForm(UserCreationForm):
    email = forms.EmailField(label="",
                             widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Adresa de mail'}))
    first_name = forms.CharField(label="", max_length=100,
                                 widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Nume'}))
    last_name = forms.CharField(label="", max_length=100,
                                widget=forms.TextInput(attrs={'class': 'form-control', 'placeholder': 'Prenume'}))

    class Meta:
        model = User
        fields = ('username', 'first_name', 'last_name', 'email', 'password1', 'password2')

    def __init__(self, *args, **kwargs):
        super(SignUpForm, self).__init__(*args, **kwargs)

        self.fields['username'].widget.attrs['class'] = 'form-control'
        self.fields['username'].widget.attrs['placeholder'] = 'Nume de utilizator'
        self.fields['username'].label = ''
        self.fields[
            'username'].help_text = ('<span class="form-text text-muted"><small>Necesar. 150 de caractere sau mai '
                                     'puțin.'
                                     'Numai litere, cifre și @/./+/-/_.</small></span>')

        self.fields['password1'].widget.attrs['class'] = 'form-control'
        self.fields['password1'].widget.attrs['placeholder'] = 'Parola'
        self.fields['password1'].label = ''
        self.fields[
            'password1'].help_text = ('<ul class="form-text text-muted small"><li>Parola dvs. nu poate fi prea '
                                      'asemănătoare'
                                      'la celelalte informații personale.</li><li>Parola dvs. trebuie sa conțină '
                                      'cel puțin 8 caractere.</li><li>Parola dvs. nu poate fi o parolă folosită în '
                                      'mod obișnuit.</li><li>Parola dvs. nu poate fi în întregime numerică.</li></ul>')

        self.fields['password2'].widget.attrs['class'] = 'form-control'
        self.fields['password2'].widget.attrs['placeholder'] = 'Confirmă parola'
        self.fields['password2'].label = ''
        self.fields[
            'password2'].help_text = ('<span class="form-text text-muted"><small>Introduceți aceeași parolă ca '
                                      'înainte, pentru verificare.</small></span>')
