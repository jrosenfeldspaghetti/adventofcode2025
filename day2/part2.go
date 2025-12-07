package main

import (
	"fmt"
	"strconv"
	"strings"

	"github.com/dlclark/regexp2"
)

func part2() {
	sampleOutput := doingTheThingWithRegex("./sampleInput")
	if sampleOutput != 4174379265 {
		panic(fmt.Sprintf("%d != 4174379265", sampleOutput))
	}

	puzzleOutput := doingTheThingWithRegex("./puzzleInput")
	fmt.Println(puzzleOutput)
}

func doingTheThingPart2(filename string) int {
	ranges := readInput(filename)
	totalSum := 0
	for _, r := range ranges {
		indexOfDash := strings.Index(r, "-")
		start, _ := strconv.Atoi(r[:indexOfDash])
		end, _ := strconv.Atoi(r[indexOfDash+1:])
		for i := start; i <= end; i++ {
			iAsStr := strconv.Itoa(i)
			pattern := ""
			for index, char := range strings.Split(iAsStr, "") {
				if len(iAsStr)-(index+1) < len(pattern) {
					break
				}
				pattern += char
				if strings.Repeat(pattern, len(iAsStr[index+1:])/len(pattern)) == iAsStr[index+1:] {
					totalSum += i
					break
				}
			}
		}
	}

	return totalSum
}

func doingTheThingWithRegex(filename string) int {
	ranges := readInput(filename)
	totalSum := 0
	pattern := `^(\d+)\1+$`
	compiledPattern, _ := regexp2.Compile(pattern, 0)
	for _, r := range ranges {
		indexOfDash := strings.Index(r, "-")
		start, _ := strconv.Atoi(r[:indexOfDash])
		end, _ := strconv.Atoi(r[indexOfDash+1:])
		for i := start; i <= end; i++ {
			iAsStr := strconv.Itoa(i)
			matched, _ := compiledPattern.MatchString(iAsStr)
			if matched {
				totalSum += i
			}

		}
	}

	return totalSum
}
