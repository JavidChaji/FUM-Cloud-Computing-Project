kubectl delete secret  sakila-database-secret
kubectl delete configmap sakila-database-configmap
kubectl delete db-network-networkpolicy 
kubectl delete network reverse-proxy-network-networkpolicy 
kubectl delete deploy sakila-database-deployment
kubectl delete deploy sakila-manager-deployment
kubectl delete deploy ping-pong-application-deployment
kubectl delete deploy reverse-proxy-deployment
