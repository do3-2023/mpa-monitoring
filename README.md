# Project instructions

Take old project and implement monitoring / observability / dashboarding.

# Prerequisites to deploy:
- [SpinKube](https://www.spinkube.dev/docs/spin-operator/installation/installing-with-helm/]) => deploy the shim executor in the same namespace as the api, here ```kubectl apply -f https://github.com/spinkube/spin-operator/releases/download/v0.2.0/spin-operator.shim-executor.yaml -n mpa-backend'```
- kubectl

# Deploy the application

Please place yourself at the infra folder for the following commands:

## Deploy the database

```bash
kubectl apply -f database/infra/
```

## Deploy the api

```
kubectl apply -f api/
```

## Deploy the web application

```
kubectl apply -f web/
```

# Access the application :

You will need to forward the listening port of the web application to access it on [localhost:8080](http://localhost:8080).
```bash
kubectl port-forward $(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1) 8080:8080 -n mpa-frontend
```

The line `$(kubectl get pods -n mpa-frontend | tail -n 1 | cut -d ' ' -f 1)` simply gets the ip of the first (and in this case only) pod.


# Feedback

I had quite some trouble with wasm.
At first, I tried to convert my python file directly to a .wasm file using py2wasm. But even though Python is partially supported, dynamic libraries are not implemented in wasi. So I tried changing my code to use other libraries: I removed psycopg2 and used psyodbc and pandas to connect and collect the data of the database. However, to build this new .wasm file, it took over an hour and returned an error. Since it took so long, I didn't want to loose too much time debugging it, so I decided to create a new project from scratch with spin. I hesitatet to recreate the entire app because you need to create one component for each path the api is listening and it seemed like a lot of work for something so easy.
But, once I recreated the api with spin, I managed to build and run it without any trouble trhough spin.
I had some errors deploying it with kubectl tough, it said I didn't have a runtime for "spin" configured, but in another kubectl environment it worked fine.