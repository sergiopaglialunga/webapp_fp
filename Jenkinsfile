pipeline {
  agent any
  
  stages {
    stage('build'){
      steps{
        sh 'cd /var/jenkins_home/workspace/MultiBranchPipeline-job_master/webapp'
        sh 'docker-compose -f cd /var/jenkins_home/workspace/MultiBranchPipeline-job_master/webapp/docker-compose.yml up --build'
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