from django.db import models
from django.contrib.auth.models import User
from django.utils.timezone import now

class Activity(models.Model):
    """An activity the user is logging."""
	
    text = models.CharField(max_length = 180)
    date_added = models.DateTimeField(auto_now_add = True) # auto activity date when it's added
    owner = models.ForeignKey(User, on_delete = models.CASCADE)

	# operation type
    home = " "
    stationary = "/n"
    portable = "/P"
    mobile = "/M"
    aeronautical = "/AM"
    maritime = "/MM"

    operation_type_choices = [
        (home, 'home QTH'),
        (stationary, 'stationary outside home QTH'),
        (portable, 'portable'),
        (mobile, 'mobile'),
        (aeronautical, 'aeronautical mobile'),
        (maritime, 'maritime mobile'),
        ]
	
    operation_type = models.CharField(max_length = 3,
                    choices = operation_type_choices,
                    default = home,
                    )

    class Meta:
        verbose_name_plural = 'Activities'

    def __str__(self):
        """Return a string representation of the model."""
        return self.text

class Contact(models.Model):
    """A single QSO in the activity."""
    activity = models.ForeignKey(Activity, on_delete =  models.CASCADE)
    date_added = models.DateField(auto_now_add = True)
    time_added = models.TimeField(auto_now_add = True)
    my_call= models.CharField(max_length = 15)
    your_call = models.CharField(max_length = 15)
    freq =  models.CharField(max_length = 10)
    mode = models.CharField(max_length = 3)
    sent_report = models.IntegerField()
    received_report = models.IntegerField()
    my_ref =  models.CharField(max_length = 15, null = True, blank = True)
    your_ref = models.CharField(max_length = 15, null = True, blank = True)

    class Meta:
        verbose_name_plural = 'QSOs'

    def __str__(self):
        """Return a string representation of the model"""
        return f"{self.your_call}"
