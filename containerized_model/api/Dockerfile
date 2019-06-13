FROM python:3.6

# make directories suited to your application 
RUN mkdir -p /home/project/app
#RUN mkdir -p /home/project/app/model
WORKDIR /home/project/app

# copy and install packages for flask
COPY requirements.txt /home/project/app
RUN pip install --no-cache-dir -r requirements.txt

# train and create the model
COPY iris_svm_train.py /home/project/app
RUN mkdir model && python /home/project/app/iris_svm_train.py

# copy app from your local to your docker container
COPY app.py /home/project/app

#CMD gunicorn -w 1 -b :8000 app:app
