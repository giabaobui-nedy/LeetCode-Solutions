class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list) # quickly build graph = { key: [] } for appending
        in_degree = [0] * numCourses

        for course, prereq in prerequisites:
            graph[prereq].append(course) # dictionary
            in_degree[course] += 1 # calculate the number of pre-reqs? per each course??

        queue = deque([c for c in range(numCourses) if in_degree[c] == 0]) # take the courses that has no pre-reqs?
        visited = 0

        while queue: # while there are still courses that are ready to be studied (done pre-reqs or no pre-req)
            node = queue.popleft() # LIFO
            visited += 1
            for neighbor in graph[node]: # check the finished course see if it is the pre-req for any other courses
                in_degree[neighbor] -= 1 
                if in_degree[neighbor] == 0:
                    queue.append(neighbor) # append to the ready to study queue

        return visited == numCourses