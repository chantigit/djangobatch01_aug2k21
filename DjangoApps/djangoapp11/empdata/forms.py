from django import forms
class EmpSignInForm(forms.Form):
    fullName=forms.CharField(max_length=10, help_text='10 characters max.')
    age=forms.IntegerField()
    email=forms.EmailField(help_text='A valid email address, please.')
    password=forms.CharField(widget=forms.PasswordInput())
    address=forms.CharField(widget=forms.Textarea)
    #Approach1: Using clean_fieldname()
    def clean_fullName(self):
        print('Validating fullName')
        fn=self.cleaned_data['fullName']
        if len(fn)<5:
            raise forms.ValidationError('Your name must be greater than 5 letters')
        return fn
    def clean_age(self):
        print('Validating age')
        age = self.cleaned_data['age']
        if age > 100:
            raise forms.ValidationError('Age must be less than 100')
        return age