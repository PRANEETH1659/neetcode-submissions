class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        
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

        if len(topo)==len(adj):
            return topo
        else:
            return []


