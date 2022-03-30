graph = { "a": { "b": 6, "c": 2 }, "b": { "d": 1 }, "c": { "b": 3, "d": 5 }, "d": {} }


def find_shortest_path( graph, source="a", destination="d" ):
	infinity = float( "inf" )
	cost = { source: 0, destination: infinity }
	parent = {}
	node = source
	while node != None:
		
