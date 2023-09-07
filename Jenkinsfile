pipeline {
    agent any
    stages {
        stage('Test') {
            steps {
                echo "build done ..."
                bat """
                    start cmd.exe /c
                    docker run -d -v D:/AUTOMATION_Pracice/Reports/report:/app/Allurerp cont_2
                    """
            }
        }
    }
}
