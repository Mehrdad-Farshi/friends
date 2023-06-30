pipeline {
    agent any
    environment{
        BUILDER_NAME = 'mehrdad'
    }
    stages {
        stage('Run Python Script') {
            steps {
            // sh "rm -rf friends"
            // sh "git clone https://github.com/Mehrdad-Farshi/friends"
            git url: 'https://github.com/Mehrdad-Farshi/friends.git', branch: 'master'
            echo "builder name : ${BUILDER_NAME} BUILD ID : ${env.BUILD_ID}, JENKINS URL : ${env.JENKINS_URL}"
            }
        }
    }
}