pipeline {
    agent any

    stages {

        stage('Checkout') {
            steps {
                echo 'Checking out project from GitHub'
                checkout scm
            }
        }

        stage('Docker Build') {
            steps {
                echo 'Building Docker image'
                bat 'docker compose build tests'
            }
        }

        stage('Start Containers') {
            steps {
                bat 'docker compose up -d app chrome'
            }
        }

        stage('Run Selenium Tests') {
            steps {
                bat 'docker compose run --rm tests'
            }
        }

        stage('Test Report') {
            steps {
                junit allowEmptyResults: true,
                      testResults: 'report.xml'
            }
        }
    }

    post {
        always {
            bat 'docker compose down --remove-orphans'
        }

        success {
            echo 'CI/CD Pipeline executed successfully!'
        }

        failure {
            echo 'CI/CD Pipeline failed. Check the console output.'
        }
    }
}