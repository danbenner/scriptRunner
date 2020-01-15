package main

import (
	"fmt"
	"log"
	"os"
	"os/exec"
	"path/filepath"
)

func main() {
	goPath := os.Getenv("GOPATH")
	dir, err := os.Getwd()
	if err != nil {
		log.Fatal(err)
	}
	scriptPath := filepath.Join(goPath, "src", "scriptRunner/scripts/connect.py")
	log.Println("Generating load files for Medicaid LOB...")
	log.Println("Scriptpath: " + scriptPath)
	c := exec.Command("/usr/local/bin/python", scriptPath, "--output="+dir)
	err = c.Run()
	if err != nil {
		fmt.Printf("ERROR: %v\n", err.Error())
		log.Fatal(err)
	}
}
