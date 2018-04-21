from django.db import models
from django import forms
from django.core.urlresolvers import reverse

# Create your models here.
class County(models.Model):
    COUNTY_CHOICES = (
        (1 , 'Kajiado'),
        (10,'Marsabit'),
        (9, 'Mandera'),
        (8, 'Garissa'),
        (7, 'Laikipia'),
        (6, 'Nakuru'),
        (4, 'Bomet'),
        (14, 'Kirinyaga'),


    )

    name = models.CharField(max_length = 10, choices=COUNTY_CHOICES)
    code = models.IntegerField()
    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("visitor:detail", kwargs={"id": self.id})
    class Meta:
        ordering = ["id"]
    def create_county(self):
        return self.save()

    def delete_county(self):
        return self.delete()
    @classmethod
    def update_county(cls, id, name):
        update_county = County.objects.filter(id=id).update(name = name)
        return update_visitor
    @classmethod
    def search(cls,search_term):
        county_search = cls.objects.filter(name__name__icontains=search_term)
        return county_search
class Visitor(models.Model):
    name = models.CharField(max_length=40)
    GENDER_CHOICES = (
        ('M', 'Male'),
        ('F', 'Female'), 
    )
    gender = models.CharField(max_length=1, choices=GENDER_CHOICES)
    age = models.IntegerField(null=True,blank=True)
    county = models.ForeignKey(County,on_delete=models.CASCADE, null=True,blank=True)
    arrival = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    departure = models.DateTimeField(auto_now=False,auto_now_add=False,null=True,blank=True)
    room = models.ForeignKey('Room',on_delete=models.CASCADE, null=True,blank=True)
    service = models.ManyToManyField('Service')

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("visitor:detail", kwargs={"id": self.id})
    class Meta:
        ordering = ['id']
    def create_visitor(self):
        return self.save()

    def delete_visitor(self):
        return self.delete()
    @classmethod
    def update_visitor(cls, id, name):
        update_visitor = Visitor.objects.filter(id=id).update(name = name)
        return update_visitor
    @classmethod
    def search(cls,search_term):
        visitor_search = cls.objects.filter(name__name__icontains=search_term)
        return visitor_search

class Room(models.Model):
    room_number = models.IntegerField()
    rate_per_day = models.DecimalField(max_digits=6, decimal_places=2)
    
    SINGLEROOM='SR'
    DOUBLEROOM ='DR'
    MASTERENSUITE = 'ME'
    EXECUTIVEWING='EW'
    ROOM_CHOICES = (
    (SINGLEROOM, 'SingleRoom'),
    (DOUBLEROOM, 'DoubleRoom'),
    (MASTERENSUITE, 'MasterEnsuite'),
    (EXECUTIVEWING, 'ExecutiveWing'),
)
    room_type = models.CharField(max_length=20, choices=ROOM_CHOICES,default=SINGLEROOM)
   
    OCCUPANCY_CHOICES = (
        ('V', 'Vacant'),
        ('O', 'Occupied'), 
    )
    occupancy = models.CharField(max_length=1, choices=OCCUPANCY_CHOICES)
    
    def __str__(self):
        return self.room_type
    
    
class Service(models.Model):
    service_name = models.CharField(max_length=30)
    amount_charged = models.DecimalField(max_digits=6, decimal_places=2)
    LAUNDRY = 'LR'
    ROOMS ='RM'
    WIFI = 'WF'

    SERVICE_CHOICES =(
    (LAUNDRY, 'Laundry'),
    (ROOMS, 'Rooms'),
    (WIFI, 'Wifi'),
    )
    service_type = models.CharField(max_length=10, choices=SERVICE_CHOICES)
    rooms = models.ForeignKey(Room,on_delete=models.CASCADE, null=True,blank=True)
    # visitor = models.ForeignKey(Visitor,on_delete=models.CASCADE, null=True,blank=True)
class Transaction(models.Model):
    service = models.ForeignKey(Service,on_delete=models.CASCADE, null=True,blank=True)
    rooms = models.ForeignKey('Room',on_delete=models.CASCADE, null=True,blank=True)
    amount = models.DecimalField(max_digits=6, decimal_places=2)