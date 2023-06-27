pipeline {
    agent any
    stages {
        stage("Build")
        steps{
            sh "rm -rf friends"
            sh "git clone https://github.com/Mehrdad-Farshi/friends"
        }
    }
}