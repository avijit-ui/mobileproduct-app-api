from django.db import models




class Mobile(models.Model):
        POCOX3 = 'PC'
        RealmeNarzo20 = 'RLME'
        EcotelE17 = 'ETEL'
        Redmi9i = "RD9"
        InfinixSmart4Plus ="INFS4"
        mobile_types = [
        (POCOX3, 'POCO X3'),
        (RealmeNarzo20, 'Realme Narzo 20'),
        (EcotelE17, 'Ecotel E17'),
        (Redmi9i, 'Redmi 9i'),
        (InfinixSmart4Plus, 'Infinix Smart 4 Plus'),
      ]
        Mobile_short = [
              ('PC', 'POCO X3'),
              ('RLME', 'Realme Narzo 20'),
              ('ETEL', ' Ecotel E17 '),
              ('"RD9', 'Redmi 9i'),
              ('INFS4', ' Infinix Smart 4 Plus'),
    
]

        Mobile_type = models.CharField(
             max_length=5,
             choices=mobile_types,
             default=POCOX3,
        )
        Highlights = models.TextField()
        price = models.DecimalField(decimal_places=2, max_digits=20)
        image = models.ImageField(upload_to='images/')
