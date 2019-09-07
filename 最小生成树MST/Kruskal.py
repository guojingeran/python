import itertools
import numpy as np
# 最小生成树之Kruskal算法，完整代码已上传到GitHub，请搜索 guojingeran

# Step 1.数据初始化

# 生成0-6数字的两两组合
couples = [i for i in itertools.combinations(range(7), 2)]

# 保存各点的根节点信息，初始值全为-1
root = [-1 for i in range(7)]

# 点之间边长的矩阵
matrix = np.array([[ 0,  7, -1,  5, -1, -1, -1],  
                   [ 7,  0,  8,  9,  7, -1, -1],  
                   [-1,  8,  0, -1,  5, -1, -1],  
                   [ 5,  9, -1,  0, 15,  6, -1],  
                   [-1,  7,  5, 15,  0,  8,  9],  
                   [-1, -1, -1,  6,  8,  0, 11],  
                   [-1, -1, -1, -1,  9, 11,  0]   
                  ])

# 生成包含所有边的数组，每个边由三元组组成，即端点和边长
edges = [[i, j, matrix[i][j]] for i, j in couples]

# 过滤掉长度为-1的边
edges = list(filter(lambda x: x[2] >= 0, edges))

# 按照边长从小到大排序
edges = sorted(edges, key = lambda edge:edge[2])

print('所有边：',edges)

mst = []
# Step 2.依次添加边
while len(mst) < 6:
    # 取出长度最短的边
    v_1, v_2, w = edges.pop(0)    
    
    # 如果两个端点都是第一次添加
    if root[v_1] == -1 and root[v_2] == -1:
        mst.append([v_1, v_2, w])    
        root[v_1] = v_1
        root[v_2] = v_1    
        continue
    
    # 如果两个端点的根节点不同
    if root[v_1] != root[v_2]:
        
        # 如果连接的是子树与点，更新点的根节点
        if root[v_2] == -1:
            mst.append([v_1, v_2, w])
            root[v_2] = root[v_1]
        
        # 如果连接的是两个子树，更新子树中所有点的根节点
        else: 
            mst.append([v_1, v_2, w])
            for i in range(len(root)):
                if root[i] == root[v_2]:
                    root[i] = root[v_1]
            
print(mst)
