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
                sh 'docker build -t mp-api-jenkins .'
            }
        }

        stage('Run Docker Container') {
            steps {
                sh 'docker run -d -p 8001:8000 mp-api-jenkins'
            }
        }
    }
}