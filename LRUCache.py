"""

기본 nodeMap 형태 : nodeMap = {key: [value, count]}
func get : lru.get(key)
func put : lru.put(key, value)

"""

from collections import deque


class LRUCache:
    def __init__(self, maxCacheSize):
        """
        self에 nodeMap을 딕셔너리로 생성한다.
        self에 maxCacheSize를 int형으로 입력 받아 생성한다.
        """
        self.maxCacheSize = maxCacheSize
        self.nodeMap = {}
        self.deque = deque()

    def get(self, key):
        """
        nodeMap에 value값을 res에 저장한다.
        만약 res가 -1이 아니라면
            put(key, res) 함수 실행
        :return:

        """
        res = self.nodeMap.get(key, [-1, 0])[0]
        if res != -1:
            self.put(key, res)
        return res

    def put(self, key, value):
        """
        만약 key가 nodeMap에 있을 경우
            count에 1을 추가 : count += 1
            value는 value로 할당
        key가 nodeMap에 없을 경우
            새로운 캐시 생성 : nodeMap = {key: [value, 1]}
        deque에 key값 추가
        nodeMap의 길이가 maxCacheSize보다 클 때
            deque에서 맨 앞에 있는 값의 count를 -1
            만약 nodeMap에 맨 앞에 있는 값의 count가 0이라면
                nodeMap에서 삭제
        :param data:
        :return:

        """
        if key in self.nodeMap:
            self.nodeMap[key][1] += 1
            self.nodeMap[key][0] = value
        else:
            self.nodeMap[key] = [value, 1]
        self.deque.append(key)
        while len(self.nodeMap) > self.maxCacheSize:
            k = self.deque.popleft()
            self.nodeMap[k][1] -= 1
            if self.nodeMap[k][1] == 0:
                del self.nodeMap[k]
