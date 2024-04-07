FROM golang:1.19
WORKDIR /app

COPY go.mod ./
COPY . .

RUN mkdir assets
RUN cd assets; openssl req -newkey rsa:4096 -nodes -keyout server.key -x509 -days 365 -out server.crt -subj "/C=DE/ST=Munich/L=Munich/O=Security/OU=IT/CN=poc"

RUN go build -o main .

CMD ["./main"]
