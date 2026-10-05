import uvicorn

uvicorn.run(
    "src.serving.app:app",
    host="0.0.0.0",
    port=8000,
    reload=True
)





pipeline {

    agent any

    environment {

        PYTHON = "C:\\Users\\80737\\AppData\\Local\\Programs\\Python\\Python312\\python.exe"

        PROJECT_DIR = "${WORKSPACE}"

        MLFLOW_TRACKING_URI = "http://127.0.0.1:5000"
    }

    stages {

        stage('Clone Repository') {

            steps {

                git branch: 'main',
                url: 'https://github.com/your-repo.git'
            }
        }

        stage('Install Dependencies') {

            steps {

                bat """
                %PYTHON% -m pip install --upgrade pip
                %PYTHON% -m pip install -r requirements.txt
                """
            }
        }

        stage('Start MLflow Server') {

            steps {

                bat """
                start /B %PYTHON% src\\start_mlflow.py
                """
            }
        }

        stage('Extract Data From Snowflake') {

            steps {

                bat """
                %PYTHON% src\\data\\extract_from_snowflake.py
                """
            }
        }

        stage('Preprocess Data') {

            steps {

                bat """
                %PYTHON% src\\data\\preprocess.py
                """
            }
        }

        stage('Split Dataset') {

            steps {

                bat """
                %PYTHON% src\\data\\split_data.py
                """
            }
        }

        stage('Train Models') {

            steps {

                bat """
                %PYTHON% src\\training\\train_model.py
                """
            }
        }

        stage('Register Best Model') {

            steps {

                bat """
                %PYTHON% src\\mlflow\\register_model.py
                """
            }
        }

        stage('Transition To Production') {

            steps {

                bat """
                %PYTHON% src\\mlflow\\transition_stage.py
                """
            }
        }

        stage('Deploy FastAPI') {

            steps {

                bat """
                start /B %PYTHON% src\\start_api.py
                """
            }
        }

        stage('Smoke Test') {

            steps {

                bat """
                curl http://127.0.0.1:8000/docs
                """
            }
        }
    }

    post {

        success {

            echo 'Pipeline Executed Successfully'
        }

        failure {

            echo 'Pipeline Failed'
        }
    }
}