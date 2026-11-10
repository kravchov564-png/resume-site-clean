from django.shortcuts import render, get_object_or_404
from .models import Resume, SkillGroup, Experience, Project, Education


def resume_view(request):
    resume = get_object_or_404(Resume)

    context = {
        'resume': resume,
        'skill_groups': SkillGroup.objects.all(),
        'experiences': Experience.objects.all(),
        'projects': Project.objects.all(),
        'educations': Education.objects.all(),
    }
    return render(request, 'main/index.html', context)
