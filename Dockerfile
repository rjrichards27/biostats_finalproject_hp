# See here for image contents: https://github.com/microsoft/vscode-dev-containers/tree/v0.245.2/containers/python-3/.devcontainer/base.Dockerfile

# [Choice] Python version (use -bullseye variants on local arm64/Apple Silicon): 3, 3.10, 3.9, 3.8, 3.7, 3.6, 3-bullseye, 3.10-bullseye, 3.9-bullseye, 3.8-bullseye, 3.7-bullseye, 3.6-bullseye, 3-buster, 3.10-buster, 3.9-buster, 3.8-buster, 3.7-buster, 3.6-buster
# ARG VARIANT="3.10-bullseye"
# FROM mcr.microsoft.com/vscode/devcontainers/python:0-${VARIANT}

# # [Choice] Node.js version: none, lts/*, 16, 14, 12, 10
# ARG NODE_VERSION="none"
# RUN if [ "${NODE_VERSION}" != "none" ]; then su vscode -c "umask 0002 && . /usr/local/share/nvm/nvm.sh && nvm install ${NODE_VERSION} 2>&1"; fi

# FROM python:3.10-bullseye

# RUN mkdir -p /app
# COPY . main.py /app/
# WORKDIR /app
# RUN pip install -r requirements.txt
# EXPOSE 8080
# CMD [ "main.py" ]
# ENTRYPOINT [ "python" ]

# [Optional] If your pip requirements rarely change, uncomment this section to add them to the image.
# COPY requirements.txt /tmp/pip-tmp/
# RUN pip3 --disable-pip-version-check --no-cache-dir install -r /tmp/pip-tmp/requirements.txt \
#    && rm -rf /tmp/pip-tmp

# [Optional] Uncomment this section to install additional OS packages.
# RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
#     && apt-get -y install --no-install-recommends <your-package-list-here>

# [Optional] Uncomment this line to install global node packages.
# RUN su vscode -c "source /usr/local/share/nvm/nvm.sh && npm install -g <your-package-here>" 2>&1

# FROM python:3.10.8-slim-bullseye
# FROM public.ecr.aws/lambda/python:3.9.2022.12.02.20, keeping this one in case if needed
# FROM public.ecr.aws/lambda/python:3.8
# FROM public.ecr.aws/lambda/python:3.10.8
# FROM public.ecr.aws/lambda/python:3.11-preview.2023.04.17.20
FROM public.ecr.aws/lambda/python:3.9
# RUN mkdir -p /app
RUN mkdir -p /app /app/templates
COPY src/templates/*.html /app/templates/
COPY . appX.py /app/
RUN ls -la /app
# COPY . src/templates/*.html /app/templates/
# COPY . src/*.py /app/
# COPY . src/templates/*.html /app/templates/
# COPY . appX.py /app/
# WORKDIR /app
WORKDIR /app
RUN pip install -r requirements.txt
# WORKDIR /app/src
ENV PORT=8080
EXPOSE 8080
CMD [ "appX.py" ]
ENTRYPOINT [ "python" ]
# CMD ["python", "app.py"]