class Solution:
    def tribonacci(self, n: int) -> int:
        dis = {}
        dis['0'] = 0
        dis['1'] = 1
        dis['2'] = 1

        def get_t(nn):
            if str(nn) not in dis.keys():
                dis[str(nn)] = get_t(nn-3)+get_t(nn-2)+get_t(nn-1)
            return dis[str(nn)]
        return get_t(n)