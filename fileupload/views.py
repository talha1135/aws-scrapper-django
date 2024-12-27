import os
from django.conf import settings
from django.shortcuts import render
from django.http import HttpResponse



# View to serve the HTML page
def serve_html(request):
    # Define the path to the HTML file
    file_path = os.path.join(os.path.dirname(__file__), 'index.html')
    
    # Open and read the HTML file content
    with open(file_path, 'r') as file:
        html_content = file.read()
    
    # Return the HTML content as an HttpResponse
    return HttpResponse(html_content)
