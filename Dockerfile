# Pull base image
FROM python:3.8-slim 

LABEL maintainer="Joseph Anyetei Sowah" 

# Set environment variables
ENV PYTHONDONTWRITEBYTECODE 1
ENV PYTHONUNBUFFERED 1

# Set work directory
WORKDIR /payment_api



# Install dependencies:
COPY requirements.txt . /payment_api/
RUN pip3 install -r requirements.txt



# Copy project
COPY . /payment_api/

EXPOSE 5000

CMD python app.py 0.0.0.0:5000