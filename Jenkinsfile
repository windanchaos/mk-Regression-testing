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
            steps {
                sh "bash ~/ci/build.sh 3"
                sh "bash ~/ci/build.sh 4"
            }
        }
        stage('deploy webent') {
            steps {
                sh "bash ~/ci/deploy.sh 1"
                sh "bash ~/ci/deploy.sh 15"
            }
            steps {
                sh "bash ~/ci/deploy.sh 2"
                sh "bash ~/ci/deploy.sh 14"
            }
        }
    }
    stages {
        stage('build webent2') {
            steps {
                sh "bash ~/ci/build.sh 3"
                sh "bash ~/ci/build.sh 4"
            }
            steps {
                sh "bash ~/ci/build.sh 5"
                sh "bash ~/ci/build.sh 6"
            }
        }
        stage('deploy webent') {
            steps {
                sh "bash ~/ci/deploy.sh 2"
                sh "bash ~/ci/deploy.sh 15"
            }
        }
    }
}