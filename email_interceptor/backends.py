import logging

from django.core.mail.backends.locmem import EmailBackend as LocMemEmailBackend
from django.core.mail.backends.smtp import EmailBackend
from django.conf import settings


log = logging.getLogger(__name__)


class EmailInterceptor(object):
    """Email Interceptor

    This mixin overrides the send_messages method found in EmailBackends
    and reroutes all messages to the email set in INTERCEPTOR_EMAIL
    """

    def __init__(self, *args, **kwargs):
        self.email = settings.INTERCEPTOR_EMAIL
        super(EmailInterceptor, self).__init__(*args, **kwargs)

    def send_messages(self, messages):
        """send messages

        Go through all of the messages to be send and override `to`
        with the INTERCEPTOR_EMAIL. Clear out cc and bcc so no more
        emails are sent.
        """
        to_send = []
        for message in messages:
            pre_intercept = message.to
            message.to, message.cc, message.bcc = [self.email], [], []
            log.info('email to {0} intercepted by {1}'.format(
                pre_intercept, message.to))
            to_send.append(message)
        return super(EmailInterceptor, self).send_messages(to_send) or 0


class SmtpInterceptorBackend(EmailInterceptor, EmailBackend):
    """Smtp Interceptor Backends

    Using the EmailIntercept, overrides the send_messages method
    of the Smtp backend.
    """
    pass


class LocMemInterceptorBackend(EmailInterceptor, LocMemEmailBackend):
    """LocMem Interceptor Backend

    Using the EmailIntercept, overrides the send_messages method
    of the Loc Mem Backend. Used primarily in testing as you can't
    connect to an SMTP server in testing environments
    """
    pass
