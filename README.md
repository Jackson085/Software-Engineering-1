# Start the Backend

To start the backend server, follow these steps:

1. **Open the Command Line Interface (CLI)**:
   Make sure that Python is installed on your system.

2. **Run the Backend**:
   In the CLI, execute the following command:

```bash
pip install -r requirements.txt
python -u -m Docker.entrypoint
```

Access the OpenAPI Documentation: After the server is running, open your web browser and navigate to the following URL:
``` code
http://127.0.0.1:5000/apidocs
```
This will display the automatically generated API documentation for your application.