# Python CI/CD Pipeline with Jenkins, Docker, and GitHub Webhooks

This project demonstrates a *CI/CD pipeline* using *Jenkins, Docker, and GitHub Webhooks* to automate the process of building, testing, and deploying a simple Python application to a cloud environment (e.g., AWS EC2).

## Project Overview

This project is a simple *Python* web application that displays *"Hello, CICD with Jenkins and Docker!"* when accessed. The purpose of this repository is to demonstrate an automated *CI/CD pipeline* using *Jenkins* and *Docker* to:
- Build and test the app.
- Create a Docker image.
- Push the Docker image to Docker Hub.
- Deploy the app to a cloud instance (AWS EC2 or GCP).

The pipeline is triggered by a *GitHub webhook*, which activates the build process whenever changes are pushed to the repository.

## Technologies Used

- *Python*: Backend application framework.
- *Docker*: Containerization platform to package the app.
- *Jenkins*: Automation server for CI/CD pipeline.
- *GitHub*: Version control and source code management.
- *AWS EC2/GCP*: Cloud deployment platforms.
- *GitHub Webhook*: To trigger Jenkins builds on code push events.

## Getting Started

Follow these steps to set up the project locally and configure the CI/CD pipeline.

### 1. Create the Project Directory

```bash
mkdir jenkins-project
cd jenkins-project
```

### 2. Install Dependencies

Run the following commands to set up the environment and install dependencies:

```bash
python3 -m venv venv
source venv/bin/activate
pip install flask
```

### 3. Create the Application File

Create a file `app.py` with the following content:

```python
from flask import Flask

app = Flask(__name__)

@app.route("/")
def home():
    return "Hello, CICD with Jenkins and Docker!"

if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)
```

### 4. Run the Application Locally

To test the application locally, run:

```bash
python app.py
```

Open your browser and navigate to `http://localhost:5000` to view the message: *Hello, CICD with Jenkins and Docker!*

---

## Docker Setup

### 1. Install Docker

Follow the [Docker installation guide](https://docs.docker.com/get-docker/) for your operating system.

### 2. Create a Dockerfile

Create a `Dockerfile` with the following content:

```dockerfile
FROM python:3.9
WORKDIR /app
COPY . .
RUN pip install -r requirements.txt
EXPOSE 5000
CMD ["python", "app.py"]
```

### 3. Build and Run the Docker Container

```bash
docker build -t web-app .
docker run -p 5000:5000 web-app
```
![Screenshot (21)](https://github.com/user-attachments/assets/2be11760-6677-4c4b-8b0d-dea42bb5b8be)

---

## Install Java and Jenkins

### 1. Install Java

Jenkins requires Java to run. Install it using:

```bash
sudo apt update
sudo apt install openjdk-11-jdk -y
```

### 2. Install Jenkins

Follow the [official Jenkins installation guide](https://www.jenkins.io/doc/book/installing/) to install Jenkins on your system.

---

## Jenkins Pipeline Setup

### 1. Create a Jenkins Pipeline

1. Go to the Jenkins Dashboard and click on **New Item**.
2. Select **Pipeline** and give it a name, e.g., `hello-cicd-pipeline`.
3. Under the **Pipeline** section, select *Pipeline script from SCM*.
4. Enter your GitHub repository URL and set the script path to `Jenkinsfile`.
5. Save and apply the configuration.

The `Jenkinsfile` defines the CI/CD pipeline for this project.

### 2. Push Docker Image to Docker Hub

The Jenkins pipeline will automatically push the Docker image to Docker Hub after a successful build. Ensure you have a Docker Hub account and store your credentials in Jenkins.

---

## Running the Pipeline

Monitor the progress of the Jenkins pipeline from the Jenkins dashboard.

The pipeline will execute the following steps:

1. Checkout the code from GitHub.
2. Install dependencies.
3. Run tests.
4. Build the Docker image.
5. Push the image to Docker Hub.
6. Deploy the app to AWS EC2 (or GCP).

![Screenshot (23)](https://github.com/user-attachments/assets/cfda4363-3c15-4b0d-a855-0bd464cef49f)

---

## GitHub Webhook Configuration

To trigger the Jenkins pipeline automatically when changes are pushed to the repository, configure a GitHub webhook:

1. Go to your repository on GitHub.
2. Navigate to **Settings > Webhooks > Add webhook**.
3. In the **Payload URL** field, enter your Jenkins server URL:
   ```
   http://<Jenkins_URL>/github-webhook/
   ```
4. Set **Content type** to `application/json`.
5. Click **Add webhook**.

This will configure GitHub to send webhook notifications to Jenkins every time you push code to the repository.

---

### 2. Access the Deployed Application

Once the deployment is complete, the app will be running on your cloud instance. Open a browser and visit the instance's public IP (e.g., `http://<instance-ip>:5000`) to see the app running.

![Screenshot (24)](https://github.com/user-attachments/assets/fc0b12bf-8bda-4da0-8ad1-941c2c2da6c0)

---

## Conclusion

This guide demonstrates how to set up a full CI/CD pipeline using Jenkins, Docker, and GitHub Webhooks to automate the deployment of a Python web application. The integration of these tools allows seamless deployment to cloud environments like AWS EC2 or GCP.

