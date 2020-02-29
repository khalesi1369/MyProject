pipeline {
    agent any
    
    stages {
        stage('Test') {
            steps {
		 sh './test_hello.py'
            }
        }
    }
    post {
        always {
            sh 'echo "test succssesfully"'
        }
    }
}
