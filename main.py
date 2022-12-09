from utils import process_tree_cover, process_view

if __name__ == '__main__':
    with open('map.txt','r') as map:
        map=[[int(c) for c in li.strip('\n')] for li in map.readlines()]

    map_copy = [row.copy() for row in map.copy()]
    
    tree_cover = process_tree_cover(map)
    views = process_view(map_copy)
    print(tree_cover)
    print(views)
    



    