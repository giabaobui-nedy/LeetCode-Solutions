class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # STEP 1: Build the graph and count prerequisites for each course.
        
        # graph[course] will be a list of "courses that need `course` to be done first are unlocked by it"
        # More precisely: graph[X] = list of courses that require X as a prerequisite.
        graph = []
        for i in range(numCourses):
            graph.append([])   # start with an empty list of "unlocked courses" for each course

        # in_degree[course] = how many prerequisites that course still has left
        in_degree = []
        for i in range(numCourses):
            in_degree.append(0)

        # Fill in graph and in_degree using the prerequisites list
        for pair in prerequisites:
            course = pair[0]
            prereq = pair[1]
            # To take `course`, you must first take `prereq`.
            # So finishing `prereq` unlocks `course`.
            graph[prereq].append(course)
            # `course` has one more prerequisite to satisfy.
            in_degree[course] += 1

        # STEP 2: Find all courses that have NO prerequisites at all.
        # These are safe to take right away.
        ready_to_take = []
        for course in range(numCourses):
            if in_degree[course] == 0:
                ready_to_take.append(course)

        # STEP 3: Simulate "taking" courses one at a time.
        finished_count = 0

        while len(ready_to_take) > 0:
            # Take the next course that's ready (no pending prerequisites)
            current_course = ready_to_take.pop(0)  # remove from front of the list
            finished_count += 1

            # Now that current_course is done, see which courses it unlocks
            for unlocked_course in graph[current_course]:
                in_degree[unlocked_course] -= 1  # one less prerequisite pending

                # If that course now has zero prerequisites left, it's ready to take
                if in_degree[unlocked_course] == 0:
                    ready_to_take.append(unlocked_course)

        # STEP 4: If we managed to "finish" every course, there was no cycle.
        return finished_count == numCourses