package otros

import (
	"fmt"
	"math/big"
)

// ExtraLongFactorials ...
func ExtraLongFactorials(n int32) {

	var result big.Int
	number := int64(n)
	result.MulRange(1, number)
	str := result.String()
	fmt.Println(str)
}
