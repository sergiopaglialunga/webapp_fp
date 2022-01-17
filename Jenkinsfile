pipeline {
  agent any
  
  stages {
    stage('build'){
      steps{
        sh 'pwd'
        sh 'ls -ls'
      }
    }
  
    
    stage('test'){
      steps{
        echo 'Test stage executed.'
      }
    }
    
    stage('deploy'){
      steps{
        echo 'Deploy stage executed.'
      }    
    }
  }
  
}