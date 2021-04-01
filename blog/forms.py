from crispy_forms.helper import FormHelper
from crispy_forms.layout import Layout, Submit,Div,HTML,Field
from django import forms
from .models import Payment

class PaymentForm(forms.ModelForm):
   

    class Meta:
        model = Payment
        fields = (  'name',
                    'last_name',
                    'email',
                    'contact',
                    'batch',
                    'courses')

    def __init__(self, *args, **kwargs):
        
        super().__init__(*args, **kwargs)

        self.helper = FormHelper
        self.helper.form_method = 'post'

        self.helper.layout = Layout(
            Field('name',placeholder='Name'),
            Field('last_name',placeholder='Last Name'),
            Field('email',placeholder='Email'),
            Field('contact',placeholder='Contact'),
            Field('batch',placeholder='Batch'),
            Field('courses',placeholder='Courses'),
            Div(
                HTML("<button type='submit' class='btn btn-primary'>Submit</button>"),
                css_class='modal-footer',
            ),
            
        )
        # self.helper.layout = Submit('submit','Submit', css_class='modal-footer btn btn-success')
