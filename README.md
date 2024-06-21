# Project instructions

Take old project and implement monitoring / observability / dashboarding.


# Push the docker image to ghcr

## login to ghcr

```bash
docker login ghcr.io -u USERNAME
```

## build image

```bash
cd web
docker build -t ghcr.io/do3-2023/mpa-kube/<web/api>:<version> .
```

## test image

```bash
docker run -itp 8080:8080 ghcr.io/do3-2023/mpa-kube/<web/api>:<version>
```

## Push on repo github

```bash
docker push ghcr.io/do3-2023/mpa-kube/<web/api>:<version>
```

# Deploy the application

Please place yourself at the root folder for the following commands.

## Deploy the database

```bash
kubectl apply -f database/infra
```

## Deploy the api

```
kubectl apply -f api/infra
```

## Deploy the web application

```
kubectl apply -f web/infra
```

# Access the application :

You will need to forward the listening port of the web application to access it on [localhost:8080](http://localhost:8080).
```bash
kubectl port-forward $(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1) 8080:8080 -n mpa-frontend
```

The line `$(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1)` simply gets the ip of the first (and in this case only) pod.


