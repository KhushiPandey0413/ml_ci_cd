pipeline {

    agent any

    stages {

        stage('Check Python') {

            steps {

                bat '''
                    echo ==============================
                    echo Checking Python
                    echo ==============================

                    where python
                    python --version
                    python -m pip --version
                '''
            }
        }


        stage('Create Virtual Environment') {

            steps {

                bat '''
                    echo ==============================
                    echo Creating Virtual Environment
                    echo ==============================

                    if exist .venv rmdir /s /q .venv

                    python -m venv .venv

                    .venv\\Scripts\\python.exe --version

                    .venv\\Scripts\\python.exe -m pip install --upgrade pip
                '''
            }
        }


        stage('Install Dependencies') {

            steps {

                bat '''
                    echo ==============================
                    echo Installing Dependencies
                    echo ==============================

                    .venv\\Scripts\\python.exe -m pip install -r requirements.txt
                '''
            }
        }


        stage('Run Tests') {

            steps {

                bat '''
                    echo ==============================
                    echo Running Tests
                    echo ==============================

                    .venv\\Scripts\\python.exe -m pytest tests -v
                '''
            }
        }


        stage('Train Model') {

            steps {

                bat '''
                    echo ==============================
                    echo Training ML Model
                    echo ==============================

                    .venv\\Scripts\\python.exe src\\train.py
                '''
            }
        }


        stage('Evaluate Model') {

            steps {

                bat '''
                    echo ==============================
                    echo Evaluating ML Model
                    echo ==============================

                    .venv\\Scripts\\python.exe src\\evaluate.py
                '''
            }
        }


        stage('Test Prediction') {

            steps {

                bat '''
                    echo ==============================
                    echo Testing Prediction
                    echo ==============================

                    .venv\\Scripts\\python.exe src\\predict.py
                '''
            }
        }


        stage('Deploy Model Locally') {

            steps {

                bat '''
                    echo ==============================
                    echo Deploying Model
                    echo ==============================

                    if not exist deployed_models mkdir deployed_models

                    copy /Y models\\model.pkl deployed_models\\model_%BUILD_NUMBER%.pkl
                '''
            }
        }
    }


    post {

        success {

            echo '===================================='
            echo 'MLOps Pipeline Successful'
            echo '===================================='

            archiveArtifacts(
                artifacts: 'models/*.pkl',
                fingerprint: true
            )
        }


        failure {

            echo '===================================='
            echo 'MLOps Pipeline FAILED'
            echo 'Check the Console Output'
            echo '===================================='
        }
    }
}