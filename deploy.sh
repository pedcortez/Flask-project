# build all the images
docker build -t pedrocortez/todo-app:latest -t pedrocortez/flask-app -f /Dockerfile


# Apply k8s config files

kubectl apply -f k8s   
kubectl set image deployments/todo-app client=pedrocortez/todo-app
