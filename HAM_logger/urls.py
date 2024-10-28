"""Defines URL patterns for HAM logger."""

from django.contrib import admin
from django.urls import path, include

from . import views

app_name =  'HAM_logger'

urlpatterns = [
    # Home page
    path('', views.index, name = 'index'),
    # activities presentation
    path('activities/', views.activities, name = 'activities'),
    # QSOs in activity
    path('activities/<int:activity_id>/', views.activity, name = 'activity'),
    # Page to add a new activity
    path('new_activity/', views.new_activity, name = 'new_activity'),
    # Page to add a new QSO
    path('new_activity/<int:activity_id>/', views.new_qso, name = 'new_qso'),
    # Pagte to edit a QSO
    path('edit_qso/<int:qso_id>/', views.edit_qso, name='edit_qso'),
]

