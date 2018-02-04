class Solution:
    def killProcess(self, pid, ppid, kill):
        """
        https://leetcode.com/problems/kill-process/description/
        :type pid: List[int]
        :type ppid: List[int]
        :type kill: int
        :rtype: List[int]
        """
        l = {}
        for i in range(len(ppid)):
            k = l.get(ppid[i], [])
            k.append(pid[i])
            l[ppid[i]] = k
        ret = [kill]
        for i in ret:
            ret.extend(l.get(i,[]))
        return ret
