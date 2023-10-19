node {
    stage('Build') {
        try {
            checkout scm
            def pythonImage = docker.image('python:2-alpine')
            pythonImage.inside {
                sh 'python -m py_compile sources/add2vals.py sources/calc.py'
            }
            stash name: 'compiled-results', includes: 'sources/*.py*'
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error("${e}")
        }
    }

    stage('Test') {
        try {
            def pytestImage = docker.image('qnib/pytest')
            pytestImage.inside {
                sh 'py.test --verbose --junit-xml test-reports/results.xml sources/test_calc.py'
            }
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error("${e}")
        } finally {
            junit 'test-reports/results.xml'
        }
    }

    stage('Deliver') {
        try {
            def dockerImage = docker.image('cdrx/pyinstaller-linux:python2')
            def volumePath = "${WORKSPACE}/sources:/src"
            def buildPath = "${env.BUILD_ID}"
            def command = "pyinstaller -F add2vals.py"
            dockerImage.inside("-v ${volumePath} ${dockerImage} ${command}") {
                sh "docker run --rm -v ${volumePath} ${dockerImage} ${command}"
            }
            archiveArtifacts "${buildPath}/sources/dist/add2vals"
            sh "docker run --rm -v ${volumePath} ${dockerImage} 'rm -rf build dist'"
        } catch (Exception e) {
            currentBuild.result = 'FAILURE'
            error("${e}")
        }
    }
}
