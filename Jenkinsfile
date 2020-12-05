pipeline {
  agent any
  stages {
    stage('Composer Install') {
      steps {
        sh '''php -r "copy(\'https://getcomposer.org/installer\', \'composer-setup.php\');"
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
        sh 'php vendor/bin/phpunit --globals-backup --bootstrap tests/Unit/bootstrap.php tests/Unit'
      }
    }

  }
}