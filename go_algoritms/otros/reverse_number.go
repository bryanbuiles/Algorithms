package otros

// hack rank Beautiful Days at the Movies
// Calcule el numero de dias bonitos divisibles por k.
// los dias bontos son el resultado de la resta del numero menos su reverso

// BeautifulDays ...
func BeautifulDays(i int32, j int32, k int32) int32 {
	var contador, numero int32
	for numero = i; numero <= j; numero++ {
		numberReversed := reverseInt(numero)
		resta := numero - numberReversed
		if resta < 0 {
			resta *= -1
		}
		if resta%k == 0 {
			contador++
		}
	}

	return contador
}

// funcion para reversar integers, va tomando de digito en digito
// ejemplo 230 luego 23 luego 2 y asi con terminar los digitos mientras va
// reversando el residuo
func reverseInt(number int32) int32 {
	var reversed, residuoDigit int32
	reversed = 0
	for number != 0 {
		residuoDigit = (number % 10)          // residuo
		reversed = reversed*10 + residuoDigit // reversa el residuo
		number = (number / 10)                // pasa al siguiente digito
	}
	return reversed
}
