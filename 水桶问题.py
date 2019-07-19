class State:
    def __init__(self, x, y, father, depth):
        self.x = x
        self.y = y
        self.father = father
        self.depth = depth
        self.f = self.depth + self.h()

    # 计算状态的h值：
    def h(self):
        if 0 < self.x < 4 and 0 < self.y < 3:
            return 2
        if 0 < self.x < 4 or 0 < self.y < 3:
            return 4
        if self.x == 0 and self.y == 3:
            return 6
        if self.x == 4 and self.y == 0:
            return 8
        if (self.x == 4 and self.y == 3) or (self.x == 0 and self.y == 0):
            return 10
        return 100


    # 获取子状态
    def get_children(self):
        children = []
        x, y, depth = self.x, self.y, self.depth
        depth += 1
        # pour in
        if x < 4:
            children.append(State(4, y, self, depth))
        if y < 3:
            children.append(State(x, 3, self, depth))
        # pour out
        if x > 0:
            children.append(State(0, y, self, depth))
        if y > 0:
            children.append(State(x, 0, self, depth))
        # transfer x -> y
        if x > 0 and y < 3:
            n = min(x, 3 - y)
            children.append(State(x-n, y+n, self, depth))
        # transfer y -> x
        if y > 0 and x < 4:
            n = min(y, 4 - x)
            children.append(State(x+n, y-n, self, depth))

        return children
        
    def show_info(self):
        print(self.x, self.y)

# 冒泡排序，根据f从大到小排序
def sort_by_f(list):  
    for i in range(len(list)-1):
        for j in range(i+1, len(list)):
            if list[i].f < list[j].f:
                list[i], list[j] = list[j], list[i]
    return list

# 判断结点是否存在于open_list
def in_open_list(node):
    for item in open_list:
        if item.x == node.x and item.y == node.y:
            return True
    return False

# 判断结点是否存在于close_list
def in_close_list(node):
    for item in close_list:
        if item.x == node.x and item.y == node.y:
            return True
    return False

if __name__ == "__main__":

    # 起始状态
    START = State(0, 0, None, 0)

    open_list = []
    close_list = []

    open_list.append(START)
   
    while len(open_list) > 0:
        # 对open_list依据f，从大到小排序，最后一个结点就是best_node
        open_list = sort_by_f(open_list)

        # 将best_node从open_list移动close_list
        best_node = open_list.pop()
        close_list.append(best_node)

        # 如果best_node是终止结点，说明已找到最有路径，程序结束
        if best_node.x == 2 or best_node.y == 2:
            print('Success.')
            DEST = best_node
            break
        else:
            # 寻找best_node所有的子结点
            children = best_node.get_children()
            # 遍历子结点
            for child in children:
                # 如果子结点已存在于close_list中，跳过
                if in_close_list(child):
                    continue
                # 如果子结点已存在于open_list中，跳过
                if in_open_list(child):
                    continue
                # 将子结点添加到open_list中              
                open_list.append(child)

    # 生成路径
    path = []
    node =  DEST
    while node.father != None:
        path.append(node)
        node = node.father
    path.append(START)

    # 打印过程
    for state in reversed(path):
        state.show_info()