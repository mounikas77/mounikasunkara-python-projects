# jan_7(trick-1)
# nested data structure into single data structure
# 1.[[1,2,3],[4,5,6]]
#print(sum([[1,2,3],[4,5,6]],[]))
#o/p:[1,2,3,4,5,6]
# 2.((1,2),(3,4),(4,5))
# print(sum(((1,2),(3,4),(4,5)),()))
# o/p:(1, 2, 3, 4, 4, 5)
# 3.{(1,2),(4,5)}
#print(sum({(1,2),(4,5)},()))
# 4.[([1,2],[6,3])]
# print(sum([([1,2],[6,3])],()))
# o/p:([1, 2], [6, 3])
# print(sum(([1,2],[6,3]),[]))
# o/p:[1, 2, 6, 3]
###############
#trick-2