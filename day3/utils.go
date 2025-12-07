package main

import (
	"os"
	"strings"
)

func readInput(filename string) []string {
	file, _ := os.ReadFile(filename)
	return strings.Split(string(file), "\n")
}
