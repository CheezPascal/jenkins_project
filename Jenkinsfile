pipeline {
    agent any
    environment {
        DOCKERHUB_CREDENTIALS = credentials('docker_hub_login')  
    }
    stages {
        stage('Build Docker Image') {
            steps {
                script {
                    echo 'Building Docker Image for chisom.py...'
                    app = docker.build("chisompascaldkr/python-app:${env.BUILD_NUMBER}")
                }
            }
        }
        stage('Login to Dockerhub') {
            steps {
                script {
                    echo 'Logging in to Docker Hub...'
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKERHUB_CREDENTIALS}") {
                        echo 'Logged in successfully.'
                    }
                }
            }
        }
        stage('Push Docker Image to Dockerhub') {
            steps {
                script {
                    echo 'Pushing Docker image to Docker Hub...'
                    docker.withRegistry('https://registry.hub.docker.com', "${DOCKERHUB_CREDENTIALS}") {
                        app.push("${env.BUILD_NUMBER}")
                        app.push("latest")
                    }
                }
            }
        }
        stage('Run Docker Container') {
            steps {
                script {
                    echo 'Running Docker container on port 8083...'
                    // Stop and remove any existing container with the same name
                    sh 'docker stop chisom_app || true && sudo docker rm chisom_app || true'
                    // Run the newly built image in a container and map port 8083 on the host to port 8080 (changed 8084) in the container
                    sh 'docker run -d --name chisom_app -p 8083:8084 chisompascaldkr/python-app:${env.BUILD_NUMBER}'
                }
            }
        }
    }
    post {
        success {
            echo 'Pipeline completed successfully!'
        }
        failure {
            echo 'Pipeline failed.'
        }
    }
}
