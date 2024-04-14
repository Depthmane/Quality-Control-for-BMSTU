from django.urls import path
from . import views

app_name = 'quality_control'

urlpatterns = [
    path('', views.IndexView.as_view(), name='quality_control'), # классовые представления

    path('bugs/', views.BugListView.as_view(), name='bug_list'),
    path('bugs/<bug_id>/', views.BugDetailView.as_view(), name='bug_detail'),

    path('features/', views.FeatureRequestListView.as_view(), name='feature_list'),
    path('features/<feature_id>/', views.FeatureRequestDetaillView.as_view(), name='feature_id_detail'),





    #сцылки для функциональных представлений (old)
#    path('', views.index, name='quality_control'),
#    path('bugs/', views.bug_list, name='bug_list'),
#    path('features/', views.feature_list, name='feature_list'),
#
#    path('bugs/<bug_id>/', views.bug_detail, name='bug_detail'),
#    path('features/<feature_id>/', views.feature_id_detail, name='feature_id_detail'),
]