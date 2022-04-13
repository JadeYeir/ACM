
def num2serial(num, n, lst):  # num 代表排列的序号，n代表排列数字的个数，lst代表被排列数字从小到大排列的list
    temp_lst = list(range(n))  # 用来保存每个位置的数字是剩下数字中的第几个，数字从小到大排列
    index = (list(range(n)))
    index.sort(reverse=True)

    for x in index:
        temp_lst[x] = num % (n - x)  # 关键步骤
        num = int(num / (n - x))  # 关键步骤 #记得在这里加括号
        print(num)
    string = ''
    for x in range(n):
        string += str(lst[temp_lst[x]])
        lst.remove(lst[temp_lst[x]])
    return int(string)


if __name__ == '__main__':
    n = int(input())
    lst = list(range(1,n+1))
    print(lst)
    for i in range(1,n+1):
        result_num = str(num2serial(i, n, lst))
        print(result_num+".mp4")


