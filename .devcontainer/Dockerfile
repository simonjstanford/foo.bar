FROM python:2.7

# Trick for getting file ownership right in bind-mounted docker volumes
ARG UNAME=user
ARG UID=1000
ARG GID=1000

RUN apt-get update && export DEBIAN_FRONTEND=noninteractive \
    && apt-get -y install --no-install-recommends \
    vim nano \
    git


RUN groupadd -g $GID $UNAME && \
    useradd -m -u $UID -g $GID -s /bin/bash $UNAME

# Include the next two lines if you are debugging the Dockerfile
#RUN apt list --installed | grep zip
#RUN pip3 list

USER ${UNAME}