pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out code...'
            }
        }

        stage('Build') {
            steps {
                sh '/Applications/Docker.app/Contents/Resources/bin/docker build -t mp-api-jenkins .'
            }
        }

        stage('Test') {
            steps {
                echo 'Running tests...'
            }
        }

        stage('Deploy') {
            steps {
                sh '/Applications/Docker.app/Contents/Resources/bin/docker run -d -p 8001:8000 mp-api-jenkins'
            }
        }
    }
}