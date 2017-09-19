from django.db import models
from django.utils import timezone
from django.core.urlresolvers import reverse
# Create your models here.


class Post(models.Model):
    author=models.ForeignKey('auth.User') # a blog is basically a one user(superuser) site thus linking to it
    title= models.CharField(max_length=264)
    text=models.TextField()
    create_date = models.DateTimeField(default=timezone.now)# note that default is set to a function not the call of the function as in .now()
    published_date =models.DateTimeField(blank=True,null=True)
    
    def publish(self):
        self.published_date =timezone.now()
        self.save()
        
    def approve_comments(self):
        return self.comments.filter(approved_comment=True)
    
    
    def get_absolute_url(self):
        return reverse('post_detail',kwargs={'pk':self.pk})
    
    def __str__(self):
        return self.title
    
    
class Comment(models.Model):
    post=models.ForeignKey('blog.Post',related_name='comments')
    author =models.CharField(max_length=200)
    text = models.TextField()
    create_date =models.DateTimeField(default=timezone.now)
    approved_comment = models.BooleanField(default=False)
    
    
    def approved(self):
        self.approved_comment=True
        
    def get_absolute_url(self):
        return reverse('post_list') # or just return given post_detail?
        
    def __str__(self):
        return self.text
    
        
    
    
