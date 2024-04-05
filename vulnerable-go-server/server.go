package main

import (
	"log"
	"net/http"
)

func main() {
	srv := &http.Server{Addr: ":8000", Handler: http.HandlerFunc(handle)}

	log.Printf("Serving on https://0.0.0.0:8000")
	log.Fatal(srv.ListenAndServeTLS("assets/server.crt", "assets/server.key"))
}

func handle(w http.ResponseWriter, r *http.Request) {
	log.Printf("Connection: %s %s", r.Proto, r.Header)
	w.Write([]byte("Hello"))
}
