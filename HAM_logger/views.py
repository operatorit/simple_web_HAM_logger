from django.shortcuts import render, redirect, get_object_or_404
from django.contrib.auth.decorators import login_required
from django.http import Http404

from .models import Activity, Contact 
from .forms import ActivityForm, QSOForm

# Create your views here.

def show_main_page(request):
    """The home page for HAM logger."""
    return render(request, 'HAM_logger/index.html')

def check_activity_owner(owner, current_user):
    """Check if user has priviledges to modify the activity."""
    if owner != current_user:
        raise Http404

@login_required
def show_activities_page(request):
    """Show all activities"""
    activities = Activity.objects.filter(owner = request.user).order_by('date_added')
    context = {'activities': activities}
    return render(request, 'HAM_logger/activities.html', context)

@login_required
def show_activity_page(request, activity_id):
    """Show a single activity with all its QSOs"""
    activity =  get_object_or_404(Activity, id = activity_id)
    # Make sure the activation belongs to the current user
    check_activity_owner(activity.owner, request.user)

    qsos = activity.contact_set.order_by('-date_added')
    context = {'activity': activity, 'QSOs': qsos}
    return render(request, 'HAM_logger/activity.html', context)

@login_required
def show_create_activity_page(request):
    """Adds a new activity to the log"""
    if request.method == 'GET': 
        # no data submitted, create a blank forms
        form = ActivityForm()
    elif request.method == 'POST':
        #POST data submitted, process data
        form = ActivityForm(data = request.POST)
        if form.is_valid():
            new_activity = form.save(commit = False)
            new_activity.owner = request.user
            new_activity.save()
            return redirect ('HAM_logger:activities')

    # display a form - blank or invalid
    context = {'form': form}
    return render(request, 'HAM_logger/new_activity.html', context)

@login_required
def show_create_qso_page(request, activity_id):
    """Add a new QSO to selected activity"""
    activity = Activity.objects.get(id = activity_id)

    if request.method == 'GET':
        # No data submitted, create a blank form
        form = QSOForm()

    elif request.method == 'POST':
        # POST data submitted, process data
        form = QSOForm(data = request.POST)
        if form.is_valid():
            new_qso = form.save(commit = False)
            new_qso.activity = activity
            # Make sure user adds QSO to its own activity
            check_activity_owner(activity.owner, request.user)
            new_qso.save()
            return redirect('HAM_logger:activity', activity_id = activity_id)

    # Display a blank or invalid frm
    context = {'activity': activity,
               'form': form,}

    return render(request, 'HAM_logger/new_qso.html', context)

@login_required
def show_edit_qso_page(request, qso_id):
    """Edit an existing QSO"""
    qso = Contact.objects.get(id = qso_id)
    activity = qso.activity
    # Check if user can edit QSO
    check_activity_owner(activity.owner, request.user)

    if request.method == 'GET':
        # Initial request: pre-fill form with the current QSO data
        form = QSOForm(instance = qso)
    elif request.method == 'POST':
        # POST data submitted; process data
        form = QSOForm(instance = qso, data = request.POST)
        if form.is_valid():
            form.save()
            return redirect('HAM_logger:activity', activity_id = activity.id)

    context = {'qso': qso, 'activity': activity, 'form': form}
    return render(request, 'HAM_logger/edit_qso.html', context)

