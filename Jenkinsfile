stage('Deploy Model') {

    steps {

        script {

            if (isUnix()) {

                sh """
                mkdir -p deployed_models
                cp models/model.pkl deployed_models/model_${BUILD_NUMBER}.pkl
                """

            } else {

                bat """
                if not exist deployed_models mkdir deployed_models
                copy /Y models\\model.pkl deployed_models\\model_%BUILD_NUMBER%.pkl
                """

            }

        }

    }

}