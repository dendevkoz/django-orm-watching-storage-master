from datacenter.models import Visit
from django.shortcuts import render


def storage_information_view(request):
    workers_in_storage = []
    now_in_storage = Visit.objects.filter(leaved_at=None)
    for visit in now_in_storage:
        duration = visit.get_duration()
        format_time = visit.format_duration(duration)
        is_strange = visit.is_visit_long(duration)
        worker_in_storage = {
            'who_entered': visit.passcard.owner_name,
            'entered_at': visit.entered_at,
            'duration': format_time,
            'is_strange': is_strange,
        }
        workers_in_storage.append(worker_in_storage)
    context = {'non_closed_visits': workers_in_storage,
               }
    return render(request, 'storage_information.html', context)


