
# File Upload & Scraping Amazone Products - Django

This project is a simple web application that allows users to upload an Excel file, process it on the server, and download the processed file. The frontend is built using HTML, CSS, and JavaScript, while the backend is powered by Django.

## Product Details

The application enables the following:
1. **File Upload**: Users can upload `.xlsx` files (up to 10MB).
2. **Processing**: The server processes the file after it’s uploaded.
3. **File Download**: After processing, users can download the processed file.

### Features:
- **File Validation**: Ensures the uploaded file is an `.xlsx` file and does not exceed the size limit of 10MB.
- **User Feedback**: Displays a loading spinner while the file is being processed.
- **Error Handling**: Proper error messages in case of invalid file formats or sizes.
- **Download Link**: A link to download the processed file once it's ready.

## Problem Solved

This application solves the problem of:
- Allowing users to upload large `.xlsx` files and have them processed on the server without page reloads.
- Providing a simple interface for uploading and downloading files with real-time feedback (loading spinner).
- Validating the file format and size to ensure that only compatible files are processed.

## Tech Stack Used

- **Frontend**:
  - **HTML**: To structure the content of the page.
  - **CSS**: For styling the page and providing a user-friendly interface.
  - **JavaScript**: To handle the form submission, file validation, and interaction with the backend via AJAX (`fetch`).
  
- **Backend**:
  - **Django**: To handle the file upload, processing, and serve the processed file for download.
  
- **Packages**:
  - **Django**: The main framework used to build the web application. It provides a robust backend for handling requests, processing files, and serving responses.
  - **django-rest-framework**: Used for building REST APIs to handle file uploads and downloads.

## Libraries and Packages Used

### 1. **Django**
   - **Purpose**: Django is the primary backend framework for handling HTTP requests, file processing, and returning responses.
   - **Reason for Usage**: Django is robust, scalable, and includes built-in functionality for handling file uploads, making it ideal for this project.

### 2. **django-rest-framework**
   - **Purpose**: Helps to create RESTful APIs for file upload and download.
   - **Reason for Usage**: It simplifies the creation of APIs, and helps manage data serialization and HTTP responses efficiently.

### 3. **JavaScript Fetch API**
   - **Purpose**: The `fetch` API is used to asynchronously send and receive files from the server.
   - **Reason for Usage**: It allows for a seamless user experience without page reloads and handles file uploads in the background.

## How to Run the Project Locally

### Prerequisites:
1. Python 3.x installed on your system.
2. Django and related dependencies installed.

### Steps to Run the Project:
1. **Clone the Repository**:
   Clone the repository to your local system using the following command:
   ```bash
   git clone https://github.com/talha1135/aws-scrapper-django.git
   ```

2. **Navigate to the Project Directory**:
   ```bash
   cd aws-scrapper-django
   ```

3. **Set Up Virtual Environment** (Optional but recommended):
   Create and activate a virtual environment:
   ```bash
   python3 -m venv venv
   source venv/bin/activate  # For Linux/MacOS
   venv\Scriptsctivate     # For Windows
   ```

4. **Install Dependencies**:
   Install the required Python packages using pip:
   ```bash
   pip install -r requirements.txt
   ```

5. **Apply Migrations**:
   Run the migrations to set up the database:
   ```bash
   python manage.py migrate
   ```

6. **Run the Development Server**:
   Start the Django development server:
   ```bash
   python manage.py runserver
   ```

7. **Access the Application**:
   Open a web browser and navigate to:
   ```
   http://127.0.0.1:8000
   ```

   The file upload page should be accessible. You can upload `.xlsx` files, and once processed, a link to download the processed file will be displayed.

## Code Details

### `views.py`

- **`upload_file`**: This view handles the file upload process.
  - It checks if the file size is within the limit and if it is an `.xlsx` file.
  - After the file passes validation, it processes the file and stores the processed version in a response.

- **`download_file`**: This view handles downloading the processed file.
  - It retrieves the file by filename and serves it to the user for download.

### `urls.py`
- Contains the routes for the file upload and download functionality:
  - **`upload/`**: The URL for uploading files.
  - **`download/<str:filename>`**: The URL for downloading the processed file.

### `HTML/JS (Frontend)`

- **File Upload Form**: The form allows users to select a `.xlsx` file, which is validated for size and format before being uploaded.
- **JavaScript (Fetch)**: Sends the file to the Django backend asynchronously, handles responses (success or error), and displays appropriate feedback to the user.

### Example of How the Views Work:

#### `upload_file` View

```python
from django.http import JsonResponse
from django.core.files.storage import FileSystemStorage
from openpyxl import load_workbook

def upload_file(request):
    if request.method == 'POST' and request.FILES['file']:
        file = request.FILES['file']
        if file.size > 10 * 1024 * 1024:  # Max 10MB
            return JsonResponse({'success': False, 'message': 'File size exceeds 10MB limit.'})

        if not file.name.endswith('.xlsx'):
            return JsonResponse({'success': False, 'message': 'Only .xlsx files are allowed.'})

        # Process the file
        fs = FileSystemStorage()
        filename = fs.save(file.name, file)
        filepath = fs.url(filename)

        # Open the file and perform any processing (e.g., reading data with openpyxl)
        wb = load_workbook(filepath)
        # Process the workbook as needed...

        processed_filename = 'processed_' + filename
        fs.save(processed_filename, file)  # Save the processed file

        return JsonResponse({'success': True, 'processed_file': processed_filename})

    return JsonResponse({'success': False, 'message': 'No file uploaded.'})
```

#### `download_file` View

```python
from django.http import FileResponse
from django.core.files.storage import FileSystemStorage

def download_file(request, filename):
    fs = FileSystemStorage()
    file_path = fs.path(filename)
    if not fs.exists(filename):
        return JsonResponse({'success': False, 'message': 'File not found.'})
    
    response = FileResponse(open(file_path, 'rb'))
    return response
```

## Repository URL

For cloning the project, use the following repository URL:

[https://github.com/talha1135/aws-scrapper-django](https://github.com/talha1135/aws-scrapper-django)

---
This `README.md` provides a comprehensive guide to understanding and running the project, including all necessary details for setting it up on a local system, the tech stack used, and a step-by-step code explanation.
