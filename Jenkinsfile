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
        stage('Deliver') {
            agent any
                environment {
                    VOLUME = '$(pwd)/sources:/src'
                    IMAGE = 'cdrx/pyinstaller-linux:python2'
                }
            steps {
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'"
                }
            }
            post {
                success {
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/add2vals"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
        stage('Manual Approval') {
            steps {
                script {
                    def userInput = input(
                        message: 'Apakah Anda ingin melanjutkan tahap Deploy? Ketik "proceed" untuk melanjutkan atau "abort" untuk menghentikan:',
                        ok: 'proceed',
                        submitter: 'user',
                        parameters: [string(defaultValue: 'proceed', description: '', name: 'ACTION')]
                    )
                    if (userInput != 'proceed') {
                        currentBuild.result = 'ABORTED'
                        error('Pipeline dihentikan oleh pengguna')
                    }
                }
            }
        }
        stage('Deploy') {
            agent any
            environment {
                VOLUME = '$(pwd)/sources:/src'
                IMAGE = 'cdrx/pyinstaller-linux:python2'
            }
            steps {
                script {
                    echo 'Menjeda eksekusi pipeline selama 5 detik...'
                    sleep time: 5, unit: 'SECONDS'
                }
                dir(path: env.BUILD_ID) {
                    unstash(name: 'compiled-results')
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'pyinstaller -F add2vals.py'"
                }
            }
            post {
                success {
                    echo 'Selamat Deploy Berhasil'
                    archiveArtifacts "${env.BUILD_ID}/sources/dist/add2vals"
                    sh "docker run --rm -v ${VOLUME} ${IMAGE} 'rm -rf build dist'"
                }
            }
        }
    }
}