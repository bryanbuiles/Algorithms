package arrays

// https://www.hackerrank.com/challenges/append-and-delete/problem?h_r=internal-search
// append and delete

// AppendAndDelete ...
func AppendAndDelete(s string, t string, k int32) string {
	sizeS := len(s)
	sizeT := len(t)
	kInt := int(k)
	strYes := "Yes"
	strNo := "No"
	var size, index, diferentArrays int
	if s == t {
		if kInt%2 == 0 || sizeS*2 <= kInt {
			return strYes
		}
		return strNo
	}
	if sizeS > sizeT {
		size = sizeT
	} else {
		size = sizeS
	}
	for index = 0; index < size; index++ {
		if s[index] != t[index] {
			break
		}
	}
	if index == size && sizeS > sizeT {
		deletes := sizeS - sizeT
		if sizeT <= sizeS-sizeT {
			if deletes <= kInt { // eliminando
				return strYes
			}
		}
		if kInt%deletes == 0 && deletes != 1 {
			return strYes
		}
		return strNo
	}

	if index == size && sizeT > sizeS {
		deletes := sizeT - sizeS
		if kInt%deletes == 0 && deletes != 1 {
			return strYes
		}
		return strNo
	}
	diferentArrays = (sizeS - index) + (sizeT - index)
	if diferentArrays <= kInt {
		return strYes
	}
	return "No"
}
