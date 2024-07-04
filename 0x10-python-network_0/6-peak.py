#!/usr/bin/python3


def find_peak(list_of_integers):
    """Return a peak in a list of unsorted integers."""
    
    def find_peak_util(arr, low, high):
        mid = low + (high - low) // 2

        # Check if the middle element is a peak
        if (mid == 0 or arr[mid - 1] <= arr[mid]) and \
           (mid == len(arr) - 1 or arr[mid + 1] <= arr[mid]):
            return arr[mid]
        # If the left neighbor is greater, search the left half
        elif mid > 0 and arr[mid - 1] > arr[mid]:
            return find_peak_util(arr, low, mid - 1)
        # Otherwise, search the right half
        else:
            return find_peak_util(arr, mid + 1, high)
    
    if not list_of_integers:
        return None

    return find_peak_util(list_of_integers, 0, len(list_of_integers) - 1)
