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

You will need to forward the listening port of the web application to access it on [localhost:8000](http://localhost:8000).
```bash
kubectl port-forward $(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1) 8000:8000 -n mpa-frontend
```

The line `$(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1)` simply gets the ip of the first (and in this case only) pod.


# Feedback

I had quite some trouble with wasm.
At first, I tried to convert my python file directly to a .wasm file using py2wasm. But even though Python is partially supported, dynamic libraries are not implemented in wasi. So I tried changing my code to use other libraries: I removed psycopg2 and used psyodbc and pandas to connect and collect the data of the database. However, to build this new .wasm file, it took over an hour and returned an error. Since it took so long, I didn't want to loose too much time debugging it, so I decided to create a new project from scratch with spin. I hesitatet to recreate the entire app because you need to create one component for each path the api is listening and it seemed like a lot of work for something so easy.
But, once I recreated the api with spin, I managed to build and run it without any trouble.