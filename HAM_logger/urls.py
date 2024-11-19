"""Defines URL patterns for HAM logger."""

from django.contrib import admin
from django.urls import path, include

from . import views

app_name =  'HAM_logger'

urlpatterns = [
    # Home page
    path('', views.show_main_page, name = 'index'),
    # activities presentation
    path('activities/', views.show_activities_page, name = 'activities'),
    # QSOs in activity
    path('activities/<int:activity_id>/', views.show_activity_page, name = 'activity'),
    # Page to add a new activity
    path('new_activity/', views.show_create_activity_page, name = 'new_activity'),
    # Page to add a new QSO
    path('new_activity/<int:activity_id>/', views.show_create_qso_page, name = 'new_qso'),
    # Pagte to edit a QSO
    path('edit_qso/<int:qso_id>/', views.show_edit_qso_page, name='edit_qso'),
]

