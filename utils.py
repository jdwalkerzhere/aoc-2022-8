def rotate_map(grid, w, h):
    return [[grid[i][j] for i in range(w)] for j in range(h-1,-1,-1)]

def process_tree_cover(map):
    height = len(map)
    width = len(map[0])

    # Creating Tuple Identifiers for the Map
    for i in range(height):
        for j in range(width):
            map[i][j] = [(i,j), map[i][j]]

    # Our Set of Visible Trees
    visible_trees = set()

    # We will view the map from each side by rotating it
    # and identifying the visible trees from each angle
    rotations = 0
    
    while rotations < 4:
        # This is added in again here to 
        # accomodate for m != n maps
        height = len(map)
        width = len(map[0])

        # At each row we are viewing into each tree
        # column from our current vantage point.
        # As we see a tree of a new higher height
        # we assign that new height as our new highest
        # and save it to our inner-loop set "seen"
        # so we can ignore previously seen heights
        for i in range(width):
            seen, best = set(), -1
            for j in range(height):
                curr = map[i][j][1]
                if curr not in seen and curr > best:
                    best = curr
                    seen.add(curr)
                    visible_trees.add(map[i][j][0])
                # if we encounter a 9 in any given column
                # we know we cannot encounter any higher 
                # trees in said column and can break early
                if curr == 9: break

        # Shifting the viewing vantage point
        map = rotate_map(map, width, height)
        rotations += 1
        
    return len(visible_trees)


# Super inefficient approach where we could be seeking
# really large areas inside of tree maps like this one: 
'''
911111119
191111191
119111911
111919111
111191111
111919111
119111911
191111191
911111119
'''

def look_around(map, coord, width, height):
    x, y = coord
    val = map[x][y]

    # Here we are identifying the coordinates
    # immediately up, down, left, and right
    # of the cell that we are currently exploring.
    # In the case that the current cell is on any
    # of the edges we set this variable at edge
    # to ensure that our scenic view factor is
    # assured to equal zero for whatever side it is.
    left = x - 1 if x > 0 else 0
    right = x + 1 if x < width - 1 else width
    up = y - 1 if y > 0 else 0
    down = y + 1 if y < height - 1 else height
    
    # Setting our Search area for this cell
    row, column = [map[j][y] for j in range(height)], map[x]

    # We increment or decrement the pointers until
    # we either encounter a taller or equal height tree
    # or we encounter and edge
    while left >= 1 and row[left] < val: left -= 1
    while right <= width-2 and row[right] < val: right += 1
    while up >= 1 and column[up] < val: up -= 1
    while down <= height-2 and column[down] < val: down += 1

    # Creating our Scenic View Factors
    left_view = x - left
    right_view = right - x
    up_view = y - up
    down_view = down - y
    
    scenic_view_score = left_view * right_view * up_view * down_view
    return scenic_view_score

def process_view(map):
    height, width = len(map), len(map[0])
    best_view = 0
    for i in range(width):
        for j in range(height):
            # At each coordinate in the tree map, we are looking
            # up, down, left, and right for as far as we can.
            # And compute the scenic view product at that point.
            # If it is higher than the 
            
            current_view = look_around(map,(i,j), width, height)
            if current_view > best_view: best_view = current_view
    return best_view