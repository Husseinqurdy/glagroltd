from django.db.models.signals import post_save
from django.dispatch import receiver
from django.core.mail import send_mail
from .models import FertilizerOrder

@receiver(post_save, sender=FertilizerOrder)
def notify_admin_on_order(sender, instance, created, **kwargs):
    if created:
        subject = f"New Order: {instance.fertilizer.name_sw}"
        message = f"""
Mteja: {instance.customer_name}
Simu: {instance.phone_number}
Location: {instance.location}
Quantity: {instance.quantity}
Notes: {instance.notes}
"""
        send_mail(
            subject,
            message,
            "qurdy@umemeswahili.co.tz",  # from_email (email yako ya domain)
            ["mwajumarashid2001@gmail.com"],  # recipient_list (admin email)
            fail_silently=False,
        )
