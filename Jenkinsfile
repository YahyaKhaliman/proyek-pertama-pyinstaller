pipeline {
    agent any
    stages {
        stage('Build') {
            steps {
                script {
                    // Build with Docker
                    docker.image('python:2-alpine').inside {
                        sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                    }

                    // Build without Docker
                    sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                }
            }
        }
    }
}
