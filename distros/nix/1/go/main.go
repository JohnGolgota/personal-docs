package main

import (
	"fmt"
	"os/exec"
	"net/http"
)

func handle(w http.ResponseWriter, r *http.Request) {
	dir := r.URL.Query().Get("dir")
	if dir == "" {
		http.Error(w, "Missing 'dir' query parameter", http.StatusBadRequest)
		return
	}
	cmd := exec.Command("ls", "-l")
	cmd.Dir = dir
	out, err := cmd.CombinedOutput()
	if err != nil {
		http.Error(w, err.Error(), http.StatusInternalServerError)
		return
	}
	fmt.Fprintf(w, "<pre>%s</pre><br><a href=\"?dir=%s\">Back</a>", out, dir)
}

func main() {
	http.HandleFunc("/", func(w http.ResponseWriter, r *http.Request) {
		fmt.Fprintf(w, "Hello, world!")
	})
	http.HandleFunc("/list", handle)
	http.ListenAndServe(":8080", nil)
}