FROM python:3

RUN mkdir -p /usr/src/app/
WORKDIR /usr/src/app/

COPY . /usr/src/app/
RUN pip install --no-cache-dir -r req.txt

ENV OPENWEATHERMAP_API_KEY="your_api_key"
ENV  WEATHERBIT_API_KEY="your_api_key"


EXPOSE 8080
ENTRYPOINT ["uvicorn", "server:app", "--host=0.0.0.0", "--port=8080"]