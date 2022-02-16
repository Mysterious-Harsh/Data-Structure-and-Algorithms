# Fastest sorting algorithm with time complexity O(n*log n)
def quicksort( array ):
	if len( array ) < 2:
		return array
	else:
		pivot = array.pop( int( len( array ) / 2 ) )
		less = [ x for x in array if x <= pivot ]
		greater = [ x for x in array if x > pivot ]
		return quicksort( less ) + [ pivot ] + quicksort( greater )


print( quicksort( [ 5, 64, 7, 2, 1 ] ) )
