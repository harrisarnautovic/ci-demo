pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                sh 'python3 -m unittest discover -v'
            }
        }
    }
    post {
        success {
            withCredentials([string(credentialsId: 'webex-token', variable: 'WEBEX_TOKEN'),
                             string(credentialsId: 'webex-room', variable: 'WEBEX_ROOM')]) {
                sh 'python3 notify.py SUCCESS'
            }
        }
        failure {
            withCredentials([string(credentialsId: 'webex-token', variable: 'WEBEX_TOKEN'),
                             string(credentialsId: 'webex-room', variable: 'WEBEX_ROOM')]) {
                sh 'python3 notify.py FAILURE'
            }
        }
    }
}
