package main

import (
	"fmt"
	"log"
	"net/http"
)

func handler(w http.ResponseWriter, r *http.Request) {
	fmt.Println(r.URL.RawQuery)
	fmt.Fprintf(w, `
	 /\_/\  
	( o.o ) 
	 > ^ <
	
Success, you've made it!
You've successfully reached the backend server.


`)
}

func main() {
	http.HandleFunc("/", handler)
	log.Fatal(http.ListenAndServe(":80", nil))
}
