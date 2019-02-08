# Import sys for command line arguments
import sys
# Import sorts
from ads_sort import bubble_sort, bucket_sort, insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort, heap_sort

keys = {
    "bubble sort": 1,
    "bucket sort": 2,
    "insertion sort": 3,
    "merge sort": 4,
    "quick sort": 5,
    "radix sort": 6,
    "selection sort": 7,
    "heap sort": 8
}

def main():
    nb_arguments = len(sys.argv) # Gets number of arguments from command line
    
    if sys.argv[1] == "-h" or sys.argv[1] == "--help": # Display help
        print("\nUsage: python main.py sort_type input_list\n")
        print("sort_type:")

        for key, val in keys.items():
            print(str(val) + ":", key.capitalize())

        print("input_list:")
        print("Input list is list of comma or space seperated integers")
        print("Eg: 1,2,3,4,5 or 1 2 3 4 5")
        return 0
    elif nb_arguments == 1: # Check number of arguments 
        print("Error: No arguments provided!")
        print("Type python main.py --help")
        return 0
    elif nb_arguments == 2:
        print("Error: Too few arguments!")
        print("Type python main.py --help")
        return 0
    else:
        if type(sys.argv[1]) is str:
            try:
                sort_type = keys[sys.argv[1].lower()]
            except:
                print("Invalid sort")
                sys.exit()
        else:          
            sort_type = int(sys.argv[1])
        input_list = []
        for a in range(2, nb_arguments):
            input_list = input_list + list(map(int, sys.argv[a].split(',')))

        result = []
        # Get sort type
        # TODO: allow string input
        if sort_type == keys["bubble sort"]:
            result = bubble_sort.sort(input_list)
        elif sort_type == keys["bucket sort"]:
            result = bucket_sort.sort(input_list)
        elif sort_type == keys["insertion sort"]:
            result = insertion_sort.sort(input_list)
        elif sort_type == keys["merge sort"]:
            result = merge_sort.sort(input_list)
        elif sort_type == keys["quick sort"]:
            result = quick_sort.sort(input_list)
        elif sort_type == keys["radix sort"]:
            result = radix_sort.sort(input_list)
        elif sort_type == keys["selection sort"]:
            result = selection_sort.sort(input_list)
        elif sort_type == keys["heap sort"]:
            result = heap_sort.sort(input_list)
        else:
            print("Error: Unknown sort type!")
            print("Type python main.py --help")
            return 0

        # Display result
        print(result)
    return 0

if __name__ == "__main__":
    main()