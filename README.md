# My CI/CD project

![image](https://github.com/tomerkul/tomerkul-myflaskproject-k8s/assets/91198141/c5920bdc-bb40-4022-8186-c87ed74ae75d)



This Jenkins pipeline automates the deployment process for a Flask application and related infrastructure. Here's a description of each stage:

 Cleanup: This stage performs cleanup by deleting all files in the current workspace directory. It's a preparation step to ensure a clean environment for the subsequent tasks.

 Clone: In this stage, the pipeline clones a Git repository from https://github.com/tomerkul/tomerkul-myflaskproject-k8s.git. It's a common practice to retrieve the source code or application files for further processing.

 Upload to Docker Hub: This stage restarts the Docker service and runs Python scripts to manage Docker images. It cleans up old versions, determines the latest version, and presumably builds and uploads Docker images to Docker Hub.

 Upload to Testing Server: This stage involves Kubernetes and Helm operations. It configures the Kubernetes context to 'rancher-desktop' and packages Helm charts. The Helm repository index is updated, and the charts are copied to a Google Cloud Storage bucket. The pipeline then deploys the application and performs tests on it.

 Preparing Cluster: This stage uses Terraform to initialize, refresh, and apply infrastructure changes. It prepares the target cluster for deployment.

 Confirmation: This is an interactive stage where a manual confirmation is required to proceed with the deployment. It prompts the user for confirmation.

 Deploy: In this final stage, the pipeline orchestrates the deployment of the Flask application to a Kubernetes cluster. It manages updates to a CD Git repository - https://github.com/tomerkul/deployment.git containing the Helm chart. This stage is crucial for continuous delivery as it triggers ArgoCD, which monitors changes in the Git repository. When changes are detected, ArgoCD automatically synchronizes with the updated repository, ensuring that the latest version of the application is deployed to the Google Cloud cluster. This process streamlines continuous integration and delivery, ensuring that the production environment is always up to date with the latest application version.

This pipeline automates the deployment of a Flask application, manages Docker images, and orchestrates infrastructure changes using Kubernetes and Terraform. It includes safety measures like manual confirmation and checks for changes before deployment.




