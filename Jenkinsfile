pipeline {
  agent any
  stages {
    stage('PHP Deps') {
      steps {
        sh 'composer install -n'
      }
    }

    stage('Core Install') {
      steps {
        sh 'php install-dev/index_cli.php --domain="localhost:8080" --db_user="alinuxien" --db_password="alinuxien" --email="ali.akrour@gmail.com" --password="alinuxien" --language="fr" --name="Don’t Feed The Groll"'
      }
    }

    stage('Javascript & CSS Deps') {
      steps {
        sh 'make assets'
      }
    }

    stage('All Unit Tests') {
      steps {
        sh 'composer test-all'
      }
    }

  }
}
