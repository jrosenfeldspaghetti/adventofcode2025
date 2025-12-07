package main

import (
	"fmt"
	"os"
)

func part1() {
	// sampleInput := readInput("./sampleInput")
	// sampleJoltage := 0
	// for _, pack := range sampleInput {
	// 	sampleJoltage += absoluteBruteForce(pack)
	// }
	// if sampleJoltage != 357 {
	// 	panic(fmt.Sprintf("%d != 357", sampleJoltage))
	// }

	puzzleInput := readInput("./puzzleInput")
	puzzleJoltage := 0
	for _, pack := range puzzleInput {
		puzzleJoltage += absoluteBruteForce(pack)
	}
	fmt.Println(puzzleJoltage)
}

func absoluteBruteForce(pack string) int {
	foundMax := 0
	for i, battery := range pack {
		if i == len(pack)-1 {
			break
		}
		for _, nextBattery := range pack[i+1:] {
			joltage1 := int(battery) - '0'
			joltage2 := int(nextBattery) - '0'
			foundMax = max(foundMax, joltage1*10+joltage2)
		}
	}
	// append pack and answer to bruteforce_output.txt
	f, err := os.OpenFile("bruteforce_output.txt", os.O_APPEND|os.O_CREATE|os.O_WRONLY, 0644)
	if err != nil {
		fmt.Fprintf(os.Stderr, "error opening bruteforce_output.txt: %v\n", err)
	} else {
		fmt.Fprintf(f, "%s %d\n", pack, foundMax)
		f.Close()
	}
	return foundMax
}
