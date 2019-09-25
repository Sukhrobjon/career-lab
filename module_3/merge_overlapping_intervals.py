from functools import reduce


def merge_overlapping_intervals(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    Return them in a sorted order
    """
    # for interval in intervals:
    # check if the the number at the index of 1 of each interval
    # if so add the interval[0] and next interval[1] to the new array
    intervals = sorted(intervals)
    merged_array = []

    if intervals[0][1] <= intervals[1][1] and intervals[0][1] >= intervals[1][0]:
        merged_array.append([intervals[0][0], intervals[1][1]])
    j = 0
    for i in range(2, len(intervals)):
        if merged_array[j][1] <= intervals[i][1] and merged_array[j][1] >= intervals[i][0]:
            print("inside if")
            print(f"merged: {merged_array[j]}, intervals: {intervals[i]}")
            merged_array.append([merged_array[j][0], intervals[i][1]])
        else:
            merged_array.append(intervals[i])
        j += 1
    return merged_array


# arr = [[1, 3], [2, 6], [8, 10], [15, 18]]
arr = [[2, 6], [1, 3], [15, 18], [16, 20]]

print(merge_overlapping_intervals(arr))
