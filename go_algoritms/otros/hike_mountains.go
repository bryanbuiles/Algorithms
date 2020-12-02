package otros

func countingValleys(steps int32, path string) int32 {
	var contador, valleyCount int32
	for index, letter := range path {
		if letter == 'U' {
			contador++
		} else {
			contador--
		}
		if contador == 0 && path[index] == 'U' {
			valleyCount++
		}
	}
	return valleyCount
}
