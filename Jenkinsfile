pipeline {
    agent any
    
    stages {
        stage('Run Python Script') {
            steps {
            sh "rm -rf friends"
            sh "git clone https://github.com/Mehrdad-Farshi/friends"
            }
        }
    }
}