def binary_search( list, item ):
	low = 0
	high = len( list ) - 1
	while low <= high:
		mid = int( ( low + high ) / 2 )
		guess = list[ mid ]
		print( guess )
		if guess == item:
			return mid
		elif guess > item:
			high = mid - 1
		else:
			low = mid + 1


binary_search( [ 1, 2, 3, 4, 5, 6, 7, 8, 9 ], 1 )
