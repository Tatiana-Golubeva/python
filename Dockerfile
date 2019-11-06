FROM python:3.7
ENV PYTHONUNBUFFERED=1

WORKDIR ./mysite
COPY requirments.txt .
RUN pip install --no-cache -r requirments.txt
EXPOSE 8000
CMD [ "/bin/bash", "mig.sh" ]
