pipeline {
    agent any
    stages {
        stage('pull code') {
            steps {
                sh "bash ~/ci/pull.sh"
            }
        }
        stage('build aggrator') {
            steps {
                sh "bash ~/ci/build.sh 0"
            }
        }
        stage('build webent') {
            steps {
                sh "bash ~/ci/build.sh 1"
                sh "bash ~/ci/build.sh 2"
            }
        }
        stage('deploy webent') {
            steps {
                sh "bash ~/ci/deploy.sh 1"
                sh "bash ~/ci/deploy.sh 15"
            }
        }
    }
}