from django.db import models


# Create your models here.
class Blog(models.Model):
    title = models.CharField(max_length=250)
    pub_date = models.DateTimeField()
    body_context = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='images/')

    # Changes the object name in the admin panel for ease of location object
    def __str__(self):
        return self.title

    def summary(self):
        return self.body_context[:50]

    def pub_date_cleaned(self):
        return self.pub_date.strftime('%b %e, %Y')
