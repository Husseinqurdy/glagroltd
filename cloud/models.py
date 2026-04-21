from django.db import models
from cloudinary.models import CloudinaryField   
from django.contrib.auth.models import User

class PasswordResetToken(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    token = models.CharField(max_length=100, unique=True)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.user.username} - {self.token}"


class Fertilizer(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usage_time = models.CharField(max_length=100, blank=True, null=True)
    image = CloudinaryField('fertilizer_image', blank=True, null=True)  
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name

class FertilizerOrder(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE, related_name="orders")
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    quantity = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('unread', 'Unread'), ('read', 'Read')],
        default='unread'
    )

    def __str__(self):
        return f"Order of {self.quantity} {self.fertilizer.name} by {self.customer_name}"


class Seed(models.Model):
    name = models.CharField(max_length=100)
    description = models.TextField()
    usage_time = models.CharField(max_length=200)
    image = CloudinaryField('seed_image')  
    price = models.DecimalField(max_digits=10, decimal_places=2)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.name


class SeedOrder(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('unread', 'Unread'), ('read', 'Read')],
        default='unread'
    )
    def __str__(self):
        return f"Order by {self.customer_name} - {self.seed.name} ({self.location})"


class FarmManagementService(models.Model):
    service_name = models.CharField(max_length=100)
    description = models.TextField()
    image = CloudinaryField('service_image')  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.service_name


class FarmServiceReport(models.Model):
    service = models.ForeignKey(FarmManagementService, on_delete=models.CASCADE, related_name='reports')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    before_description = models.TextField()
    before_image = CloudinaryField('before_image', blank=True, null=True)  
    after_description = models.TextField()
    after_image = CloudinaryField('after_image', blank=True, null=True)    
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report by {self.farmer_name} - {self.service.service_name}"


class FarmServiceOrder(models.Model):
    service = models.ForeignKey(FarmManagementService, on_delete=models.CASCADE, related_name='orders')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('unread', 'Unread'), ('read', 'Read')],
        default='unread'
    )
    
    def __str__(self):
        return f"Order by {self.farmer_name} - {self.service.service_name} ({self.location})"


class ExpertConsultation(models.Model):
    topic = models.CharField(max_length=150)
    description = models.TextField()
    image = CloudinaryField('consultation_image', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.topic


class ConsultationOrder(models.Model):
    consultation = models.ForeignKey(ExpertConsultation, on_delete=models.CASCADE, related_name='orders')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    question = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    status = models.CharField(
        max_length=20,
        choices=[('unread', 'Unread'), ('read', 'Read')],
        default='unread'
    )
    
    def __str__(self):
        return f"Consultation: {self.farmer_name} - {self.consultation.topic}"


class FarmerBlog(models.Model):
    title = models.CharField(max_length=200)
    content = models.TextField()
    author = models.CharField(max_length=100)
    image = CloudinaryField('blog_image', blank=True, null=True)  
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return self.title
