FROM golang:1.19
WORKDIR /app

COPY go.mod ./
COPY . .
RUN go build -o main .

CMD ["./main"]