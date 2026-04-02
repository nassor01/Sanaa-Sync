from django.db import models
from django.conf import settings

class Resource(models.Model):
    RESOURCE_TYPES = (
        ('hall', 'Space/Hall'),
        ('gear', 'Equipment/Gear'),
    )
    name = models.CharField(max_length=100)
    resource_type = models.CharField(max_length=10, choices=RESOURCE_TYPES)
    description = models.TextField(blank=True)
    capacity = models.IntegerField(default=0, help_text="Applicable for Halls")

    def __str__(self):
        return f"{self.name} ({self.get_resource_type_display()})"

class Booking(models.Model):
    STATUS_CHOICES = (
        ('pending', 'Pending Approval'),
        ('approved', 'Approved'),
        ('completed', 'Completed'),
        ('cancelled', 'Cancelled'),
    )

    user = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='bookings')
    resource = models.ForeignKey(Resource, on_delete=models.CASCADE)
    start_time = models.DateTimeField()
    end_time = models.DateTimeField()
    status = models.CharField(max_length=15, choices=STATUS_CHOICES, default='pending')
    
    # The staff member assigned to supervise this session
    assigned_staff = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.SET_NULL, 
        null=True, 
        blank=True, 
        related_name='supervised_sessions'
    )

    def __str__(self):
        return f"{self.resource.name} | {self.user.username} | {self.start_time.strftime('%d %b')}"