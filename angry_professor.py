def get_stuff():
    tot_stu, req_stu = [int(x) for x in input().strip().split(" ")]
    stu_time = [int(x) for x in input().strip().split(" ")]

    on_time = sum(x <= 0 for x in stu_time)
    
    if on_time >= req_stu:
        return "NO"
    else:
        return "YES"
    
def main():
    test_num = int(input())
    for x in range(test_num):
        print(get_stuff())
        
main()