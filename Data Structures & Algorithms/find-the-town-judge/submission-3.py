class Solution:
    def findJudge(self, n: int, trust: List[List[int]]) -> int:
        # if everyone trusts same person -> judge
        # must only be one person all trust
        # the person that everyone trusts must not trust anyone else
        incoming_point = defaultdict(int)
        outgoing_point = defaultdict(int)

        for (person, trusted) in trust:
            outgoing_point[person] += 1
            incoming_point[trusted] += 1

        for i in range(1, n+1):
            if outgoing_point[i] == 0 and incoming_point[i] == n - 1:
                return i
        return -1