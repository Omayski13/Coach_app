from asgiref.sync import async_to_sync
from django.contrib.auth import get_user_model
from django.core.mail import send_mail
from django.db.models.signals import post_save
from django.dispatch import receiver

from coach_app.accounts.models import Profile
from coach_app.settings import COMPANY_EMAIL

UserModel = get_user_model()

async def async_send_mail(subject, message, from_email, recipient_list):
    send_mail(
        subject=subject,
        message=message,
        from_email=from_email,
        recipient_list=recipient_list,
        fail_silently=False,
    )

@receiver(post_save, sender=UserModel)
def create_profile(sender, instance, created, **kwargs):
    if created:
        Profile.objects.create(user=instance)
        async_to_sync(async_send_mail)(
            subject='Добре дошъл, тренер',
            message=f'Здравей, тренер {instance.username}!\n\nБлагодаря за регистрацията!\nВече можеш да използваш всички функции на BG Football Trener.',
            from_email=COMPANY_EMAIL,
            recipient_list=[instance.email],
        )
