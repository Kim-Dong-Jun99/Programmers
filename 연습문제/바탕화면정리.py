def solution(wallpaper):
    answer = []
    # 12:36
    # 12:42
    """
    .#...
    ..#..
    ...#.
    """
    lux = 100
    luy = 100
    rdx = 0
    rdy = 0
    for i in range(len(wallpaper)):
        for j in range(len(wallpaper[0])):
            if wallpaper[i][j] == "#":
                if i < lux:
                    lux = i
                if j < luy:
                    luy = j
                if i > rdx:
                    rdx = i
                if j > rdy:
                    rdy = j
    print(lux, luy, rdx, rdy)
    answer = [lux, luy, rdx+1, rdy+1]
    return answer
