from django.db import models
from django.utils.text import slugify

# Create your models here.
class Owner(models.Model):
    username = models.CharField(max_length=100, unique =True)
    def __str__(self):
        return self.username

class Prop_Name(models.Model):
    prop_name = models.CharField(max_length=100, unique=True)
    owner = models.ForeignKey(Owner, on_delete=models.CASCADE, related_name= 'properties')
    def __str__(self):
        return self.prop_name

#normal models
class Reserve(models.Model):
    name = models.CharField(max_length=100, default="default")
    def __str__(self):
        return self.name
    IN_direction = "IN"
    OUT_direction = "OUT"
    DIRECTION_CHOICES = [
        (IN_direction,"IN"),
        (OUT_direction,"OUT")
    ]
    date = models.DateField()
    direction =  models.CharField(
        max_length=3,
        choices=DIRECTION_CHOICES,
        default = IN_direction
    )
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=100)
    prop_name = models.ForeignKey(Prop_Name, on_delete=models.CASCADE)

class Room_Info(models.Model):
    room_no = models.IntegerField()
    def __str__(self):
        return "{}-{}".format(str(self.room_no),self.name)
    name = models.CharField(max_length=100)
    email = models.CharField(max_length=100,unique = True)
    phone_no = models.CharField(max_length=16,unique = True)
    
    rent = models.IntegerField()
    key_deposit = models.IntegerField()
    last_month = models.IntegerField()
    active_room = models.BooleanField(default=True)
    
    prop_name = models.ForeignKey(Prop_Name, on_delete=models.CASCADE)

class Expenses(models.Model):
    name = models.CharField(max_length=100,default="default")
    def __str__(self):
        return self.name
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=200)
    room_no = models.ForeignKey(Room_Info, on_delete=models.CASCADE,related_name= 'expenses')
    prop_name = models.ForeignKey(Prop_Name, on_delete=models.CASCADE, related_name= 'expenses')

class Earnings(models.Model):
    name = models.CharField(max_length=100,default="default")
    def __str__(self):
        return self.name
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=200)
    room_no = models.ForeignKey(Room_Info, on_delete=models.CASCADE,related_name= 'earnings')
    prop_name = models.ForeignKey(Prop_Name, on_delete=models.CASCADE,related_name= 'earnings')

class Room_Transactions(models.Model): 
    name = models.CharField(max_length=100,default="default")
    def __str__(self):
        return self.name
    
    date = models.DateField()
    amount = models.DecimalField(max_digits=8, decimal_places=2)
    comment = models.CharField(max_length=100)
    prop_name = models.ForeignKey(Prop_Name,on_delete=models.CASCADE,related_name='reserves' )
    room_no = models.ForeignKey(Room_Info, on_delete=models.CASCADE)





