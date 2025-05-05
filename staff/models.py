from django.db import models

# Create your models here.
class StaffUser(models.Model):
    employee_id = models.CharField(max_length=255, unique=True)
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    job_title = models.CharField(max_length=100)
    department = models.CharField(max_length=100)
    monthly_ctc = models.IntegerField()
    date_of_joining = models.DateField()
    email = models.EmailField()
    contact = models.CharField(max_length=15)
    # profile_photo = models.ImageField(upload_to='upload_path e.g staff_photos/',null=True ,blank=True)

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.employee_id})"