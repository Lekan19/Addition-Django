from django.db import models

# Create your models here.
class InputNum(models.Model):
    first_num  = models.FloatField()
    second_num = models.FloatField()
    date    = models.DateField(auto_now_add=True)

    def __str__(self):
        return f"InputNum({self.first_num}, {self.second_num})"