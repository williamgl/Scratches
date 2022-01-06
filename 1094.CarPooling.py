#def carPooling(self, trips, capacity: int) -> bool:

trips = [[2, 1, 5], [3, 3, 7]]
capacity = 4
to = trips[-1][2]
stop = [0] * (to + 1)

for i in trips:
    for j in range(stop[i[1]], stop[i[2]]):
        stop[i[1]] += i[0]

for i in stop:
    if i > capacity:
        print('F')
