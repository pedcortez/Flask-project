# build all the images
docker build -t pedrocortez/multi-client:latest -t pedrocortez/flask-app -f /Dockerfile


# Apply k8s config files

kubectl apply -f k8s   
kubectl set image deployments/flask-deployment client=pedrocortez/flask-app
