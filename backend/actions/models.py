from django.db import models
from django.core.validators import MinValueValidator, MaxValueValidator


class Ratings(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    rating = models.DecimalField(null=True, max_digits=2, decimal_places=1,
                        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return '%s - %s - %s' % (self.user, self.game, self.rating)

    class Meta:
        unique_together = ['game', 'user']
        

class Journal(models.Model):
    game = models.ForeignKey('games.Game', on_delete=models.CASCADE)
    user = models.ForeignKey('users.CustomUser', on_delete=models.CASCADE)
    date = models.DateField()
    review = models.TextField(null=True)
    spoilers = models.BooleanField(null=True)
    liked = models.BooleanField(null=True)
    rating = models.DecimalField(null=True, max_digits=2, decimal_places=1,
                        validators=[MinValueValidator(0), MaxValueValidator(5)])

    def __str__(self):
        return '%s - %s - %s' % (self.date, self.game, self.user)
