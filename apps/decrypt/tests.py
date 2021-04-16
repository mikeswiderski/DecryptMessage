from django.urls import reverse
from rest_framework import status
from rest_framework.test import APIClient, APITestCase


class DecryptTests(APITestCase):

    def setUp(self):
        self.client = APIClient()

        self.decrypt = reverse('decrypt')

    def test_webservice_only_takes_POST_requests(self):
        response = self.client.get(self.decrypt, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.put(self.decrypt, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.patch(self.decrypt, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

        response = self.client.delete(self.decrypt, format='json')
        self.assertEqual(response.status_code, status.HTTP_405_METHOD_NOT_ALLOWED)

    def test_webservice_can_dectrypt_message_when_correct_parameters_provided(self):
        data = {"passphrase": "topsecret",
                "message": "-----BEGIN PGP MESSAGE-----\nVersion: GnuPG v2\n\njA0ECQMCVady3RUyJw3X0kcBF"\
                           "+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\npEoI2S82cDiCNBIVAYWB8WKPtH2R2YSuss"\
                           "KhpSJ4mFgqyOA01uwroA==\n=KvJQ\n-----END PGP MESSAGE-----"}
        response = self.client.post(self.decrypt, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_200_OK)

    def test_webservice_can_not_dectrypt_message_when_passphrase_parameter_not_provided(self):
        data = {"message": "-----BEGIN PGP MESSAGE-----\nVersion: GnuPG v2\n\njA0ECQMCVady3RUyJw3X0kcBF"\
                "+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\npEoI2S82cDiCNBIVAYWB8WKPtH2R2YSuss"\
                "KhpSJ4mFgqyOA01uwroA==\n=KvJQ\n-----END PGP MESSAGE-----"}
        response = self.client.post(self.decrypt, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_webservice_can_not_dectrypt_message_when_message_parameter_not_provided(self):
        data = {"passphrase": "topsecret"}
        response = self.client.post(self.decrypt, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_webservice_can_not_dectrypt_message_when_wrong_parameter_provided(self):
        data = {"passphrase": "secret",
                "message": "-----BEGIN PGP MESSAGE-----\nVersion: GnuPG v2\n\njA0ECQMCVady3RUyJw3X0kcBF"\
                           "+zdkfZOMhISoYBRwR3uk3vNv+TEg+rJnp4/yYIS\npEoI2S82cDiCNBIVAYWB8WKPtH2R2YSuss"\
                           "KhpSJ4mFgqyOA01uwroA==\n=KvJQ\n-----END PGP MESSAGE-----"}
        response = self.client.post(self.decrypt, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)

    def test_webservice_can_not_dectrypt_message_when_no_parameters_provided(self):
        data = {}
        response = self.client.post(self.decrypt, data, format='json')
        self.assertEqual(response.status_code, status.HTTP_400_BAD_REQUEST)
