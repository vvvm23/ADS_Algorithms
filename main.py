# Import sys for command line arguments
import sys
# Import sorts
from ads_sort import bubble_sort, bucket_sort, insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort, HeapSort

def main():
    nb_arguments = len(sys.argv) # Gets number of arguments from command line
    
    if sys.argv[1] == "-h" or sys.argv[1] == "--help": # Display help
        print("\nUsage: python main.py sort_type input_list\n")
        print("sort_type:")
        print("1: Bubble Sort")            
        print("2: Bucket Sort")    
        print("3: Insertion Sort")
        print("4: Merge Sort")
        print("5: Quick Sort")
        print("6: Radix Sort")
        print("7: Selection Sort")
        print("8: Heap Sort\n")     
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
        sort_type = int(sys.argv[1])
        input_list = []
        for a in range(2, nb_arguments):
            input_list = input_list + list(map(int, sys.argv[a].split(',')))

        result = []
        # Get sort type
        # TODO: allow string input
        if sort_type == 1:
            result = bubble_sort.sort(input_list)
        elif sort_type == 2:
            result = bucket_sort.sort(input_list)
        elif sort_type == 3:
            result = insertion_sort.sort(input_list)
        elif sort_type == 4:
            result = merge_sort.sort(input_list)
        elif sort_type == 5:
            result = quick_sort.sort(input_list)
        elif sort_type == 6:
            result = radix_sort.sort(input_list)
        elif sort_type == 7:
            result = selection_sort.sort(input_list)
        elif sort_type == 8:
            result = HeapSort.sort(input_list)
        else:
            print("Error: Unknown sort type!")
            print("Type python main.py --help")
            return 0

        # Display result
        print(result)
    return 0

if __name__ == "__main__":
    main()