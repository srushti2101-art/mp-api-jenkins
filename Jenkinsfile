pipeline {
    agent any

    stages {
        stage('Clone Repository') {
            steps {
                echo 'Cloning repository...'
            }
        }

        stage('Build Docker Image') {
            steps {
                sh '/Applications/Docker.app/Contents/Resources/bin/docker build -t mp-api-jenkins .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh '/Applications/Docker.app/Contents/Resources/bin/docker run -d -p 8001:8000 mp-api-jenkins'
            }
        }
    }
}