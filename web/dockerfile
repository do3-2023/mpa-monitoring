FROM denoland/deno:alpine-1.34.3

LABEL org.opencontainers.image.source="https://github.com/do3-2023/mpa-kube"

WORKDIR /app

USER deno

COPY deps.ts .

RUN deno cache deps.ts

ADD . .

EXPOSE 8080

RUN deno cache main.ts

CMD [ "run", "--allow-net", "--allow-read", "--allow-env", "main.ts" ]
