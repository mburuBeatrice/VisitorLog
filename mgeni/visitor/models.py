from django.db import models
from django.core.urlresolvers import reverse

# Create your models here.
class Visitor(models.Model):
    name = models.CharField(max_length=40)

    def __str__(self):
        return self.name
    def get_absolute_url(self):
        return reverse("visitor:detail", kwargs={"id": self.id})
    class Meta:
        ordering = ["id"]
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
