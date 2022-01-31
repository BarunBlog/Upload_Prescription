from django.contrib import admin
from .models import Upload_Prescription


class Upload_Prescription_Admin(admin.ModelAdmin):

    list_display =('id','phone','name','delivary', 'store', )
    

    """def save_model(self, request, obj, form, change):
        update_fields = []
        print(obj)
        if change: 
            for key, value in form.cleaned_data.items():
                # True if something changed in model
                print(key, value)
                if value != form.initial[key]:
                    update_fields.append(key)
        else:
            #update_fields.append('id') # primary key
            for key, value in form.cleaned_data.items():
                update_fields.append(key)

        obj.save(update_fields=update_fields)"""


admin.site.register(Upload_Prescription, Upload_Prescription_Admin)
