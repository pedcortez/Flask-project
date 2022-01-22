pipeline {

  agent any
 
  environment {
    DOCKERHUB_CREDENTIALS = credentials('pedro-dockerhub')
  }
  stages {
    stage('Build') {
      steps {
        sh 'docker build -t pedrocortez/todo-app .'
        sh 'docker build . -t pedrocortez/todo-mysql -f database/Dockerfile'
        }
      }

    stage('test env') {
        steps {
            sh 'pip install -r requirements.txt'
            sh 'python3 test.py'
        }
      }
    // stage('Login') {
    //   steps {
    //     sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
    //   }
    // }
    stage('Push') {
      steps {
        sh 'echo $DOCKERHUB_CREDENTIALS_PSW | docker login -u $DOCKERHUB_CREDENTIALS_USR --password-stdin'
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