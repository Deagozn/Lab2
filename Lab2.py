def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    return list(map(float, input().split(",")))

def calc_average(array):
    average = sum(array)/len(array)
    return average
def find_min_max(array):
    return [min(array), max(array)]
def sort_temperature(array):
    return sorted(array)
def calc_median_temperature(array):
    sorted_array = sort_temperature(array)
    if len(sorted_array)%2 == 0:
        med_pos1 = len(sorted_array)/2
        med_pos2 = med_pos1 - 1
        median_value = (sorted_array[int(med_pos1)] + sorted_array[int(med_pos2)])/2
    else:
        median_value = sorted_array[len(sorted_array)//2]
    return median_value
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(calc_median_temperature(num_list))

if __name__ == "__main__":
    main()