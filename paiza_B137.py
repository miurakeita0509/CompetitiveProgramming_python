#https://paiza.jp/challenges/673/ready

def find_and_remove_blocks(grid, n, m):
    to_remove = set()
    for i in range(n):
        for j in range(m):
            if i > 0 and grid[i][j] == grid[i-1][j]:
                to_remove.add((i, j))
                to_remove.add((i-1, j))
            if j > 0 and grid[i][j] == grid[i][j-1]:
                to_remove.add((i, j))
                to_remove.add((i, j-1))

    # print(f"Blocks to remove: {to_remove}")  # Add print here
    
    for i, j in to_remove:
        grid[i][j] = "#"
    
    return grid

def drop_blocks(grid, n, m):
    for j in range(m):
        stack = []
        for i in range(n-1, -1, -1):
            if grid[i][j] != "#":
                stack.append(grid[i][j])
                grid[i][j] = "#"
        
        # print(f"Stack for column {j}: {stack}")  # Add print here

        for i, block in enumerate(stack):
            grid[n-1-i][j] = block
    
    return grid

def solve_puzzle(grid, n, m):
    # print("Current grid:")
    # print_grid(grid)  # Print current grid status

    new_grid = find_and_remove_blocks([row.copy() for row in grid], n, m)
    grid = drop_blocks(new_grid, n, m)
    
    return grid

def print_grid(grid):
    for row in grid:
        print(" ".join(row))


def main():
    n, m, x = map(int, input().split())
    grid = [input().split() for _ in range(n)]

    final_grid = solve_puzzle(grid, n, m)
    print_grid(final_grid)


if __name__ == "__main__":
    main()
