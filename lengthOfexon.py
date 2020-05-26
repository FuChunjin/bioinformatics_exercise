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

