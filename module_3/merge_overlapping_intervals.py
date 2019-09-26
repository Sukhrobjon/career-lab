from functools import reduce


def merge_overlapping_intervals_v1(intervals):
    """
    NOTE: DOES NOT WORK! BUT KEEP IT FOR FUTURE REFERENCE
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
            # merged_array.pop()
            merged_array.append([merged_array[j][0], intervals[i][1]])
        else:
            merged_array.append(intervals[i])

        j += 1
    return merged_array


def merge_overlapping_intervals_v2(intervals):
    """
    Given a collection of intervals, merge all overlapping intervals.
    Return them in a sorted order
    """

    if len(intervals) == 0:
        return []
    # we need sorted array
    intervals = sorted(intervals)  # O(nlog(n))

    # to hold the merged intervals
    merged_stack = [intervals[0]]
    j = 0  # counter for merged stack
    
    for i in range(1, len(intervals)):
        # check if the interval in the merged stack and intervals are
        # overlapping
        if merged_stack[j][0] < intervals[i][1] and merged_stack[j][1] >= intervals[i][0]:
            curr_item = merged_stack.pop(j)
            # print("last item: ", curr_item)
            merged_stack.append([curr_item[0], intervals[i][1]])
        # otherwise, add the current interval from intervals to merged stack
        else:
            merged_stack.append(intervals[i])
            j += 1
    return merged_stack


arr = [[1, 3], [2, 6], [8, 10], [15, 18]]  # => [[1,6], [8,10], [15,18]]
# arr = []

print(merge_overlapping_intervals_v2(arr))
