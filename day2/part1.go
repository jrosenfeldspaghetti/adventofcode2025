package main

import (
	"fmt"
	"strconv"
	"strings"
)

// basically we want to split the word in half and check the
// two sides are equal, but I think we really want to avoid
// iterating through each range.
func part1() {
	sampleOutput := doingTheThing("./sampleInput")
	if sampleOutput != 1227775554 {
		panic("sampleOutput != 1227775554")
	}

	puzzleOutput := doingTheThing("./puzzleInput")
	fmt.Println(puzzleOutput)
}

func doingTheThing(filename string) int {
	ranges := readInput(filename)
	totalSum := 0
	for _, r := range ranges {
		indexOfDash := strings.Index(r, "-")
		start, _ := strconv.Atoi(r[:indexOfDash])
		end, _ := strconv.Atoi(r[indexOfDash+1:])
		for i := start; i <= end; i++ {
			numberOfDigits := len(strconv.Itoa(i))
			if numberOfDigits%2 != 0 {
				continue
			}
			iAsStr := strconv.Itoa(i)
			firstHalf := iAsStr[:numberOfDigits/2]
			secondHalf := iAsStr[numberOfDigits/2:]
			if firstHalf == secondHalf {
				totalSum += i
			}
		}
	}

	return totalSum
}
