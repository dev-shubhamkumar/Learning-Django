from django.shortcuts import render     ## render is used to render dynamic content to webpage


# Create your views here.
def index(request):
    meetups = [
        {'title': 'A First Meetup'},
        {'title': 'A Second Meetup'}
    ]
    return render(request, 'meetups/index.html', {
        'show_meetups': True,
        'meetups': meetups
    })