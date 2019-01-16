# Import sys for command line arguments
import sys
# Import sorts
import bubble_sort, bucket_sort, insertion_sort, merge_sort, quick_sort, radix_sort, selection_sort

def main():
    nb_arguments = len(sys.argv)
    
    if sys.argv[1] == "-h" or sys.argv[1] == "--help":
        print("\nUsage: python main.py sort_type input_list\n")
        print("sort_type:")
        print("1: Bubble Sort")            
        print("2: Bucket Sort")    
        print("3: Insertion Sort")
        print("4: Merge Sort")
        print("5: Quick Sort")
        print("6: Radix Sort")
        print("7: Selection Sort\n")     
        print("input_list:")
        print("Input list is list of comma seperated integers")
    elif nb_arguments == 1:
        print("Error: No arguments provided!")
        print("Type python main.py --help")
    elif nb_arguments == 2:
        print("Error: Too few arguments!")
        print("Type python main.py --help")
    elif nb_arguments > 3:
        print("Error: Too many arguments!")
        print("Type python main.py --help")
    else:   
        sort_type = int(sys.argv[1])
        input_list = list(map(int, sys.argv[2].split(','))) # Does not work for negative numbers yet

        if sort_type == 1:
            bubble_sort.sort(input_list)
            pass
        elif sort_type == 2:
            bucket_sort.sort(input_list)
            pass
        elif sort_type == 3:
            insertion_sort.sort(input_list)
            pass
        elif sort_type == 4:
            merge_sort.sort(input_list)
            pass
        elif sort_type == 5:
            quick_sort.sort(input_list)
            pass
        elif sort_type == 6:
            radix_sort.sort(input_list)
            pass
        elif sort_type == 7:
            selection_sort.sort(input_list)
            pass
        else:
            print("Error: Unknown sort type!")
            print("Type python main.py --help")

    pass

if __name__ == "__main__":
    main()