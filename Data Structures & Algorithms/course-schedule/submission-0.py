from collections import deque
class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        
        #Where are going to use khan's algo for this uisng bfS

        n=len(prerequisites)
        adj=[[] for  _ in range(numCourses)]
        in_degree=[0]*numCourses

        for x,y in prerequisites:
            adj[y].append(x)
            in_degree[x]+=1

    
        queue=deque()

        for i in range(numCourses):
            if in_degree[i]==0:
                queue.append(i)
        topo=[]
        while queue:
            front=queue.popleft()
            topo.append(front)

            for k in adj[front]:
                in_degree[k]-=1

                if in_degree[k]==0:
                    queue.append(k)
        return len(topo)==len(adj)


