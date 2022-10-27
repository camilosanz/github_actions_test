pipeline {
    agent {label 'DevOps'}
    environment {
                    SONAR_TOKEN = credentials('sonarqube')
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
        stage('Static code analysis') {
            steps {
                script {
                    def sonarscanner = tool 'sonarqube-scanner-jala'
                    def sonarscannerParams = "-Dsonar.projectName=AttendanceApp " + 
                        "-Dsonar.projectKey=AttendanceApp " + 
                        "-Dsonar.sources=. " +
                        "-Dsonar.python.coverage.reportPaths=coverage.xml"
                    withSonarQubeEnv('SonarQubeCE-Jala'){
                        sh "${sonarscanner}/bin/sonar-scanner ${sonarscannerParams}"
                    }
                }
            }
        }
        // stage('Static code analysis') {
        //     steps {
        //         sh "sonar-scanner -Dsonar.login=${SONAR_TOKEN}"
        //     }
        // }
    }
}