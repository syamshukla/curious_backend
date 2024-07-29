from django.urls import path
from . import views

urlpatterns = [
    path('facts/', views.facts_list),
    path('facts/<int:pk>/', views.facts_detail),
    path('categories/', views.categories_list),
    path('categories/<int:pk>/', views.categories_detail),
    path('create_category/', views.create_category),
    path('update_category/<int:category_id>/', views.update_category),
    path('delete_category/<int:category_id>/', views.delete_category),
    path('create_fact/', views.create_fact),
    path('update_fact/<int:fact_id>/', views.update_fact),
    path('delete_fact/<int:fact_id>/', views.delete_fact),
    
]
