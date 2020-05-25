from django.contrib import admin
from .models import Owner, Prop_Name, Reserve, Room_Info

# Register your models here.
admin.site.register(Owner)
admin.site.register(Prop_Name)
admin.site.register(Reserve)
admin.site.register(Room_Info)
