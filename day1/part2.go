package main

import (
	"fmt"
	"os"
	"strconv"
)

func part2() {
	turns := receiveInput("./sampleInput")
	sampleSession := session{currentPosition: 50}

	for _, turn := range turns {
		direction := turn[:1]
		rotation, _ := strconv.Atoi(turn[1:])

		sampleSession.processClicks(direction, rotation)
	}
	if sampleSession.actualPassword != 6 {
		fmt.Println("Sample input failed. Output should be 6 but is", sampleSession.actualPassword)
		os.Exit(1)
	}

	turns = receiveInput("./puzzleInput")
	puzzleSession := session{currentPosition: 50}

	for _, turn := range turns {
		direction := turn[:1]
		rotation, _ := strconv.Atoi(turn[1:])

		puzzleSession.processClicks(direction, rotation)
	}
	fmt.Println(puzzleSession.actualPassword)
}

func (s *session) processClicks(direciton string, rotation int) {
	scalar := 1
	if direciton == "L" {
		scalar = -1
	}
	s.actualPassword += (rotation / 100)

	for c := 0; c < rotation%100; c++ {
		s.currentPosition = (s.currentPosition + scalar) % 100
		if s.currentPosition == 0 {
			s.actualPassword++
		}
	}
}
