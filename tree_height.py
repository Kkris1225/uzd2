import sys
import threading


def compute_height(n, parents):
    tree = {}
    for i in range(n):
        if i not in tree:
            tree[i] = []
        if parents[i] == -1:
            root = i
        else:
            if parents[i] not in tree:
                tree[parents[i]] = []
            tree[parents[i]].append(i)

    def height(node):
        if not tree[node]:
            return 0
        else:
            return 1 + max(height(child) for child in tree[node])
    return height(root) + 1


def main():
    n = int(input())
    parents = list(map(int, input().split()))
    print(compute_height(n, parents))


if __name__ == '__main__':
    sys.setrecursionlimit(10**7) 
    threading.stack_size(2**27)  
    threading.Thread(target=main).start()
