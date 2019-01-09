from collections import deque

# 지하철역 클래스


class Station:
    def __init__(self, name):
        self.name = name
        self.neighbor = []

    def add_connection(self, another_station):
        if another_station not in self.neighbor:
            self.neighbor.append(another_station)
            another_station.neighbor.append(self)

    # 코드를 입력하세요.


# Breadth-First Search 알고리즘
def bfs(start, goal):
    previous = {}
    queue = deque()
    current = None

    previous[start.name] = None
    queue.append(start)
    while len(queue) != 0 and current != goal:
        current = queue.popleft()
        for nb in current.neighbor:
            if nb.name not in previous.keys():
                queue.append(nb)
                previous[nb.name] = current
    path = []
    if current == goal:
        while previous[current.name] != None:
            path.append(current)
            current = previous[current.name]
        path.append(start)
    return path
    # 코드를 입력하세요.


# 파일 읽기
stations = {}
in_file = open('stations.txt', encoding='utf-8')
for line in in_file:
    temp = line.split(' - ')
    for i in range(len(temp)):
        station_name = temp[i].strip()
        if station_name not in stations.keys():
            station = Station(station_name)
            stations[station_name] = station
    for j in range(1, len(temp)):
        station_name = temp[j].strip()
        before_station_name = temp[j - 1].strip()
        stations[station_name].add_connection(stations[before_station_name])
# 코드를 입력하세요

in_file.close()


# 테스트
start_name = "이태원"
goal_name = "잠원"

start = stations[start_name]
goal = stations[goal_name]

path = bfs(start, goal)
for station in path:
    print(station.name)
