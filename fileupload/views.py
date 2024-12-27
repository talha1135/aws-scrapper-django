from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import FileResponse
from .controllers import FileController
import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse

class FileUploadView(APIView):
    def post(self, request):
        file = request.FILES.get('file')
        if not file:
            return Response({'error': 'No file provided.'}, status=400)

        controller = FileController(file)
        is_valid, error_message = controller.validate_file()
        if not is_valid:
            return Response({'error': error_message}, status=400)

        file_path = controller.save_file()
        processed_file_path = controller.process_file(file_path)

        return Response({
            'success': True,
            'message': 'File uploaded and processed successfully.',
            'downloadLink': os.path.basename(processed_file_path),
        }, status=200)


class FileDownloadView(APIView):
    def get(self, request, filename):
        file_path = os.path.join(settings.MEDIA_ROOT, 'uploads', filename)
        if os.path.exists(file_path):
            return FileResponse(open(file_path, 'rb'), as_attachment=True, filename=filename)
        return Response({'error': 'File not found.'}, status=404)


# View to serve the HTML page
def serve_html(request):
    # Define the path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    # Open and read the HTML file content
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    # Return the HTML content as an HttpResponse
    return HttpResponse(html_content)
