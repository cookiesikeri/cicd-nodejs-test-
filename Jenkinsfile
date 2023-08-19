pipeline {
    agent any
    environment {
        ECR_REPO_NAME = 'your-ecr-repo-name'
        ECR_URL = 'https://your-ecr-url'
        GIT_CREDENTIALS_ID = 'your-git-credentials-id'
    }
    stages {
        stage('Unit Test') {
            when { changeRequest target: 'develop' }
            steps {
                sh 'npm test'
            }
        }
        stage('Docker Build and Push') {
           when { anyOf { branch 'develop'; branch 'master' } }
            steps {
                script {
                    docker.build("${ECR_REPO_NAME}:${env.BUILD_NUMBER}")
                    docker.withRegistry(ECR_URL, "ecr:us-west-2:${env.CREDENTIALS_ID}") {
                        docker.push("${ECR_REPO_NAME}:${env.BUILD_NUMBER}")
                    }
                }
            }
        }
        stage('Approval') {
           when { anyOf { branch 'develop'; branch 'master' } }
            steps {
                input 'Deploy to environment?'
            }
        }
        stage('Deploy') {
           when { anyOf { branch 'develop'; branch 'master' } }
            steps {
                script {
                    // Determine the environment based on the branch
                    def env = (env.BRANCH_NAME == 'develop') ? 'development' : 'production'
                    // Clone the Helm chart repo
                    git credentialsId: GIT_CREDENTIALS_ID, url: 
'https://github.com/your-helm-chart-repo'
                    // Update the Docker image tag in the values.yaml file
                    sh """
                        sed -i 's|image: .*|image: 
${ECR_URL}/${ECR_REPO_NAME}:${env.BUILD_NUMBER}|' ${env}/values.yaml
                    """
                    // Commit and push the changes
                    sh """
                        git add ${env}/values.yaml
                        git commit -m "Update Docker image tag for ${env} environment"
                        git push origin HEAD
                    """
                }
            }
        }
    }
}
