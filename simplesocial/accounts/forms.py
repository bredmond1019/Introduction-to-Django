# returns user model currenlty active in this project
from django.contrib.auth import get_user_model
# Built in User Creation Form -- how to create user and admin accounts -- great documentation page
from django.contrib.auth.forms import UserCreationForm


class UserCreateForm(UserCreationForm):
    
    # These are the fields that the user is going to have acess to when they sign up
    class Meta:
        # the fields we are putting here are acutally
        # already available to me by the contrib.auth import
        fields = ('username', 'email', 'password1', 'password2')
        
        # This allows us to get the current model of who ever is currently accessing the site
        model = get_user_model()

        # This allows us to set up a label for the fields
        def __init__(self, *args, **kwargs):
            super()._init__(*args, **kwargs)
            self.fields['username'].label = 'Display Name'  #Could say something like 'Twitter Handle'
            self.fields['email'].label = 'Email Address'

