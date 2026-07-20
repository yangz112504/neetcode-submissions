class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        # map each course to an empty list
        prereqMap = { i : [] for i in range(numCourses)}
        for course, prereq in prerequisites:
            prereqMap[course].append(prereq)

        visitSet = set() # all courses along current DFS path

        def dfs(course):
            if course in visitSet:
                return False # cycle so course can definitely not be completed
            if prereqMap[course] == []:
                return True # course can definitely be completed
            visitSet.add(course)
            for prereq in prereqMap[course]:
                if not dfs(prereq):
                    return False
            visitSet.remove(course)
            prereqMap[course] = []
            return True
        # need to call it for all courses we have in case the graph is not connected
        for course in range(numCourses):
            if not dfs(course):
                return False
        return True
           
        