pipeline{
    agent any

    environment {
        VENV_DIR ="hotel"
        GCP_PROJECT="yt-analysis-project-437219"
        GCLOUD_PATH="/var/jenkins_home/google-cloud-sdk/bin"
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
                    . ${VENV_DIR}/bin/activate
                    pip install --upgrade pip
                    pip install -e .
                    '''
                }
            }
        }
       stage('Building and Pushing Docker Image to GCR'){
            steps{
                withCredentials([file(credentialsId: 'gcp-key', variable : "GOOGLE_APPLICATION_CREDENTIALS")]){
                    script{
                        echo 'Building and Pushing Docker Image to GCR................'
                        sh '''
                        export PATH=$PATH:${GCLOUD_PATH}

                        gcloud auth activate-service-account --key-file="\$GOOGLE_APPLICATION_CREDENTIALS"

                        gcloud config set project ${GCP_PROJECT}

                        gcloud auth configure-docker --quiet

                        docker build -t gcr.io/${GCP_PROJECT}/hotel-reservation-prediction .

                        docker push gcr.io/${GCP_PROJECT}/hotel-reservation-prediction 
                        '''

                    }
                }
                }
            }
        } 
    }

