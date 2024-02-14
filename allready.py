import subprocess
import time

def run_command(command):
    process = subprocess.Popen(command, stdout=subprocess.PIPE, stderr=subprocess.PIPE, shell=True)
    output, error = process.communicate()
    return output, error

# Run 'terraform plan'
terraform_plan_command = 'terraform plan'
output, error = run_command(terraform_plan_command)
print(output.decode())
print(error.decode())

# Run 'terraform apply eks-cluster.tf'
terraform_apply_command = 'terraform apply eks-cluster.tf'
output, error = run_command(terraform_apply_command)
print(output.decode())
print(error.decode())

# Run 'aws eks --region us-west-1 update-kubeconfig --name ems-eks-cluster'
update_kubeconfig_command = 'aws eks --region us-west-1 update-kubeconfig --name ems-eks-cluster'
output, error = run_command(update_kubeconfig_command)
print(output.decode())
print(error.decode())

# Wait for 30 seconds
time.sleep(30)

# Run 'kubectl get nodes'
get_nodes_command = 'kubectl get nodes'
output, error = run_command(get_nodes_command)
print(output.decode())
print(error.decode())

# Wait for 2 minutes (120 seconds)
time.sleep(120)

# Run 'kubectl create -f jenkins-pod.yml'
jenkins_pod_command = 'kubectl create -f jenkins-pod.yml'
output, error = run_command(jenkins_pod_command)
print(output.decode())
print(error.decode())

# Run 'kubectl create -f jenkins-service.yml'
jenkins_service_command = 'kubectl create -f jenkins-service.yml'
output, error = run_command(jenkins_service_command)
print(output.decode())
print(error.decode())
