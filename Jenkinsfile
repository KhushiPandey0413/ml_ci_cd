pipeline {

    agent any


    environment {

        VENV = ".venv"

    }


    stages {

        stage('Checkout Code') {

            steps {

                echo 'Checking out source code...'

                checkout scm

            }

        }


        stage('Create Virtual Environment') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        python3 -m venv .venv
                        '''

                    } else {

                        bat '''
                        python -m venv .venv
                        '''

                    }

                }

            }

        }


        stage('Install Dependencies') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        . .venv/bin/activate
                        python -m pip install --upgrade pip
                        pip install -r requirements.txt
                        '''

                    } else {

                        bat '''
                        .venv\\Scripts\\python.exe -m pip install --upgrade pip
                        .venv\\Scripts\\pip.exe install -r requirements.txt
                        '''

                    }

                }

            }

        }


        stage('Run Tests') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        .venv/bin/python -m pytest tests/
                        '''

                    } else {

                        bat '''
                        .venv\\Scripts\\python.exe -m pytest tests\\
                        '''

                    }

                }

            }

        }


        stage('Train Model') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        .venv/bin/python src/train.py
                        '''

                    } else {

                        bat '''
                        .venv\\Scripts\\python.exe src\\train.py
                        '''

                    }

                }

            }

        }


        stage('Evaluate Model') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        .venv/bin/python src/evaluate.py
                        '''

                    } else {

                        bat '''
                        .venv\\Scripts\\python.exe src\\evaluate.py
                        '''

                    }

                }

            }

        }


        stage('Test Prediction') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        .venv/bin/python src/predict.py
                        '''

                    } else {

                        bat '''
                        .venv\\Scripts\\python.exe src\\predict.py
                        '''

                    }

                }

            }

        }


        stage('Deploy Model Locally') {

            steps {

                script {

                    if (isUnix()) {

                        sh '''
                        mkdir -p deployed_models
                        cp models/model.pkl deployed_models/model.pkl
                        '''

                    } else {

                        bat '''
                        if not exist deployed_models mkdir deployed_models
                        copy /Y models\\model.pkl deployed_models\\model.pkl
                        '''

                    }

                }

            }

        }

    }


    post {

        success {

            echo 'MLOps Pipeline Completed Successfully!'

        }


        failure {

            echo 'Pipeline Failed! Check Jenkins Console Output.'

        }


        always {

            echo 'Cleaning workspace...'

        }

    }

}