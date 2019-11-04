"""
You work at a sorting factory. You sort things. One day, your boss comes in to
tell you there's a new ball shipment. There are three kinds of balls: red,
white, and blue. You've been charged with the task of sorting these balls.
Unfortunately, your boss won't let you take your lunch break until you've
finished sorting the balls, so you want to do it quickly.

Instructions:
Create an algorithm that will sort an array of n elements, each element either
red, white or blue. The integers 0, 1, 2, will represent red, white, and blue,
respectively. Perform this sorting in-place, using constant space. Your
solution should complete this in O(n) time, any longer and you'll miss your
lunch break!

Example:
[0, 1, 0, 1, 2, 1] --> [0, 0, 1, 1, 2]

Extra Challenge:
The boss is threatening to replace your job with a very efficient sorting
robot, provided you don't perform better than it would. Luckily for you, the
robot requires taking two passes over the array to sort the elements. You're not sure, but you think there might be a way to sort the elements that requires taking only one pass over the array, thus handily out-performing the robot.

Original Platform:  https://leetcode.com/problems/sort-colors/ 
"""

def color_sort(nums):
    """
    red - 0
    white - 1
    blue - 2
    """

    