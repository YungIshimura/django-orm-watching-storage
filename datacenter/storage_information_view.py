from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def get_duration(visit):
    duration = (localtime() - visit.entered_at).total_seconds()
    
    return duration


def format_duration(duration):
    hours = int(duration//3600)
    minutes = int((duration%3600)//60)
    
    return f"{hours}:{minutes}"


def storage_information_view(request):
    visits = Visit.objects.filter(leaved_at = None)

    non_closed_visits = []
    
    for visit in visits:
    
        non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': format_duration(get_duration(visit)),
            }
        )
    context = {
        'non_closed_visits': non_closed_visits,  # не закрытые посещения
    }
    return render(request, 'storage_information.html', context)
