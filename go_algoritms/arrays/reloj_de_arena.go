// hacker rank problem 2D Array - DS

package arrays

// funcion para sumar cada 3 elemntos de la fila y guardar los valores intermedios del reloj
func sumRows(array []int32, dic map[int32]int32, contador int32, dicResult map[int32]int32) (int32, map[int32]int32, map[int32]int32) {
	var sumaArray, NumberRestar, contadorPrimerElementoRestar, contadorValoresIntermedios int32
	contadorValoresIntermedios = contador
	for index, numbers := range array {
		if contador >= 4 && contador <= 19 { // GUardo los valores intermedios en el dic
			if index > 0 && index < 5 {
				dicResult[contadorValoresIntermedios-4] = numbers
				contadorValoresIntermedios++
			}
		}
		if index > 2 {
			NumberRestar = array[contadorPrimerElementoRestar]
			contador++
			contadorPrimerElementoRestar++
		}
		sumaArray += numbers - NumberRestar
		if index >= 2 {
			dic[contador] = sumaArray // Agregando la suma de los 3 elemntos del dic
		}
	}
	contador++
	return contador, dic, dicResult
}

//  Funcio para sumar los resultados de los dic
func hourglassSum(arr [][]int32) int32 {
	var contador int32
	dic := make(map[int32]int32)
	dicResult := make(map[int32]int32)
	for i := 0; i < 6; i++ { // se hace por cada fila
		contador, dic, dicResult = sumRows(arr[i], dic, contador, dicResult)
	}
	var j, result int32
	result = -64
	for j = 0; j < 16; j++ { // comparando todos los valores del DICresult
		dicResult[j] += dic[j] + dic[j+8]
		if dicResult[j] > result {
			result = dicResult[j]
		}
	}
	return result
}
