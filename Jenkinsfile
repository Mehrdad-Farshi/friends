pipeline {
    agent any
    
    stages {
        stage('Run Python Script') {
            steps {
            sh "rm -rf friends"
            sh "git clone https://github.com/Mehrdad-Farshi/friends"
            echo "BUILD ID : ${env.BUILD_ID}, JENKINS URL : ${env.JENKINS_URL}"
            }
        }
    }
}