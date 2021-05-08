from django import forms
from products.models import enrool
from django.core.exceptions import ValidationError

class registerForms(forms.ModelForm):

    firstName = forms.CharField(max_length=100)
    lastName = forms.CharField(max_length=100)
    
    uploadImage = forms.ImageField()
    email = forms.EmailField()

    phoneNumber = forms.CharField(max_length=15)
    WphoneNumber = forms.CharField(max_length=15)
    collegess = forms.CharField(max_length=100)
    
    courses = forms.CharField(max_length=10)
    years = forms.CharField(max_length=1)
    program = forms.CharField(max_length=100)
    price = forms.CharField()


    class Meta:
        model = enrool
        fields = '__all__'


    def clean(self):
        cleaned_data = super().clean()
        firtName = self.cleaned_data.get('firstName')
        lastNam = self.cleaned_data.get('lastName')

        if firtName == "" :
            self._errors['firstName'] = self.error_class(["Can't leave empty"])
            # raise ValidationError('Enter "Deepak" nothing else')
        if lastNam != 'kumar':
            self._errors['lastName'] = self.error_class(['Enter "kumar" only.'])
            
        return cleaned_data