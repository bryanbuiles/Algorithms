package otros

func pageCount(n int32, p int32) int32 {
	var i, contador, numberPages int32 = 0, 0, 0
	for i = 0; i <= n; i += 2 {
		if i == p || (i+1) == p {
			numberPages = contador
		}
		contador++
	}
	if (contador-1)-numberPages > numberPages {
		return numberPages
	}
	return (contador - 1) - numberPages
}
