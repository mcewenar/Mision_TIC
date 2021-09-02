#6. Arrays creator
#
#Given two integers size and u, return the number of all the possible arrays of length size you can create using u different integers with the condition that no more than 2 elements are repeated one after another. The elements you use do not matter, just make sure they are different.
#
#Example 1
#
#Input:
#
#size = 1, u = 3
#
#Output: 3
#
#Explanation:
#
#Here, u = 3 different elements were used: 1, 2, and 3. The arrays of length size = 1 are:
#
#[1]
#[2]
#[3]
#Example 2
#
#Input:
#
#size = 3, u = 3
#
#Output: 24
#
#Explanation:
#
#The possible arrays are:
#
#[1,1,2]    [2,2,1]    [3,3,1]
#[1,1,3]    [2,2,3]    [3,3,2]
#[1,2,2]    [2,1,1]    [3,1,1]
#[1,2,3]    [2,1,3]    [3,1,2]
#[1,3,2]    [2,3,1]    [3,2,1]
#[1,3,3]    [2,3,3]    [3,2,2]
#[1,2,1]    [2,1,2]    [3,1,3]
#[1,3,1]    [2,3,2]    [3,2,3]
#Note that the following arrays are not an option because the elements are repeated sequentially more than two times.
#
#[1,1,1]
#[2,2,2]
#[3,3,3]
#Constraints
#
#1 <= size <= 9
#1 <= u <= 10
#Please enter the output for the following inputs:
#
#size
#
#9
#
#u
#
#9
#
#size
#
#7
#
#u
#
#8
#
#Please copy and paste your code
#
#Back
#Complete
#