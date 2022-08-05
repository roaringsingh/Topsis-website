from django import forms
from .models import UserData


class DataForm(forms.ModelForm):
    file = forms.FileField()

    class Meta:
        model = UserData
        fields = ['columns', 'weights', 'impacts', 'add']

    def clean_file(self):
        file = self.cleaned_data.get('file')
        if not file.name.endswith('csv'):
            raise forms.ValidationError('.csv file only')
        return file

    def clean_columns(self):
        col = self.cleaned_data.get('columns')
        if not col > 1:
            raise forms.ValidationError('At least 2 columns required')
        return col

    def clean_weights(self):
        weights = self.cleaned_data.get('weights')
        col = self.cleaned_data.get('columns')
        try:
            w = [float(x) for x in weights.split(',')]
        except ValueError:
            raise forms.ValidationError('comma separated decimals only')
        if len(w) != col:
            raise forms.ValidationError('Weights should be equal to columns')
        return weights

    def clean_impacts(self):
        impacts = self.cleaned_data.get('impacts')
        col = self.cleaned_data.get('columns')
        try:
            i = [x for x in impacts.split(',')]
        except ValueError:
            raise forms.ValidationError('comma separated only')
        if len(i) != col:
            raise forms.ValidationError('Impacts should be equal to columns')
        for sig in i:
            if sig != '+' and sig != '-':
                raise forms.ValidationError('+ and - only')
        return impacts
