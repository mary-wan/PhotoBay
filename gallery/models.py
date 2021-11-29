from django.db import models

class Location(models.Model):
    name = models.CharField(max_length=100)
    
    def save_location(self):
        self.save()

    def delete_location(self):
        self.delete()
    
    @classmethod
    def all_locations(cls):
        locations = Location.objects.all()
        return locations

    @classmethod   
    def update_location(cls, id, name):
        cls.objects.filter(id=id).update(name=name)

    def __str__(self):
        return self.name
    
class Category(models.Model):
    name = models.CharField(max_length=100)

    def save_category(self):
        self.save()

    def delete_category(self):
        self.delete()
     
    @classmethod   
    def update_category(cls, id, name):
        cls.objects.filter(id=id).update(name=name)
        
    def __str__(self):
        return self.name
      
class Image(models.Model):
    image = models.ImageField(upload_to='images/')
    description = models.TextField()
    name = models.CharField(max_length=200)
    upload_date = models.DateTimeField(auto_now_add=True)
    category = models.ForeignKey(Category,on_delete=models.CASCADE)
    location = models.ForeignKey(Location,on_delete=models.CASCADE)
    
    def save_image(self):
        self.save()

    def delete_image(self):
        self.delete()
        
    @classmethod
    def update_image(cls, id ,image, description , name,category,location):
        cls.objects.filter(id = id).update(image=image,description=description,name=name,category=category,location=location)

        
    # @classmethod
    # def update_image(cls, id ,image):
    #     cls.objects.filter(id = id).update(image=image)
        
    @classmethod
    def get_image_by_id(cls,id):
        image =cls.objects.filter(id= id).first()
        return image
    
    @classmethod
    def search_image(cls, search_category):
        images = cls.objects.filter(category__name__icontains=search_category)
        return images
    
    @classmethod
    def filter_by_location(cls,search_location):
        location = cls.objects.filter(location__name=search_location).all()
        return location
    

    

    