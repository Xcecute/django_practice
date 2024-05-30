from django.db import models

class Experiment(models.Model):
    project_code = models.CharField(max_length=20)
    visit_date = models.DateField()

    def __str__(self):
        return self.project_code

class Sample(models.Model):
    experiment = models.ForeignKey(Experiment, related_name='samples', on_delete=models.CASCADE)
    name = models.CharField(max_length=100)
    quantity = models.CharField(max_length=100)

    def __str__(self):
        return f"{self.name} - {self.quantity}"
