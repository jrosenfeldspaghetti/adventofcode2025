package main

import (
	"fmt"
	"strconv"
)

func part1() {
	s := session{currentPosition: 50}
	turns := receiveInput("./sampleInput")
	for _, turn := range turns {
		direction := turn[:1]
		rotation, _ := strconv.Atoi(turn[1:])
		s.processDial(direction, rotation)
	}
	fmt.Println(s.actualPassword)
}

func (s *session) processDial(direction string, rotation int) {
	if direction == "L" {
		postRotation := (s.currentPosition - rotation) % 100
		s.currentPosition = postRotation
	} else {
		s.currentPosition = (s.currentPosition + rotation) % 100
	}
	if s.currentPosition == 0 {
		s.actualPassword++
	}
}
