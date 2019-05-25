from django import forms
from django.forms import Textarea

from django.contrib.auth import(
    authenticate,
    get_user_model,
    login,
    logout,
)

from .models import Task, HelperSignUp

User = get_user_model()

class UserLoginForm(forms.Form):
   
    username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))


    def clean(self, *args , **kwargs):
        username = self.cleaned_data.get("username")
        password = self.cleaned_data.get("password")

        if username and password:
            user = authenticate(username =username, password =password)

            if not user:
                raise forms.ValidationError("This user doesnt exist")
        
            if not user.check_password(password):
                raise forms.ValidationError("Incorrect Password")
            if not user.is_active:
                raise forms.ValidationError("This user is no longer active")
            return super(UserLoginForm , self).clean(*args, **kwargs)

class UserSignUpForm(forms.ModelForm):
   
    username = forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'placeholder':'Username'}))
    password =forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Password'}))
    email=forms.EmailField(widget=forms.TextInput(attrs={'placeholder':'Email'}))
    Confirm_Password = forms.CharField(widget=forms.PasswordInput(attrs={'placeholder':'Confirm Password'}))
    phone=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'placeholder':'Phone'}))
    address=forms.CharField(max_length=30 ,widget=forms.TextInput(attrs={'placeholder':'Address'}))

    class Meta:
        model= User
        fields = [
            'username',
            'email',            
            'password', 
            'phone',
            'address',              
        ]
    
    def clean_Confirm_Password(self):
        password = self.cleaned_data.get('password')
        password2 = self.cleaned_data.get('Confirm_Password')        

        if password != password2:
            raise forms.ValidationError("Passwords Mismatch")        

        return password



class TaskForm(forms.ModelForm):
     class Meta:
        model= Task
        # date = forms.DateTimeField(input_formats=['%d/%m/%Y %H:%M'])
        fields = [ 'title','description','service_date','service_time','pickup_location','drop_location','phone']
        widgets = {
            'description' : Textarea(attrs={'cols':30, 'rows':3}),
        }

class HelperForm(forms.ModelForm):
    confirm_password = forms.CharField(widget=forms.PasswordInput)
    password =forms.CharField(widget=forms.PasswordInput)

    class Meta:
        model = HelperSignUp
        fields =['first_name','last_name','email','password','confirm_password','phone','address','description']
        widgets = {
            'description' : Textarea(attrs={'cols':30, 'rows':3}),
        }

    
        


    
