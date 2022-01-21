pipeline {
  agent any
 
  environment {
    DOCKERHUB_CREDENTIALS = credentials('pedro-dockerhub')
  }
  stages {
    stage('Initialize'){
        def dockerHome = tool 'myDocker'
        env.PATH = "${dockerHome}/bin:${env.PATH}"
    }
    stage('Build') {
      steps {
        sh 'docker build -t todo-app:latest .'
        sh 'docker build -t todo-mysql:latest ./database .'
      }
    }
    stage('Login') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
      }
    }
    stage('Push') {
      steps {
        sh 'docker push pedrocortez/todo-app:latest'
        sh 'docker push pedrocortez/todo-mysql:latest'
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}