FROM pytorch/torchserve:latest

ADD /model-store /app/model-store
ADD /serve /app/serve

EXPOSE 8080 8081 8082

ENTRYPOINT ["torchserve"]
