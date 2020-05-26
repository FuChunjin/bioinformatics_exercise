import os
import sys
import re

def Length(arr):
    n = len(arr)
    # 如果有n个数，那么循环n-1次，range(1, n)实际上取到的是1至(n-1)个数
    for i in range(1, n):
        for j in range(0, n-i):
            if  arr[j+1][0] > arr[j][0] :
                arr[j+1],arr[j] = arr[j+1],arr[j]
            else:
                arr[j+1],arr[j] = arr[j],arr[j+1]
    # print(arr)
    length = arr[0][1]-arr[0][0] + 1
    arr_range = len(arr)
    # 最后的元素
    n_end = arr[0][1] 
    # print(n_end)
    for i in range(arr_range-1):
    	# 如果当前的最右坐标在下一组的左右端点之间 如【41，721】，【315，1020】721在315和1020之间
        if (n_end < arr[i+1][1] and arr[i+1][0] < n_end):
        	# 长度总和变成原来的加上新增加的长度  按上面例子就是length+1020-721
            length += arr[i+1][1] - n_end 
            n_end = arr[i+1][1]
        if (arr[i+1][0] >= n_end):
        	# 如果下一组的左端点都比当前的最右坐标靠右  如【41,1020】，【1172,2156】 1172在1020右边
            length += arr[i+1][1] - arr[i+1][0] + 1
            # 长度总和变成原来的加上新增加的长度  按上面例子就是length + 2156 - 1172
            n_end = arr[i+1][1]
        # 其他情况length和n_end都不变类似【41,721】，【124,356】 n_end和length都不会变，直接进下一个循环
        # print(i, n_end, length)
    return length

gene_id_pattern = re.compile(r'gene_id\s+"(.+?)";')
gene_name_pattern = re.compile(r'gene_name\s+"(.+?)";')
Gene=dict()
with open(sys.argv[1], 'r') as f:
    for each in f:
        if each.startswith("#"):
                continue
        else:
            line = each.strip().split()
            typ = line[2]
            if typ != "CDS":
                    continue
            else:
                start = line[3]
                end = line[4]
                each_len = [int(start), int(end)]

                gene_id = gene_id_pattern.search(each)
                gene_id = gene_id.groups()[0]
                
                gene_name = gene_name_pattern.search(each)
                gene_name = gene_name.groups()[0]

                gene_info = gene_id + "\t" + gene_name
                Gene.setdefault(gene_info,[]).append(each_len)
                



# 每个基因CDS长度
CDS = []
for i in Gene.values():
    i = Length(i)
    i = str(i)
    CDS.append(i)
# print(CDS)
# print(len(CDS))

GENE = dict(zip(Gene, CDS))
with open('gene.txt', 'a') as f:
	for i in GENE:
		f.write(f'{i}\t{GENE[i]}\n')



# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算


# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算


# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算




# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算


# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算


# # 统计人类CDS序列的总长度  
# result = 0
# for i in Gene.values():
#      i = Length(i)
#      result += i
# print(result)



# for each in Gene:
#         # print(f'{each}\t{sum(Gene[each])}')
#         # print(f'{each}\t{Gene[each]}')
#         print(each)
#         print(Gene[each])
#         print(Gene.values())


# # 1st bubble sort
# # __author__: Fyilyer
# # 2020.5.24

# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 错误示范,但也可以实现该项功能，只不过复杂度很高，增加了很多无效计算，可以自己推一下
#         for j in range(0, len(arr)-1):
#             if arr[i] > arr[j]:
#                 arr[i], arr[j] = arr[i], arr[j]
#             else:
#                 arr[i], arr[j] = arr[j], arr[i]
#     print(arr)
# bubble_sort(arr)




# # __version__: 2nd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 注意这里的len(arr)-1在循环多次之后，实际上是对末端已排好的序列的多余计算
#         for j in range(0, len(arr)-1):
#             if arr[j+1] > arr[j]:
#                 arr[j+1], arr[j] = arr[j+1], arr[j]
#             else:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     print(arr)
# bubble_sort(arr)



# # __version__: 3rd bubble sort
# # __author__: Fyilyer
# # __date__: 2020.5.24
# 
# # 定义一个数字列表
# arr = [54, 26, 10, 3, 49, 10, 1, 4]
# 
# # 打印的长度为８,实际上把8放在range里面只能取到7，因为range是左闭右开的
# print(len(arr))
# 
# # 冒泡排序，range索引左闭右开,注意这一版和第一版的区别，因为i=j+1，所以把i替换成了j+1
# def bubble_sort(arr):
#     for i in range(1, len(arr)):
#         # 这里的len(arr)-1才是正确的，已排好序的数字干嘛还要再排一遍？所以应该减去i
#         for j in range(0, len(arr)-i):
#             if arr[j+1] > arr[j]:
#                 arr[j+1], arr[j] = arr[j+1], arr[j]
#             else:
#                 arr[j+1], arr[j] = arr[j], arr[j+1]
#     print(arr)
# bubble_sort(arr)




# # arr = [[2, 5],  [11, 13], [4, 9]]
# arr = [[5, 15],  [10, 18], [8, 30]]
# 
# n = len(arr)
# print(arr)
# 
# # 如果有n个数，那么循环n-1次，range(1, n)实际上取到的是1至(n-1)个数
# for i in range(1, n):
#     for j in range(0, n-i):
#         if  arr[j+1][0] > arr[j][0] :
#             arr[j+1],arr[j] = arr[j+1],arr[j]
#         else:
#             arr[j+1],arr[j] = arr[j],arr[j+1]
# print(arr)
# 
# 
# length = arr[0][1]-arr[0][0]
# arr_range = len(arr)
# n_end = arr[0][1]
# print(n_end)
# for i in range(arr_range-1):
#     if (arr[i][1] < arr[i+1][1] and arr[i+1][0] < n_end):
#         n_end = arr[i+1][1]
#         length += n_end - arr[i][1]
#     if (arr[i+1][0] >= n_end):
#         n_end = arr[i+1][1]
#         length += n_end - arr[i+1][0]
#     print(i, n_end, length)
# print(length)


# def Length(arr):
#     n = len(arr)
#     # 如果有n个数，那么循环n-1次，range(1, n)实际上取到的是1至(n-1)个数
#     for i in range(1, n):
#         for j in range(0, n-i):
#             if  arr[j+1][0] > arr[j][0] :
#                 arr[j+1],arr[j] = arr[j+1],arr[j]
#             else:
#                 arr[j+1],arr[j] = arr[j],arr[j+1]
#     # print(arr)
#     length = arr[0][1]-arr[0][0] + 1
#     arr_range = len(arr)
#     n_end = arr[0][1]
#     # print(n_end)
#     for i in range(arr_range-1):
#         if (n_end < arr[i+1][1] and arr[i+1][0] < n_end):
#             length += arr[i+1][1] - n_end
#             n_end = arr[i+1][1]
#         if (arr[i+1][0] >= n_end):
#             length += arr[i+1][1] - arr[i+1][0] + 1
#             n_end = arr[i+1][1]
#         # print(i, n_end, length)
#     return length
# 
# 
# a = [[11869, 12227], [12613, 12721], [13221, 14409], [12010, 12057], [12179, 12227], [12613, 12697], [12975, 13052], [13221, 13374], [13453, 13670]]
# print(Length(a))
















