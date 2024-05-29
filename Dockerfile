FROM python:3.9-slim

# Instalar dependências
RUN apt-get update && apt-get install -y \
    cron \
    wget \
    unzip \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Definir o fuso horário para Brasília
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

# Instalar o Chrome e o ChromeDriver
RUN wget https://dl.google.com/linux/direct/google-chrome-stable_current_amd64.deb \
    && apt-get install -y ./google-chrome-stable_current_amd64.deb \
    && rm google-chrome-stable_current_amd64.deb

RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Adicionar o script Python ao contêiner
COPY script.py /app/script.py

# Adicionar o crontab ao contêiner
COPY crontab /etc/cron.d/my-cron-job

# Dar permissão de execução ao crontab
RUN chmod 0644 /etc/cron.d/my-cron-job

# Aplicar o crontab
RUN crontab /etc/cron.d/my-cron-job

# Executar o cron no foreground (requisito do Docker)
CMD ["cron", "-f"]
