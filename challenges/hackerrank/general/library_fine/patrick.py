from datetime import date    

def main():
    ret = date(*(int(x) for x in input().strip().split(' ')[::-1]))
    due = date(*(int(y) for y in input().strip().split(' ')[::-1]))
    print(calc_fine(ret, due))
    
def calc_fine(ret, due):
    if ret <= due:
        return 0
    elif ret.year > due.year:
        return 10000
    elif ret.month > due.month:
        return (ret.month - due.month) * 500
    elif ret.day > due.day:
        return (ret.day - due.day) * 15
    
main()
