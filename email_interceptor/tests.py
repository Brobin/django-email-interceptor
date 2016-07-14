from django.conf import settings
from django.core.mail import send_mail
from django.test import TestCase
from django.test.utils import override_settings

from mock import patch


@override_settings(EMAIL_BACKEND='email_interceptor.backends.LocMemInterceptorBackend')
class EmailInterceptorBackendTestCase(TestCase):
    """Email Intercept Backend Test Case

    Our test case for the Intercept backend. We are going to override
    the EMAIL_BACKEND to use our implementation of the Local Memory
    backend so we can successfull run tests.
    """

    @override_settings(INTERCEPTOR_EMAIL='text@example.com')
    @patch('email_interceptor.backends.log')
    def test_interceptor_send_mail(self, log):
        """Test intercept send_mail

        Test that the intercept backend is called correctly
        and logs that our email was intercepted and sent to
        'test@test.com' as specified in the INTERCEPTOR_EMAIL
        setting.
        """
        to = ['asdf@asdf.com']
        success = send_mail('test', 'test', 'admin@admin.com', to)
        self.assertTrue(success)
        expect = [settings.INTERCEPTOR_EMAIL]
        message = 'email to {0} intercepted by {1}'.format(to, expect)
        log.info.assert_called_with(message)

    @patch('email_interceptor.backends.log')
    def test_interceptor_send_mail_intercept_fail(self, log):
        """Test intercept send_mail fail

        Test that if we try to use our backend without the
        INTERCEPTOR_EMAIL set, we will get an AttributeError.
        """
        to = ['test@test.com']
        self.assertRaises(AttributeError, send_mail, 'test',
                          'test', 'test@test.com', to)
