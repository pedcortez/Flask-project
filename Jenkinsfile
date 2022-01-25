pipeline {

  agent any
 
  environment {
    DOCKERHUB_CREDENTIALS = credentials('pedro-dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t pedrocortez/todo-app .'
        }
      }

    stage('Test') {
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
    stage('Deploy') {
      steps {
        sh ./deploy.sh
      }
    }
  }
  post {
    always {
      sh 'docker logout'
    }
  }
}
