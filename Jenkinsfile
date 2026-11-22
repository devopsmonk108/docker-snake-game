pipeline{
  agent any
  environment {
    IMAGE = "anoncat01/docker-snake-game"
  }
stages{
 stage('Checkout') {
    steps { checkout scm }
 }
  stage('Build Image') {
   steps { sh 'docker build -t $IMAGE:${BUILD_NUMBER} -t $IMAGE:latest .'}
}
 stage('Test') {
  steps {sh 'docker run --rm $IMAGE:${BUILD_NUMBER} python -m py_compile app.py' }
}
stage('Push to Docker Hub') {
  steps {
      withCredentials([usernamePassword(credentialsId: 'dockerhub-creds', usernameVariable: 'USER', passwordVariable: 'PASS')]) {
 sh '''
     echo $PASS | docker login -u $USER --password-stdin
     docker push $IMAGE:${BUILD_NUMBER}
     docker push $IMAGE:latest
    '''
  }
 }
}
stage('Deploy to AWS') {
  steps{
    sshagent(credentials: ['ec2-ssh']) {
     sh '''
         ssh -o StrictHostKeyChecking=no ubuntu@100.52.135.136 "
           docker pull $IMAGE:${BUILD_NUMBER} &&
           (docker rm -f snake || true) &&
           docker run -d --name snake --network web --restart unless-stopped $IMAGE:${BUILD_NUMBER}
"
'''
  } 
 }
}
stage ('Smoke test') {
  steps {sh 'curl --fail --retry 5 --retry-delay 3 --retry-connrefused https://myownsnake-game.duckdns.org'
    }
   }
  }
} 
