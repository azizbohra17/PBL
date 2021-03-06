from django.shortcuts import render
from django.contrib.auth.decorators import login_required
from django.http import HttpResponse
from .forms import CertificateOfParticipationForm,  MultipleForm
from .functions import handle_uploaded_file

posts = [
    {
        'title': 'The Da Vinci Code',
        'author': 'Dan Brown',
        'content': 'Robert Langton',
        'date_posted': '24 August 2000',
    },
    {
        'title': 'Angel and Demons',
        'author': 'Dan Brown',
        'content': 'XYZ author',
        'date_posted': '10 July 2000',
    },
]


@login_required
def home(request):
    # context = {
    #     'posts': posts,
    # }
    return render(request, 'certificate/home.html')


def about(request):
    return render(request, 'certificate/about.html')


def cop(request):
    form = CertificateOfParticipationForm(request.POST)
    if form.is_valid():
        name = form.cleaned_data['name']
        fest = form.cleaned_data['fest']
        date = form.cleaned_data['date']
        event_name = form.cleaned_data['event_name']
        print(name, fest, date, event_name)

    return render(request, 'certificate/certificate_participation.html', {'form': form})


def optionCertificate(request):
    return render(request, 'certificate/option_for_certificate.html')


def excel_file_upload(request):
    if request.method == 'POST':
        student = MultipleForm(request.POST, request.FILES)
        if student.is_valid():
            handle_uploaded_file(request.FILES['file'])
            return HttpResponse("File uploaded successfully")
    else:
        file = MultipleForm()
        return render(request, 'certificate/multiple_participant.html', {'form': file})
