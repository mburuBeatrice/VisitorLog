from django.db import models

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    
    def create_visitor(self):
        return self.save()

    def delete_visitor(self):
        return self.delete()
    # @classmethod
    # def update_visitor


