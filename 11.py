# import os, sys
#
# # 找到当前目录
# project_root = os.path.dirname(os.path.realpath(__file__))
# print(project_root)
#
# # 找到解释器，虚拟环境目录
# python_root = sys.exec_prefix
# print(python_root)
#
# # 拼接生成requirements命令
# command = python_root + '\Scripts\pip freeze > ' + project_root + '\\requirements.txt'
# print(command)
#
# # 执行命令。
# os.system(command)

def creattime(arr,limit0):
    l_hour = []
    hour = 0
    for i in range(len(arr)):
        for j in arr[i+1:]:
            tem1 = arr[i]*10 + j
            tem2 = j*10 +arr[i]
            if tem1<limit0:
                l_hour.append(tem1)
            if tem2 < limit0:
                l_hour.append(tem2)
    hour = max(l_hour)
    if hour>=10:
        arr.pop(arr.index(hour%10))
        arr.pop(arr.index(hour//10))
    else:
        arr.pop(arr.index(hour))
    return hour,arr

if __name__ == '__main__':
    arr_str = list(input())
    arr_str = arr_str[1:-1]
    arr = []
    for i in range(len(arr_str)):
        if i%2==0:
            arr.append(int(arr_str[i]))
    print(arr)
    hour,arr = creattime(arr,24)
    minute,arr = creattime(arr,60)
    second,arr = creattime(arr,60)
    if second == 0:
        second = '00'
    print(str(hour)+':'+str(minute)+':'+str(second))
