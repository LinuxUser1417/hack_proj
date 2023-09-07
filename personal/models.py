from django.db import models

class Favorite(models.Model):
    product_id = models.IntegerField()
    user_id = models.IntegerField()

    def __str__(self):
        return str(self.product_id) + " " + str(self.user_id)
    
class RatingForUser(models.Model):
    name = models.CharField(max_length=255)


