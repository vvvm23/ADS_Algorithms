# ADS Algorithms
## Description
Repository of all sorting algorithms taught by Durham University Computer Science Level 1 in python.

---
## Usage

Call in terminal in the format:

    python main.py [--help] sort_type input_list

The sorting types are as follows:

    1: Bubble Sort
    2: Bucket Sort
    3: Insertion Sort
    4: Merge Sort
    5: Quick Sort
    6: Radix Sort
    7: Selection Sort
    8: Heap Sort
    9: Bogo Sort

And input list is of either of the two formats:

    1,2,3,4,5,6,7 (Comma seperated)
    1 2 3 4 5 6 7 (Space seperated)

Alternatively, you can call the sorting functions directly by importing them. The import statements and their corresponding functions are shown here:

    import bubble_sort; bubble_sort.sort(L)
    import bucket_sort; bucket_sort.sort(L)
    import insertion_sort; insertion_sort.sort(L)
    import merge_sort; merge_sort.sort(L)
    import quick_sort; quick_sort.sort(L)
    import radix_sort; radix_sort.sort(L)
    import selection_sort; selection_sort.sort(L)

    Where L is a Python list

    Or:

    from ads_sort import bubble_sort, bucket_sort, insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort

The program should also work on Linux however this is untested. Call using python3 instead of python.

---
## ToDo

* Implement error checking eg. when empty lists are passed or non-lists
* Add ability for other developers to make pull requests and easily add their sorts by simply placing a .py file
* Add timing mechanisms to compare times of different sorts
* Add educational mode which will step through sorting process with statistics
* Bogosort
