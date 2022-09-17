from django.db import models
from django.utils import timezone

# Create your models here.
""" Model
 Callsign = string
 name = string
 date = datetime
 country = optional string
 state =  optional string
 mode = optional string
 frequency = float
 band = string
 notes = text
 
 
 
 
 """


class Contact(models.Model):
    DMR = 'DMR'
    CW = 'CW'
    AM = 'AM'
    FM = 'FM'
    RTTY = 'RTTY'
    FT8 = 'FT8'
    SSTV = 'SSTV'
    C4FM = 'C4FM'
    JS8 = 'JS8'
    FT4 = 'FT4'
    PSK31 = 'PSK31'
    DSTAR = 'DSTAR'
    SSB = 'SSB'

    MODE_CHOICES = [(DMR, 'DMR'), (SSB, 'SSB'), (CW, 'CW'), (AM, 'AM'), (FM, 'FM'), (RTTY, 'RTTY'), (FT8, 'FT8'),
             (SSTV, 'SSTV'), (C4FM, 'C4FM'),
             (JS8, 'JS8'), (FT4, 'FT4'), (PSK31, 'PSK31'), (DSTAR, 'DSTAR'), (SSB, 'SSB')

             ]
    callsign = models.CharField(max_length=10, null=False, unique=True)
    name = models.CharField(max_length=20, null=True)
    country = models.CharField(max_length=20, null=True)
    state = models.CharField(max_length=40, null=True)
    mode = models.CharField(max_length=10,choices=MODE_CHOICES,default=AM)
    freq = models.FloatField
    power = models.IntegerField(max_length=4)
    created_at = models.DateTimeField(default=timezone.now())

    def __str__(self) -> str:
        return self.callsign
