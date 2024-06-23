FROM public.ecr.aws/docker/library/python:3.9.16-bullseye
WORKDIR /rest_n_link
RUN apt-get update && apt-get install -y gcc python3-dev python3-pip
COPY requirements.txt requirements.txt
RUN pip3 install -r requirements.txt
COPY . .
CMD [ "python3", "-m" , "flask", "run", "--host=0.0.0.0"]