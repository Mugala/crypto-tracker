from django.db import models
from django.contrib.auth.models import User

# Create your models here.

'''
This model will allow the admin to be able to send news letters to the subscribers of the 
application.
'''

class NewsLetterRecipient (models.Model):
    name = models.CharField(max_length=30)
    email = models.EmailField()

'''
This class model will be used to store user profiles

'''

class Profile (models.Model):
    user = models.ForeignKey(User,on_delete=models.CASCADE)
    first_name = models.CharField(max_length =30)
    last_name = models.CharField(max_length =30)
    email = models.EmailField()
    bio = models.CharField(max_length =200)
    pub_date = models.DateTimeField(auto_now_add=True)
    default_pic = models.ImageField(upload_to = 'pro-photos/', null=True)

    def __str__(self):
        return self.first_name

    def save_profile(self):
        self.save()

    def delete_profile(self):
        self.delete()

    @classmethod
    def user_details(cls):
        user_details = cls.objects.all()
        return user_details
    
    @classmethod
    def update_profile(cls, profile_id, **kwargs):
        rows = 0
        if kwargs is not None:
            rows = cls.objects.filter(id = profile_id).update(**kwargs)

        return rows

    class Meta:
        ordering = ['first_name']


class Currency:

    def __init__(self,id):

        self.id=id    
        

class Currency_details:

    def __init__(self,id,name,symbol,price,rank,total_supply,max_supply,percent_change_24h):

        self.id=id
        self.name=name
        self.symbol=symbol
        self.rank=rank        
        self.price=price
        self.total_supply=total_supply
        self.max_supply=max_supply
        self.percent_change_24h=percent_change_24h

class Article:
    """
    Defines what we want our articles object to look like
    """

    def __init__(self,id,name,author,title,description,url,urlToImage,publishedAt):
        self.id = id
        self.name = name
        self.author = author
        self.title = title
        self.description = description
        self.url = url
        self.urlToImage = urlToImage
        self.publishedAt = publishedAt


