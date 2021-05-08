from django import forms


class test_form(forms.Form):

    text_val = forms.CharField(
        label='test',
        max_length=100,
        widget=forms.TextInput(attrs={
            'class':"input",'type':"text",
            'name':"first-name",'placeholder':"First Name",'style':"width:30rem"})
    )
