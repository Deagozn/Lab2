def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5, 67, 32)")

def get_user_input():
    return list(map(float, input().split(",")))

def calc_average(array):
    average = sum(array)/len(array)
    return average
def find_min_max(array):
    return [min(array), max(array)]
def sort_temperature():
    return
def calc_median_temperature():
    return
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    print(find_min_max(num_list))

if __name__ == "__main__":
    main()