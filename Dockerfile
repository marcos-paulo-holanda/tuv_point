FROM python:3.9-slim

# Instalar dependências
RUN apt-get update && apt-get install -y \
    cron \
    wget \
    unzip \
    gnupg \
    ca-certificates \
    tzdata \
    && rm -rf /var/lib/apt/lists/*

# Adicionar o repositório do Google Chrome e a chave GPG
RUN wget -q -O - https://dl.google.com/linux/linux_signing_key.pub | apt-key add - \
    && sh -c 'echo "deb [arch=amd64] http://dl.google.com/linux/chrome/deb/ stable main" > /etc/apt/sources.list.d/google-chrome.list'

# Atualizar os pacotes novamente e instalar o Google Chrome
RUN apt-get update && apt-get install -y google-chrome-stable

# Instalar o ChromeDriver
RUN wget -O /tmp/chromedriver.zip https://chromedriver.storage.googleapis.com/$(wget -qO- https://chromedriver.storage.googleapis.com/LATEST_RELEASE)/chromedriver_linux64.zip \
    && unzip /tmp/chromedriver.zip chromedriver -d /usr/local/bin/ \
    && rm /tmp/chromedriver.zip

# Definir o fuso horário para Brasília
ENV TZ=America/Sao_Paulo
RUN ln -snf /usr/share/zoneinfo/$TZ /etc/localtime && echo $TZ > /etc/timezone

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
