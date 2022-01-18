pipeline {
  agent any
  
  stages {
    stage('build'){
      steps{
        sh 'cd /var/jenkins_home/workspace/MultiBranchPipeline-job_master'
        sh 'docker-compose -df cd /var/jenkins_home/workspace/MultiBranchPipeline-job_master/docker-compose.yml up --build'
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