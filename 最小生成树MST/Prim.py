import numpy as np
# 最小生成树之Prim算法，完整代码已上传到GitHub，请搜索 guojingeran

# Step 1. 数据初始化
matrix = np.array([[ 0,  7, -1,  5, -1, -1, -1],  
                   [ 7,  0,  8,  9,  7, -1, -1],  
                   [-1,  8,  0, -1,  5, -1, -1],  
                   [ 5,  9, -1,  0, 15,  6, -1],  
                   [-1,  7,  5, 15,  0,  8,  9],  
                   [-1, -1, -1,  6,  8,  0, 11],  
                   [-1, -1, -1, -1,  9, 11,  0]   
                  ])
mst_nodes = [0]
left_nodes = [i for i in range(1,7)]
path = []

# Step 2. 检查left_nodes是否为空
while len(left_nodes) > 0:
    minimum = 99
    start = 0
    end = 0
    
    # Step 3. 双重for循环寻找最小边
    for i in range(0, len(mst_nodes)):        
        for j in range(0, len(left_nodes)):
            index_1 = mst_nodes[i]
            index_2 = left_nodes[j]
            cost = matrix[index_1][index_2]
            if 0 < cost < minimum:
                minimum = cost
                start = mst_nodes[i]
                end = left_nodes[j]
                
    # Step 4. 更新节点集合与边集合    
    left_nodes.remove(end)
    mst_nodes.append(end)
    path.append([start, end, minimum])    

# Step 5. 跳转到Step 2.
# Step 6. 打印结果
print(mst_nodes)
print(path)
