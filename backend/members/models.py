from django.db import models

class Member(models.Model):
    first_name = models.CharField(max_length=100)  # Prénom
    last_name = models.CharField(max_length=100)   # Nom
    date_of_birth = models.DateField()             # Date de naissance
    cin = models.CharField(max_length=10, unique=True)  # CIN (Carte d'Identité Nationale)
    profession = models.CharField(max_length=150, blank=True)  # Profession
    address = models.TextField()                   # Adresse
    phone = models.CharField(max_length=15)        # Téléphone
    photo = models.ImageField(upload_to='member_photos/', blank=True, null=True)  # Photo
    date_joined = models.DateTimeField(auto_now_add=True)  # Date d'inscription
    sport_type = models.CharField(
        max_length=50,
        choices=[
            ('fitness', 'Fitness'),
            ('taekwando', 'Taekwando'),
            ('b', 'Boxing'),
            ('Aerobics', 'Aerobics'),
            ('fibox', 'fitBoxing'),
        ]
    )  # Type de sport

    def __str__(self):
        return f"{self.first_name} {self.last_name} ({self.cin})"
