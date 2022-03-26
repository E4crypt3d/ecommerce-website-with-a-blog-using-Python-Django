from email.policy import default
from django.db import models

# Create your models here.


class BlogPost(models.Model):
    post_id = models.AutoField(primary_key=True)
    title = models.CharField(max_length=60)
    head0 = models.CharField(max_length=60)
    chead0 = models.TextField(max_length=1500)
    head1 = models.CharField(max_length=60)
    chead1 = models.TextField(max_length=1500)
    head2 = models.CharField(max_length=60)
    chead2 = models.TextField(max_length=1500)
    pub_date = models.DateField()

    class categories(models.TextChoices):
        Design = 'Design', ('Design')
        World = 'World', ('World')
        Education = 'Eduction', ('Eduction')
        Art = 'Art', ('Art')
        History = 'History', ('History')
        Random = 'Random', ('Random')
    category = models.CharField(max_length=15, choices=categories.choices, default=categories.Random)
    thumbnail = models.ImageField(upload_to='buybest/images', default='')
    posted_by = models.CharField(max_length=25)

    def __str__(self):
        return self.title
