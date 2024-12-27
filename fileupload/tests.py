from rest_framework.test import APITestCase
from django.urls import reverse
from io import BytesIO
from django.core.files.uploadedfile import SimpleUploadedFile

class FileUploadTests(APITestCase):
    def test_upload_file(self):
        url = reverse('file-upload')
        file = SimpleUploadedFile("test.xlsx", b"dummy data")
        response = self.client.post(url, {'file': file})
        self.assertEqual(response.status_code, 200)

    def test_download_file(self):
        url = reverse('file-download', args=['test.xlsx'])
        response = self.client.get(url)
        self.assertIn(response.status_code, [200, 404])
