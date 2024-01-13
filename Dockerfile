# pull official base image
FROM rayproject/ray:nightly-py311
# install requirements.txt
COPY requirements.txt /tmp/
RUN pip install --requirement /tmp/requirements.txt
# set work directory
WORKDIR /serve_app
# set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1
# Copy App foler into workdir
COPY app /serve_app/app