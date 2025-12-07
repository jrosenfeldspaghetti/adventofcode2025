package main

import (
	"fmt"
	"strconv"
	"strings"
)

func part2() {
	sampleInput := readInput("./sampleInput")
	sampleJoltage := calculateLargestJoltage(sampleInput)
	if sampleJoltage != 3121910778619 {
		panic(fmt.Sprintf("%d != 3121910778619", sampleJoltage))
	}
	puzzleInput := readInput("./puzzleInput")
	puzzleJoltage := calculateLargestJoltage(puzzleInput)
	fmt.Println(puzzleJoltage)
}

func calculateLargestJoltage(packs []string) int {
	joltages := []int{}
	for _, batteryPack := range packs {
		idPointer := 11
		pointers := []int{}
		currentOffset := 0

		for idPointer >= 0 {
			highestI := findMaxIndex(batteryPack, currentOffset, len(batteryPack)-idPointer)
			currentOffset = highestI + 1
			idPointer--
			pointers = append(pointers, highestI)
		}

		var digits strings.Builder
		for _, i := range pointers {
			digits.WriteByte(batteryPack[i])
		}
		num, err := strconv.Atoi(digits.String())
		if err != nil {
			panic(err)
		}

		joltages = append(joltages, num)
	}
	sum := 0
	for _, joltage := range joltages {
		sum += joltage
	}
	return sum
}

func findMaxIndex(pack string, start, end int) int {
	if start >= end {
		return start
	}

	maxIdPointer := start
	maxVal := pack[start]
	for i := start + 1; i < end; i++ {
		if pack[i] > maxVal {
			maxVal = pack[i]
			maxIdPointer = i
		}
	}
	return maxIdPointer
}
