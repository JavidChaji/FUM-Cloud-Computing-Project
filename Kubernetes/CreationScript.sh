kubectl apply -f sakila-database-secret.yaml
kubectl apply -f sakila-database-configmap.yaml
kubectl apply -f db-network-networkpolicy.yaml 
kubectl apply -f reverse-proxy-network-networkpolicy.yaml 
kubectl apply -f sakila-database-deployment.yaml 
kubectl apply -f sakila-manager-deployment.yaml 
kubectl apply -f ping-pong-application-deployment.yaml 
kubectl apply -f reverse-proxy-deployment.yaml
