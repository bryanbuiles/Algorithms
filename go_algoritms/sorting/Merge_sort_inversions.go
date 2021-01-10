package sorting

var contador int64

func countInversions(arr []int32) {

	lenArr := int32(len(arr))
	var (
		left  []int32
		right []int32
	)
	if lenArr > 1 {
		mid := lenArr / 2

		left = append(left, arr[:mid]...)
		right = append(right, arr[mid:]...)
		countInversions(left)
		countInversions(right)

		var i, j, k int32
		lenL := int32(len(left))
		lenR := int32(len(right))
		for i < lenL && j < lenR {
			if left[i] < right[j] {
				arr[k] = left[i]
				i++
			} else {
				arr[k] = right[j]
				j++
			}
			k++
		}
		for i < lenL {
			arr[k] = left[i]
			i++
			k++
		}

		for j < lenR {
			arr[k] = right[j]
			j++
			k++
		}
	}
}
