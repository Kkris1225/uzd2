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
    input_type = input()
    
    if input_type == "I":
        n = int(input("Enter number of nodes: "))
        parents = list(map(int, input().split()))
        
    elif input_type == "F":
        while True:
            filename = input()
            if "a" in filename:
                print("Invalid file name. File name cannot contain the letter 'a'.")
            else:
                with open(f"test/{filename}", "r", encoding="utf-8") as f:
                    n = int(f.readline())
                    parents = list(map(int, f.readline().split()))
    
    else:
        print("Invalid input type.")
        return
    
    print(compute_height(n, parents))


if __name__ == '__main__':
    sys.setrecursionlimit(10**7) 
    threading.stack_size(2**27)  
    threading.Thread(target=main).start()
