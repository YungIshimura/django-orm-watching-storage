from datacenter.models import Passcard
from datacenter.models import Visit
from django.shortcuts import render
from django.utils.timezone import localtime


def passcard_info_view(request, passcode):
    passcard = Passcard.objects.get(passcode=passcode)
    visits = Visit.objects.filter(passcard=passcard)

    this_passcard_visits = []

    for visit in visits:
        this_passcard_visits.append(
            {
                'entered_at': visit.entered_at,
                'duration': visit.format_duration(visit.get_duration(
                    leaved_at=localtime())),
                'is_strange': visit.is_visit_long(visit.get_duration(
                    leaved_at=localtime()))
            },
        )
        context = {
            'passcard': passcard,
            'this_passcard_visits': this_passcard_visits
        }
    return render(request, 'passcard_info.html', context)
