pipeline{
    agent any

    environment {
        VENV_DIR ="hotel"
    }

    stages{
        stage('Cloning Github repo to Jenkins'){
            steps{
                script{
                    echo 'Cloning Github repo to Jenkins.....'
                    checkout scmGit(branches: [[name: '*/main']], extensions: [], userRemoteConfigs: [[credentialsId: 'github-token', url: 'https://github.com/saksham011023/Hotel-Reservation-Prediction.git']])
                }
            }
        }

        stage('Setting up our virtual environment and install dependencies'){
            steps{
                script{
                    echo 'Setting up our virtual environment and install dependencies.....'
                    sh '''
                    python -m venv ${VENV_DIR}
                    -${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
    }
}
