pipeline {
  agent any
  stages {
    stage('Composer Install') {
      steps {
        sh '''chmod +x -R ${WORKSPACE}; 
              php -r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"
              php -r "if (hash_file(\'sha384\', \'composer-setup.php\') === \'756890a4488ce9024fc62c56153228907f1545c228516cbf63f885e036d37e9a59d27d63f46af1d4d07ee0f76181c7d3\') { echo \'Installer verified\'; } else { echo \'Installer corrupt\'; unlink(\'composer-setup.php\'); } echo PHP_EOL;"
              php composer-setup.php
              php -r "unlink(\'composer-setup.php\');"
              php composer.phar install'''
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

    stage('Unit Tests') {
      steps {
        sh 'php vendor/bin/phpunit --globals-backup --bootstrap tests/Unit/bootstrap.php tests/Unit --log-junit report_unit.xml'
      }
    }

    stage('Build App Container') {
      steps {
        sh '/usr/bin/docker build -t prestashop:${BRANCH_NAME}-${BUILD_ID} .docker'
      }
    }

    stage('Functional Tests') {
      steps {
        sh 'docker-compose up -d'
        sh 'wget -t 30 -w 10 ${SRV_QA}'
        sh 'python3 -m xmlrunner discover tests/Functional -o reports'
        sh 'docker-compose down -v'
        junit 'reports/TEST*.xml'
        junit 'report_unit.xml'
      }
    }

  }
  environment {
    SYMFONY_DEPRECATIONS_HELPER = 'weak'
    DISPLAY = ':1.5'
    SRV_QA = 'http://127.0.0.1:8001'
  }
}
