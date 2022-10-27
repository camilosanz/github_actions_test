pipeline {
    agent {label 'DevOps'}
    environment {
        SONARQUBE_URL="10.0.2.15:3002"
        YOUR_PROJECT_KEY="attendance_app_ci_blue"
        SONAR_LOGIN=credentials('sonarscanner-container')
    }
    stages {
        stage('Install python') {
            steps {
                sh """ 
                    sudo apt-get update
                    sudo apt-get install python3 python3-pip -y
                """
            }

        }
        stage('Install dependencies') {
            steps {
                sh 'pip3 install -r requirements.txt'
            }

        }
        stage('Run pytest') {
            steps {
                sh 'python3 -m coverage run -m pytest'
            }
        }
        stage('Run Coverage pytest') {
            steps {
                sh 'python3 -m coverage html'
            }
        }

        stage('Static Code Analysis - Plugin') {
           steps {
               script {
                   def sonarscanner = tool 'sonarqube-scanner-jala'
                   def sonarscannerParams = "-Dsonar.projectName=${YOUR_PROJECT_KEY} " + 
                       "-Dsonar.projectKey=${YOUR_PROJECT_KEY} " + 
                       "-Dsonar.sources=. " + 
                       "-Dsonar.python.coverage.reportPaths=coverage.xml"
                   withSonarQubeEnv('SonarQubeCE-Jala'){
                       sh "${sonarscanner}/bin/sonar-scanner ${sonarscannerParams}"
                   }
               }
           }
        }

        stage('Static Code Analysis') {
            steps {
                sh """
                    docker run \
                        --rm \
                        -e SONAR_HOST_URL="http://${SONARQUBE_URL}" \
                        -e SONAR_SCANNER_OPTS="-Dsonar.projectKey=${YOUR_PROJECT_KEY} -Dsonar.python.coverage.reportPaths=coverage.xml -Dsonar.projectName=${YOUR_PROJECT_KEY}-project" \
                        -e SONAR_LOGIN="${SONAR_LOGIN}" \
                        -v "$WORKSPACE:/usr/src" \
                        sonarsource/sonar-scanner-cli
                """
            }
        }
    }
}