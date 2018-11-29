def get_stuff():
    students = input("Please enter total and required students ")
    tot_stu, req_stu = [int(x) for x in students.strip().split(" ")]
    stu_time = [int(x) for x in input().strip().split(" ")]

    on_time = sum(x <= 0 for x in stu_time)
    
    if on_time >= req_stu:
        return "NO"
    else:
        return "YES"
    
def main():
    test = input("Please enter number of tests ")
    for x in range(int(test)):
        print(get_stuff())
        
main()