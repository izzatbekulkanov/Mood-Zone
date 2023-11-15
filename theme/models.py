from django.db import models

# Create your models here.


class Theme(models.Model):
    VERTICAL = 'vertical'
    TWOCOLUMN = 'twocolumn'
    SEMIBOX = 'semibox'
    HORIZONTAL = 'horizontal'

    LAYOUT_CHOICES = [
        (VERTICAL, 'Vertical'),
        (TWOCOLUMN, 'Two Column'),
        (SEMIBOX, 'Semi Box'),
        (HORIZONTAL, 'Horizontal')
    ]

    data_layout = models.CharField(max_length=200, choices=LAYOUT_CHOICES, default=VERTICAL)




