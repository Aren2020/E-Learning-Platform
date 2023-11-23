from django.db import models
from django.core.exceptions import ObjectDoesNotExist

class OrderField(models.PositiveIntegerField):
    def __init__(self, for_fields = None, *args, **kwargs):
        self.for_fields = for_fields
        super().__init__(*args, **kwargs)

    def pre_save(self, model_instanse, add): # model_instanse экземляр класса модели
        if getattr(model_instanse, self.attname) is None: # self.attname имя поля в котором он будет храниться 
            try: 
                qs = self.model.objects.all()
                if self.for_fields:
                    query = {field: getattr(model_instanse,field) for field in self.for_fields} # field: Model.field
                    qs = qs.filter(**query) # qs.filter(field = (Model.field --> 14))
                last_item = qs.latest(self.attname) # if item: new_item.id = item.id + 1
                value = last_item.order + 1
            except ObjectDoesNotExist:
                value = 0 # No item in with your conditions 
            setattr(model_instanse, self.attname, value) # Model.attname = value
            return value
        else: # если объект уже сушествует
            super().pre_save(model_instanse, add)    
