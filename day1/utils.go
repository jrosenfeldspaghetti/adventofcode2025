package main

import "os"

type session struct {
	currentPosition int
	actualPassword  int
}

func receiveInput(filename string) []string {
	file, _ := os.ReadFile(filename)
	out := []string{}
	currentInput := ""
	for _, rawOut := range file {
		stringOut := string(rawOut)
		if stringOut == "\n" {
			out = append(out, currentInput)
			currentInput = ""
			continue
		}
		currentInput += stringOut
	}
	out = append(out, currentInput)
	return out
}
