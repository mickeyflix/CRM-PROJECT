from django.contrib import admin
from .models import client
# Register your models here.
from django.shortcuts import reverse
from django.utils.safestring import mark_safe


class clientAdmin(admin.ModelAdmin):
    model=client
    list_display=['id','name','email','courseinterest','claim_here']
    def claim_here(self,obj):
        return mark_safe("<a href='{link}'>Claim here</a>".format(link=reverse('clientdetails:claim_here', args=[obj.id])))


admin.site.register(client,clientAdmin)