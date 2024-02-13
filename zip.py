X = ["a", "b", "c", "d", "e", "f", "g", "h", "i"]
Y = [0,   1,   1,    0,   1,   2,   2,   0,   1]
zipped_pairs = zip(X,Y)
print(sorted(zipped_pairs))
#print( [_ for _, x in sorted(zipped_pairs)])
#print(z)