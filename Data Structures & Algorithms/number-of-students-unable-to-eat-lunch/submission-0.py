class Solution:
    def countStudents(self, students: List[int], sandwiches: List[int]) -> int:
        # maybe it's not the amount of sandiwches that matter, butthe amount of students that are left

        zeroStudents = students.count(0)
        oneStudents = students.count(1)

        for s in sandwiches:
            if s == 0:
                if zeroStudents > 0:
                    zeroStudents-=1
                else: #no more students left to eat, return
                    return oneStudents
            elif s == 1:
                if oneStudents > 0:
                    oneStudents -=1
                else:
                    return zeroStudents
        return 0
        