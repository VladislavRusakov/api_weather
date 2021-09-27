To build docker image:
1. enter your API keys into dockerfile
2. docker build -t api .
3. docker run -it -p 8080:8080 api

Go to your browser. You can enter city name into frontend form, or you can use :8080/api/moscow (or any other city, you want)
