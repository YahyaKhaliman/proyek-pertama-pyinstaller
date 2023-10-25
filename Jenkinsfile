pipeline {
    agent none
    stages {
        stage('Build') {
            agent {
                docker {
                    image 'python:2-alpine'
                }
            }
            steps {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
                stash(name: 'compiled-results', includes: 'sources/*.py*')
            }
        }
        stage('Test') {
            agent {
                docker {
                    image 'qnib/pytest'
                }
            }
            steps {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
            post {
                always {
                    junit 'test-reports/results.xml'
                }
            }
        }
        // stage('Deliver') {
        //     agent any
        //         environment {
        //             VOLUME = '$(pwd)/sources:/src'
        //             IMAGE = 'cdrx/pyinstaller-linux:python2'
        //         }
        //     steps {
        //         dir(path: env.BUILD_ID) {
        //             unstash(name: 'compiled-results')
        //             sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'"
        //         }
        //     }
        //     post {
        //         success {
        //             archiveArtifacts "${env.BUILD_ID}/sources/dist/add2vals"
        //             sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
        //         }
        //     }
        // }
        stage('Deploy') {
            agent {
                docker {
                    image 'python:3-alpine'
                }
            }
            steps {
                script {
                    // Buat virtual environment (venv)
                    sh 'python -m venv venv'
                    // Aktifkan venv
                    sh 'source venv/bin/activate'
                    // Upgrade pip
                    sh 'pip install --upgrade pip'
                    // Instal cmake
                    sh 'pip install cmake'
                    // Jalankan aplikasi Python Anda
                    sh 'python ./sources/app.py'
                }
            }
        }
    }
}
