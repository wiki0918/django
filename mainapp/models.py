from django.db import models


class Article(models.Model):
    aid = models.AutoField(primary_key=True)
    title = models.TextField()
    content = models.TextField(blank=True, null=True)
    url = models.TextField()
    bid = models.TextField()
    article_type = models.TextField(blank=True, null=True)
    article_space = models.TextField(blank=True, null=True)
    date = models.DateField(blank=True, null=True)
    create_time = models.DateField(blank=True, null=True)
    mod_time = models.DateField(blank=True, null=True)

    class Meta:
        managed = False
        db_table = 'article'

class Blog(models.Model):
    bid = models.AutoField(primary_key=True)
    blog_name = models.TextField()
    blog_url = models.TextField()
    blog_link = models.TextField()
    blog_type = models.TextField()
    invest_type = models.CharField(max_length=20)
    priority = models.CharField(max_length=20)
    status = models.CharField(max_length=20)

    class Meta:
        managed = False
        db_table = 'blog'

#class DjangoSession(models.Model):
#    session_key = models.CharField(primary_key=True, max_length=40)
#    session_data = models.TextField()
#    expire_date = models.DateTimeField()
#
#    class Meta:
#        managed = False
#        db_table = 'django_session'


class StockNum(models.Model):
    stock_num = models.IntegerField()
    stock_name = models.TextField()
    stock_type = models.TextField()
    stock_market = models.TextField()
    stock_group = models.IntegerField()

    class Meta:
        managed = False
        db_table = 'stock_num'


class User(models.Model):
    uid = models.AutoField(primary_key=True)
    email = models.TextField()
    password = models.TextField()
    name = models.TextField()
    create_time = models.DateTimeField()

    class Meta:
        app_label = 'mysql'
        managed = False
        db_table = 'user'
        
    def __unicode__(self):
        return self.name