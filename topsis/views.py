from django.contrib.auth.decorators import login_required
from django.shortcuts import render, redirect, reverse
from django.http import HttpResponse
from django import forms
from .models import UserData
from .forms import DataForm
from .files import file_topsis
import pandas as pd


# Create your views here.
# @login_required()
def data_view(request):
    dataform = DataForm()
    if request.POST:
        dataform = DataForm(request.POST, request.FILES)
        if dataform.is_valid():
            result = file_topsis(request.FILES['file'], dataform.cleaned_data)  # returns dataframe or error
            if result.empty:
                return render(request, 'topsis/error.html', {})
            if dataform.cleaned_data['add']:
                dataform.cleaned_data['user'] = request.user
                obj = UserData(user=dataform.cleaned_data['user'], columns=dataform.cleaned_data['columns'],
                               weights=dataform.cleaned_data['weights'], impacts=dataform.cleaned_data['impacts'],
                               add=dataform.cleaned_data['add'], file=result.to_csv(index=False),
                               html=result.to_html(index=False))
                obj.save()
            result_table = result.to_html()
            context = {
                'table': result_table,
            }
            return render(request, 'topsis/table.html', context)
    context = {
        'form': dataform
    }
    return render(request, 'topsis/dataform.html', context)
