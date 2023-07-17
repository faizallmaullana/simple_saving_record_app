FROM python:3-alpine3.15
WORKDIR /home/tanjung/Desktop/app
COPY . /home/tanjung/Desktop/app
RUN pip install --upgrade pip
RUN python -m pip install alembic==1.10.4
RUN python -m pip install Flask==2.3.2
RUN python -m pip install Flask==2.0.1
RUN python -m pip install Flask_Cors==4.0.0
RUN python -m pip install Flask_Migrate==4.0.4
RUN python -m pip install Flask_RESTful==0.3.9
RUN python -m pip install flask_sqlalchemy==3.0.5
RUN python -m pip install pytz==2022.1
RUN python -m pip install SQLAlchemy==2.0.13
RUN python -m pip install SQLAlchemy==2.0.19

ENV FLASK_APP=app.py
ENV FLASK_ENV=development

CMD flask run --host 0.0.0.0

EXPOSE 5000