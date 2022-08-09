from django.db import models


class Ticket(models.Model):
    """
    A ticket is a record of a customer's request to get served.
    """
    number = models.IntegerField(default=100, unique=True)
    timestamp = models.DateTimeField(auto_now_add=True)
    wait = models.IntegerField(default=0) 
    called = models.BooleanField(default=False)
    counter = models.ForeignKey('Counter', on_delete=models.PROTECT, null=True)
    
    def __str__(self) -> str:
        return f'Ticket #{self.number}'


class Counter(models.Model):
    """
    A counter is assigned to one or more tickets.
    """
    counter_name = models.CharField(max_length=10, unique=True)

    def __str__(self) -> str:
        return self.counter_name
