class Solution:
    def sortTheStudents(self, A, k):
        return sorted(A, key=lambda a: -a[k])
