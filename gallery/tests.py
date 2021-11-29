from django.test import TestCase
from .models import Image,Location,Category
class CategoryTestClass(TestCase):

    def setUp(self):
        self.category = Category(name="travel")
        self.category.save_category()

    def test_instance(self):
        self.assertTrue(isinstance(self.category, Category))

    def test_save_method(self):
        self.category.save_category()
        category = Category.objects.all()
        self.assertTrue(len(category) > 0)

    def test_delete_method(self):
        self.category.save_category()
        self.category.delete_category()
        search_category = Category.objects.all()
        self.assertTrue(len(search_category) == 0)

    def test_update_category(self):
        changed_location = 'Food'
        self.category.update_category(self.category.id, changed_location)
        changed_location = Category.objects.filter(name='Food')
        self.assertTrue(len(changed_location) == 1)
    
    
class LocationTestCLass(TestCase):
  
    def setUp(self):
        self.location = Location(name="Paris")
        self.location.save_location()

    def test_instance(self):
        self.assertTrue(isinstance(self.location,Location))

    def test_save_location(self):
        self.location.save_location()
        locations = Location.objects.all()
        self.assertTrue(len(locations) > 0)

    def test_delete_location(self):
        self.location.save_location()
        self.location.delete_location()
        location = Location.objects.all()
        self.assertTrue(len(location) == 0)
        
    def test_update_location(self):
        changed_location = 'USA'
        self.location.update_location(self.location.id, changed_location)
        changed_location = Location.objects.filter(name='USA')
        self.assertTrue(len(changed_location) == 1)

class ImageTestClass(TestCase):

    def setUp(self):
        self.location = Location(name="Paris")
        self.location.save_location()
        
        self.category = Category(name="travel")
        self.category.save_category()

        self.image = Image(id=1,name='image test', description='my test',category=self.category,location=self.location)
        self.image.save_image()

    def test_instance(self):
        self.assertTrue(isinstance(self.image, Image))

    def tearDown(self):
        self.image.delete_image()
        self.category.delete_category()
        self.location.delete_location()


    def test_save_method(self):
        self.image.save_image()
        images  = Image.objects.all()
        self.assertTrue(len(images)>0)
        
    def test_get_image_by_id(self):
        searched_image = self.image.get_image_by_id(self.image.id)
        image = Image.objects.filter(id=self.image.id)
        self.assertTrue(searched_image, image)
        
        
    def test_search_image_by_category(self):
        self.image.save_image()
        searched_images = self.image.search_image('travel')
        self.assertTrue(len(searched_images) >= 1)
    
    
    def test_search_image_by_location(self):
        self.image.save_image()
        searched_images = self.image.filter_by_location('Paris')
        self.assertTrue(len(searched_images) == 1)

        
    # def test_delete_image(self):
    #     self.image.save_image()
    #     self.image.delete_image()
    #     self.assertTrue(len(Image.objects.all()) == 0)

    # def test_update_image(self):
    #     self.image.save_image()
    #     self.image.update_image('pizza.jpg','testing change','2021-11-28','testing','food','Africa')
    #     updated_image=Image.objects.filter(image='pizza.jpg')
    #     self.assertTrue(len(updated_image) ==1)
