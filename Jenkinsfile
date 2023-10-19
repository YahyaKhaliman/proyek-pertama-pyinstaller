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
        //     agent {
        //         docker {
        //             image 'cdrx/pyinstaller-linux:python2'
        //         }
        //     }
        //     steps {
        //         sh 'pyinstaller --onefile sources/add2vals.py'
        //     }
        //     post {
        //         success {
        //             archiveArtifacts 'dist/add2vals'
        //         }
        //         failure {
        //             echo 'Failed to deliver the application. Notify the team or take appropriate actions.'
        //             // Di sini Anda dapat menambahkan tindakan-tindakan lain untuk menangani kegagalan
        //         }
        //     }
        // }
        stage('Deliver') {
            agent {
                docker {
                    image 'cdrx/pyinstaller-linux:python2'
                }
            }
            steps {
                // Restore the Python source code and compiled byte code files (with .pyc extension) from the previously saved stash.
                unstash(name: 'compiled-results')

                // Execute the pyinstaller command (in the PyInstaller container) on your simple Python application.
                // This bundles your add2vals.py Python application into a single standalone executable file
                // and outputs this file to the dist workspace directory (within the Jenkins home directory).
                sh "pyinstaller --onefile sources/add2vals.py"
            }
            post {
                success {
                    // Archive the standalone executable file and expose this file through the Jenkins interface.
                    archiveArtifacts 'dist/add2vals'

                    // Clean up the build and dist directories
                    sh 'rm -rf build dist'
                }
            }
        }
    }
}