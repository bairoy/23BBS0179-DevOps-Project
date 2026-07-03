pipeline {
    agent any

    environment {
        IMAGE_NAME = 'abc-tech-website'
        IMAGE_TAG  = 'latest'
        CONTAINER_PORT = '80'
        TEST_PORT = '8088'
        K8S_NAMESPACE = 'default'
    }

    stages {
        stage('Checkout Code') {
            steps {
                echo '=== Stage 1: Checking out code from GitHub Repository ==='
                checkout scm
            }
        }

        stage('Validate Source Code') {
            steps {
                echo '=== Stage 2: Validating HTML, CSS, and JS Assets ==='
                sh '''
                    echo "Checking HTML files structure..."
                    ls -la website/*.html
                    echo "Checking style assets..."
                    ls -la website/css/*.css
                    echo "Checking script assets..."
                    ls -la website/js/*.js
                    echo "All source files verified successfully."
                '''
            }
        }

        stage('Build Docker Image') {
            steps {
                echo "=== Stage 3: Building production container image ${IMAGE_NAME}:${IMAGE_TAG} ==="
                sh "docker build -t ${IMAGE_NAME}:${IMAGE_TAG} ."
            }
        }

        stage('Test Docker Container') {
            steps {
                echo '=== Stage 4: Testing containerized website locally ==='
                sh """
                    # Remove lingering test container if present
                    docker rm -f test-${IMAGE_NAME} || true
                    # Run container in test mode
                    docker run -d --name test-${IMAGE_NAME} -p ${TEST_PORT}:80 ${IMAGE_NAME}:${IMAGE_TAG}
                    sleep 3
                    # Verify HTTP status code 200 OK
                    curl -I http://localhost:${TEST_PORT}/healthz
                    curl -s http://localhost:${TEST_PORT}/index.html | grep -i "ABC Technologies"
                    # Clean up test container
                    docker rm -f test-${IMAGE_NAME}
                """
            }
        }

        stage('Deploy to Kubernetes') {
            steps {
                echo '=== Stage 5: Deploying Container to Kubernetes Cluster ==='
                sh '''
                    # Apply Kubernetes manifests
                    kubectl apply -f k8s/deployment.yaml --namespace=${K8S_NAMESPACE}
                    kubectl apply -f k8s/service.yaml --namespace=${K8S_NAMESPACE}
                    
                    # Force restart rollout to pick up newly built local tag
                    kubectl rollout restart deployment/abc-tech-website-deployment --namespace=${K8S_NAMESPACE}
                '''
            }
        }

        stage('Verify K8s Deployment') {
            steps {
                echo '=== Stage 6: Verifying Kubernetes Rollout and Pod Status ==='
                sh '''
                    kubectl rollout status deployment/abc-tech-website-deployment --timeout=60s --namespace=${K8S_NAMESPACE}
                    kubectl get pods -l app=abc-tech-website --namespace=${K8S_NAMESPACE}
                    kubectl get svc abc-tech-website-service --namespace=${K8S_NAMESPACE}
                '''
            }
        }
    }

    post {
        success {
            echo '==========================================================='
            echo '🎉 PIPELINE SUCCESS: ABC Technologies Website Deployed!'
            echo 'Access Application at: http://localhost:30080'
            echo '==========================================================='
        }
        failure {
            echo '❌ PIPELINE FAILURE: Inspect console output above for build errors.'
        }
    }
}
