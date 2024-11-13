# Branching Strategy

This project follows a branching strategy designed to separate development and production environments:

- **main branch**: The primary branch used for production. Only thoroughly tested and approved code is merged here.


- **develop branch**: The active development branch where new features, bug fixes, and improvements are tested. Once the code is stable, it can be merged into the `main` branch for release.


- **Feature branches**: All new features, fixes, or enhancements should be developed in separate branches created from `develop`. When ready, these branches are merged into `develop` through pull requests.


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