pipeline
{
    
    agent any

    stages
    {     
        stage('ec2 deploy')        {
            steps{
                sshagent(['Express_Stroe_Admin_Portal']){
                    sh """ssh -o StrictHostKeyChecking=no -tt ubuntu@ec2-44-200-232-234.compute-1.amazonaws.com << EOF
                    pwd
                    cd ~/apps/opt/python/es.adminportal.service
                    git pull
                    sudo docker-compose down
                    sudo docker-compose build
                    sudo docker-compose up --detach
                    exit
                    EOF"""
                }
            }
        }
}
    post 
    {
        success {

      emailext (
          subject: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
          
          body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p> Successful executed all the stages, Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
          recipientProviders: [[$class: 'DevelopersRecipientProvider']],
          to: 'arunkumar.s@infovision.com'
        )
      emailext (
          subject: "SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",
          
          body: """<p>SUCCESSFUL: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p> Successful executed all the stages, Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
          recipientProviders: [[$class: 'DevelopersRecipientProvider']],
          to: 'vinayak.ashwin@infovision.com'
        )
    }

    failure {
    emailext (
          subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",  

          body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p> Pipeline is interrupted by Python, Error message is thrown, target env uninterrupted, Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
            recipientProviders: [[$class: 'DevelopersRecipientProvider']],
          to: 'arunkumar.s@infovision.com'
        )
    emailext (
          subject: "FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]'",  

          body: """<p>FAILED: Job '${env.JOB_NAME} [${env.BUILD_NUMBER}]':</p>
            <p> Pipeline is interrupted by Python, Error message is thrown, target env uninterrupted, Check console output at &QUOT;<a href='${env.BUILD_URL}'>${env.JOB_NAME} [${env.BUILD_NUMBER}]</a>&QUOT;</p>""",
            recipientProviders: [[$class: 'DevelopersRecipientProvider']],
          to: 'vinayak.ashwin@infovision.com'
        )
   }
    always 
    { 
            cleanWs()
    }
    } 
}
