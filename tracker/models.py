from django.db import models

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
    def update_profile(cls, profile_id, **kwargs):
        rows = 0
        if kwargs is not None:
            rows = cls.objects.filter(id = profile_id).update(**kwargs)

        return rows

    class Meta:
        ordering = ['first_name']

