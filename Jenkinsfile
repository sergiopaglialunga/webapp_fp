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
        def test = 2 + 2 > 3? 'pass':'fail'
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