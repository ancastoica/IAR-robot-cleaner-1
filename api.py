def printmap(mapp):
    for i in range(len(mapp)):
        line = ""
        for j in range(len(mapp[i])):
            if mapp[i][j].home == 1:
                line += "h"
            elif mapp[i][j].dirty == 1:
                line += "x"
            elif mapp[i][j].dirty == 0:
                line += "o"
        print(line)
