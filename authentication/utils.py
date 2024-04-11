from django.conf import settings
from django.core.mail import EmailMessage
from django.urls import reverse
from django.utils.encoding import force_bytes
from django.utils.http import urlsafe_base64_encode


class Utils:
    @staticmethod
    def email_sender(data):
        email = EmailMessage(subject=data['email_subject'], body=data['email_body'], from_email=data['from_email'],
                             to=(data['to_email'],))
        email.send()

    @staticmethod
    def send_verification_email(domain, user):
        current_site = domain
        uidb64 = urlsafe_base64_encode(force_bytes(user.pk))
        verification_link = reverse('authentication:email_verify', args=(uidb64,))
        absurl = f"http://{current_site}{verification_link}"
        from_email = settings.EMAIL_HOST_USER
        email_body = f'Hello {user.username} Use link below to verify your account\n {absurl}'
        data = {'to_email': user.email,
                'from_email': from_email,
                'email_body': email_body,
                'email_subject': "Email verification"}
        Utils.email_sender(data)
