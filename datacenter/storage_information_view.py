from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def storage_information_view(request):
    non_closed_visits = Visit.objects.filter(leaved_at=None)

    serialized_non_closed_visits = []

    for visit in non_closed_visits:

        serialized_non_closed_visits.append(
            {
                'who_entered': visit.passcard,
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(visit.get_duration(
                    leaved_at=localtime())),
                'is_strange': visit.is_visit_long(visit.get_duration(
                    leaved_at=localtime()))
            }
        )
    context = {
        'non_closed_visits': serialized_non_closed_visits,
    }
    return render(request, 'storage_information.html', context)
