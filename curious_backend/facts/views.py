from django.shortcuts import render

# Create your views here.
from django.http import HttpResponse, JsonResponse
from django.core import serializers
from django.http import Http404, HttpResponseNotAllowed
import json
from .models import Facts, Categories


def create_fact(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        print(data)
        fact = Facts(body=data['body'], category=data['category'])
        fact.save()
        return HttpResponse("Fact created")
    else:
        return HttpResponseNotAllowed(['POST'])
def update_fact(request, fact_id):
    if request.method == 'PUT':
        data = json.loads(request.body)
        fact = Facts.objects.get(pk=fact_id)
        fact.body = data['body']
        fact.category = data['category']
        fact.save()
        return HttpResponse("Fact updated")
    else:
        return HttpResponseNotAllowed(['PUT'])
    
    
def delete_fact(request, fact_id):
    if request.method == 'DELETE':
        fact = Facts.objects.get(pk=fact_id)
        fact.delete()
        return HttpResponse("Fact deleted")
    else:
        return HttpResponseNotAllowed(['DELETE'])
    
def create_category(request):
    if request.method == 'POST':
        data = json.loads(request.body)
        category = Categories(name=data['name'])
        category.save()
        return HttpResponse("Category created")
    else:
        return HttpResponseNotAllowed(['POST'])
    
def update_category(request, category_id):

    if request.method == 'PUT':
        data = json.loads(request.body)
        category = Categories.objects.get(pk=category_id)
        category.name = data['name']
        category.save()
        return HttpResponse("Category updated")
    else:
        return HttpResponseNotAllowed(['PUT'])
def delete_category(request, category_id):
    if request.method == 'DELETE':
        category = Categories.objects.get(pk=category_id)
        category.delete()
        return HttpResponse("Category deleted")
    else:
        return HttpResponseNotAllowed(['DELETE'])
    
def facts_list(request):
    facts = Facts.objects.all()
    facts = list(facts.values())
    return JsonResponse(facts, safe=False)

def facts_detail(request, pk):
    try:
        fact = Facts.objects.get(pk=pk)
    except Facts.DoesNotExist:
        raise Http404("Fact does not exist")
    return JsonResponse({"body": fact.body, "category": fact.category})

def categories_list(request):
    categories = Categories.objects.all()
    categories = list(categories.values())
    return JsonResponse(categories, safe=False)

def categories_detail(request, pk):
    try:
        category = Categories.objects.get(pk=pk)
    except Categories.DoesNotExist:
        raise Http404("Category does not exist")
    return JsonResponse({"name": category.name})

