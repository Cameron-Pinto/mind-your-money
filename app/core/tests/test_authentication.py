from unittest.mock import patch
from django.test import TestCase
from django_recaptcha.client import RecaptchaResponse


class TestFields(TestCase):
    @patch("django_recaptcha.fields.client.submit")
    def test_client_success_response(self, mocked_submit):
        mocked_submit.return_value = RecaptchaResponse(is_valid=True)
