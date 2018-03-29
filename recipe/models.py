from django.db import models

class Recipe(models.Model):
    title = models.CharField(max_length=100)
    image_path = models.TextField(max_length=100)
    decscription = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    class Meta:
        managed = False
        db_table = 'recipe'
        
    def __str__(self):
        return self.name