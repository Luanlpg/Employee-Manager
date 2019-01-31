from django.db import models


class Employee(models.Model):
    """
    Model de funcionário.
    """
    name = models.CharField(max_length=200, unique=True)
    email = models.CharField(max_length=200, unique=True)
    department = models.CharField(max_length=200)
    link = models.CharField(max_length=200, null=True)

    def save(self, *args, **kwargs):
        """
        Criação do link.
        """
        if self.link == None:
            self.link = 'http://localhost:8000/api/employee/'+self.name.replace(' ', '-')
        super(Employee, self).save(*args, **kwargs)
