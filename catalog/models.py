from django.db import models

# Create your models here.
class Brand(models.Model):
    """
    Model representing a book genre (e.g. Science Fiction, Non Fiction).
    """
    name = models.CharField(max_length=200, help_text="Enter a dress brand (e.g. Chanel, Versace etc.)")
    
    def __str__(self):
        """
        String for representing the Model object (in Admin site etc.)
        """
        return self.name

from django.urls import reverse #Used to generate URLs by reversing the URL patterns

class Dress(models.Model):
    """
    Model representing a book (but not a specific copy of a book).
    """
    title = models.CharField(max_length=200)
    guest = models.ForeignKey('guest', on_delete=models.SET_NULL, null=True)
    # Foreign Key used because dress can only have one guest, but guests can have multiple dress
    # Guest as a string rather than object because it hasn't been declared yet in the file.
    summary = models.TextField(max_length=1000, help_text="Enter a brief description of the dress")
    price = models.CharField('PRICE',max_length=13, help_text='13 Character <a href="https://www.isbn-international.org/content/what-isbn">ISBN number</a>')
    brand = models.ManyToManyField(Brand, help_text="Select a brand for this dress")
    # ManyToManyField used because brand can contain many dress. Dress can cover many brands.
    # Brand class has already been defined so we can specify the object above.
    


    def display_brand(self):
        """
        Creates a string for the Brand. This is required to display genre in Admin.
        """
        return ', '.join([ brand.name for brand in self.brand.all()[:3] ])
    display_brand.short_description = 'brand'
    
    def __str__(self):
        """
        String for representing the Model object.
        """
        return self.title
    
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular book instance.
        """
        return reverse('dress-detail', args=[str(self.id)])
import uuid # Required for unique dress instances

class DressInstance(models.Model):
    """
    Model representing a specific copy of a book (i.e. that can be borrowed from the library).
    """
    id = models.UUIDField(primary_key=True, default=uuid.uuid4, help_text="Unique ID for this particular book across whole library")
    dress = models.ForeignKey('Dress', on_delete=models.SET_NULL, null=True) 
    size = models.CharField(max_length=200)
    due_back = models.DateField(null=True, blank=True)

    LOAN_STATUS = (
        ('m', 'Summer'),
        ('o', 'Spring'),
        ('a', 'Winter'),
        ('r', 'Autumn'),
    )

    status = models.CharField(max_length=1, choices=LOAN_STATUS, blank=True, default='d', help_text='Dress season')

    class Meta:
        ordering = ["due_back"]
        

    def __str__(self):
        """
        String for representing the Model object
        """
        return '%s (%s)' % (self.id,self.dress.title)

class Guest(models.Model):
    """
    Model representing an author.
    """
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    order_date= models.DateField(null=True, blank=True)
    availability_date = models.DateField('Ready', null=True, blank=True)
    
    def get_absolute_url(self):
        """
        Returns the url to access a particular author instance.
        """
        return reverse('guest-detail', args=[str(self.id)])
    

    def __str__(self):
        """
        String for representing the Model object.
        """
        return '%s, %s' % (self.last_name, self.first_name)