from django import forms
from django.contrib.auth.forms import UserCreationForm
from django.db import transaction

from DjangoRestAPI.accounts.models import User
from .models import Dealer


class DealerSignUpForm(UserCreationForm):
    interests = forms.ModelMultipleChoiceField(
        queryset=Subject.objects.all(),
        widget=forms.CheckboxSelectMultiple,
        required=True
    )

    class Meta(UserCreationForm.Meta):
        model = User

    @transaction.atomic
    def save(self):
        user = super().save(commit=False)
        user.is_dealer = True
        user.save()
        dealer = Dealer.objects.create(user=user)
        student.interests.add(*self.cleaned_data.get('interests'))
        return user
