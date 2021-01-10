#!/usr/bin/env groovy
pipeline {
  agent {
        node {
            label 'ec2-linux-instance'
        }
    }

  stages {
    stage("Build") {
      steps {
        echo "inside build"
      }
    }

    stage("Testing") {
      parallel {
        stage("Unit Tests") {
          steps {
            echo "inside unit tests"
			
          }
        }
        stage("Functional Tests") {
          steps {
            echo "inside functional tests"
          }
        }
        stage("Integration Tests") {
          steps {
            echo "inside integration tests"
          }
        }
      }
    }

    stage("Deploy") {
      steps {
        echo "Deploy!"
      }
    }
  }
}
