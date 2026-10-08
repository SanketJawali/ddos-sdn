FROM iwaseyusuke/mininet:latest

WORKDIR /app

# MiniEdit env config
ENV DEBIAN_FRONTEND=noninteractive
ENV TZ=Asia/Kolkata

# Install pip
RUN apt-get update && \
    apt-get install -y python3-pip && \
    apt-get install -y python3-tk && \
    rm -rf /var/lib/apt/lists/*

COPY requirements.txt .
RUN pip install -r requirements.txt

# Edit the entrypoint from base image. Enables us to execute python after image is run.
# Without this we need to run the main.py file manually inside the container shell.
COPY entrypoint.sh /entrypoint.sh
RUN chmod +x /entrypoint.sh

COPY . .

ENTRYPOINT ["/entrypoint.sh"]
CMD ["python3", "main.py"]
