pipeline {
    agent {
        docker {
            image 'python:3-alpine' 
        }
    }
    stages {
        stage('Build') {
            agent{
                docker{
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'

                // stash(name: "compiled-results", includes: "sources/*.py*")
            }
        }
    }
}
