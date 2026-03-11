from django.http import JsonResponse
from .models import Voter
from django.contrib.auth.decorators import login_required
from django.shortcuts import render


@login_required
def search_voter(request):
    name = request.GET.get("name")

    voters = Voter.objects.filter(name_hindi__icontains=name)[:20]

    results = []

    for v in voters:
        results.append({
            "serial_number": v.serial_number,
            "house_no": v.house_number,
            "name": v.name_hindi,
            "father_name": v.father_name,
            "voter_id": v.voter_id,
            "gender": v.gender,
            "age": v.age,
            "district": v.location.district,
            "block": v.location.block,
            "gram_panchayat": v.location.gram_panchayat,
            "ward": v.location.ward,
            "polling_station": v.location.polling_station,
            "booth": v.location.polling_booth,
            "village": v.location.village
        })

    return JsonResponse(results, safe=False)


@login_required
def search_page(request):
    return render(request, "search.html")