# You are given an integer array A of size N.

# You can pick B elements from either left or right end of array A to get the maximum sum.

# Find and return this maximum possible sum.

# NOTE: Suppose B = 4, and array A contains 10 elements, then

# You can pick the first four elements or can pick the last four elements, or can pick 1 from front and 3 from the back, etc. You need to return the maximum possible sum of elements you can pick.

A=[ -533, -666, -500, 169, 724, 478, 358, -38, -536, 705, -855, 281, -173, 961, -509, -5, 942, -173, 436, -609, -396, 902, -847, -708, -618, 421, -284, 718, 895, 447, 726, -229, 538, 869, 912, 667, -701, 35, 894, -297, 811, 322, -667, 673, -336, 141, 711, -747, -132, 547, 644, -338, -243, -963, -141, -277, 741, 529, -222, -684, 35 ]
l=len(A)
k=48
A=A+A[0:k-1]
sums=[0]*l
for i in range(l):
    sums[i]=sum(A[i:i+k])
print(sums)