FROM ubuntu:latest
RUN apt-get update && apt-get install -y curl
WORKDIR /app
RUN mkdir -p /app/logs
COPY src/monitor.sh /app/monitor.sh
RUN chmod +x /app/monitor.sh
CMD ["/app/monitor.sh"]
