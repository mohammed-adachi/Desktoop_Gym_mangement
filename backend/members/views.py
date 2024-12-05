from django.shortcuts import render

# Create your views here.
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from .models import Member
from django.core.files.base import ContentFile
import json

@csrf_exempt
def add_member(request):
    if request.method == "POST":
        data = request.POST
        member = Member(
            first_name=data["first_name"],
            last_name=data["last_name"],
            date_of_birth=data["date_of_birth"],
            cin=data["cin"],
            profession=data["profession"],
            address=data["address"],
            phone=data["phone"],
            sport_type=data["sport_type"],
        )
        if request.FILES.get("photo"):
            member.photo.save(request.FILES["photo"].name, request.FILES["photo"])
        member.save()
        return JsonResponse({"message": "Member added successfully!"}, status=201)
    return JsonResponse({"error": "Invalid request"}, status=400)
