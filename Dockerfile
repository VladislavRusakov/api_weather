FROM python:3.9.1

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r req.txt

EXPOSE 8000
ENTRYPOINT [ "./run.sh" ]