from django.db import models

class Fertilizer(models.Model):
    # Basic info
    name_sw = models.CharField(max_length=100)   # Jina kwa Kiswahili
    name_en = models.CharField(max_length=100)   # Jina kwa Kiingereza

    description_sw = models.TextField()          # Maelezo kwa Kiswahili
    description_en = models.TextField()          # Maelezo kwa Kiingereza

    usage_time_sw = models.CharField(max_length=100, blank=True, null=True)
    usage_time_en = models.CharField(max_length=100, blank=True, null=True)

    image = models.ImageField(upload_to='fertilizers/', blank=True, null=True)
    price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.name_sw} / {self.name_en}"


class FertilizerOrder(models.Model):
    fertilizer = models.ForeignKey(Fertilizer, on_delete=models.CASCADE, related_name="orders")

    # Customer info
    customer_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    # Order details
    quantity = models.PositiveIntegerField()
    notes = models.TextField(blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order of {self.quantity} {self.fertilizer.name_sw} by {self.customer_name}"



class Seed(models.Model):
    name_sw = models.CharField(max_length=100)  # Jina la mbegu kwa Kiswahili
    name_en = models.CharField(max_length=100)  # Jina la mbegu kwa Kiingereza
    description_sw = models.TextField()         # Maelezo kwa Kiswahili
    description_en = models.TextField()         # Maelezo kwa Kiingereza
    usage_time_sw = models.CharField(max_length=200)  # Wakati wa matumizi kwa Kiswahili
    usage_time_en = models.CharField(max_length=200)  # Wakati wa matumizi kwa Kiingereza
    image = models.ImageField(upload_to='seeds/')     # Picha itahifadhiwa kwenye media/seeds/
    price = models.DecimalField(max_digits=10, decimal_places=2)  # Bei ya mbegu
    created_at = models.DateTimeField(auto_now_add=True)  # Wakati record inaundwa
    updated_at = models.DateTimeField(auto_now=True)      # Wakati record inabadilishwa

    def __str__(self):
        return f"{self.name_sw} / {self.name_en}"

 
class SeedOrder(models.Model):
    seed = models.ForeignKey(Seed, on_delete=models.CASCADE, related_name='orders')
    customer_name = models.CharField(max_length=100)
    customer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)   # Mahali pa mkulima
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order ya {self.customer_name} - {self.seed.name_sw} ({self.location})"



class FarmManagementService(models.Model):
    service_name_sw = models.CharField(max_length=100)   # Jina la huduma kwa Kiswahili
    service_name_en = models.CharField(max_length=100)   # Jina la huduma kwa Kiingereza
    description_sw = models.TextField()                  # Maelezo kwa Kiswahili
    description_en = models.TextField()                  # Maelezo kwa Kiingereza
    image = models.ImageField(upload_to='services/')     # Picha ya huduma (general branding)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.service_name_sw} / {self.service_name_en}"


class FarmServiceReport(models.Model):
    service = models.ForeignKey(FarmManagementService, on_delete=models.CASCADE, related_name='reports')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)

    # Taarifa kabla ya kusimamiwa
    before_description = models.TextField()
    before_image = models.ImageField(upload_to='farm_reports/before/', blank=True, null=True)

    # Taarifa baada ya kusimamiwa
    after_description = models.TextField()
    after_image = models.ImageField(upload_to='farm_reports/after/', blank=True, null=True)

    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Report ya {self.farmer_name} - {self.service.service_name_sw}"

class FarmServiceOrder(models.Model):
    service = models.ForeignKey(FarmManagementService, on_delete=models.CASCADE, related_name='orders')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)   # Mahali pa shamba
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Order ya {self.farmer_name} - {self.service.service_name_sw} ({self.location})"


class ExpertConsultation(models.Model):
    topic_sw = models.CharField(max_length=150)   # Mada ya ushauri kwa Kiswahili
    topic_en = models.CharField(max_length=150)   # Mada ya ushauri kwa Kiingereza
    description_sw = models.TextField()           # Maelezo kwa Kiswahili
    description_en = models.TextField()           # Maelezo kwa Kiingereza
    image = models.ImageField(upload_to='consultations/', blank=True, null=True)  # Picha ya mada
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f"{self.topic_sw} / {self.topic_en}"


class ConsultationOrder(models.Model):
    consultation = models.ForeignKey(ExpertConsultation, on_delete=models.CASCADE, related_name='orders')
    farmer_name = models.CharField(max_length=100)
    farmer_phone = models.CharField(max_length=20)
    location = models.CharField(max_length=200)
    question = models.TextField()   # Swali au changamoto ya mkulima
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"Ushauri: {self.farmer_name} - {self.consultation.topic_sw}"
