export KUBECONFIG=$(pwd)/kubeconfig_aussrc-radec-cluster
helm repo add jupyterhub https://jupyterhub.github.io/helm-chart/
helm repo update
helm install jupyterhub jupyterhub/jupyterhub -f jupyterhub/config.yml -n jupyter --timeout 500s