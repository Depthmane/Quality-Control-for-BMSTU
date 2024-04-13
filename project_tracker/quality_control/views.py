from django.http import HttpResponse
from django.urls import reverse

def index(request):
    bug_list_url = reverse('quality_control:bug_list')
    feature_list_url = reverse('quality_control:feature_list')
    html = f"<h1> Система контроля качества </h1> " \
           f"<a href='{bug_list_url}'> Список всех багов"  \
           f"<a href='{feature_list_url}'> Запросы на улучшение"
    return HttpResponse(html)

def bug_list(request):
    return HttpResponse('Cписок отчетов об ошибках')

def feature_list(request):
    return HttpResponse('Список запросов на улучшение')

def bug_detail(request, bug_id):
    return HttpResponse(f'Детали бага {bug_id}')

def feature_id_detail(request, feature_id):
    return HttpResponse(f'Детали улучшения {feature_id}')

