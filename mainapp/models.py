from django.db import models


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    name = models.TextField()
    create_time = models.DateField()

    class Meta:
#        app_label = 'mysql'
        managed = False
        db_table = 'user'
        
    def __str__(self):
        return self.name