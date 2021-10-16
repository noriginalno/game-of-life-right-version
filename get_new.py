def get_next_generation(fld):

    ng = [i[::] for i in fld]

    for i in range(len(ng)):
        for j in range(1, len(ng[0]) - 1):
            crit = 0
            for x in range(-1, 2):
                for y in range(-1, 2):
                    try: crit += ng[i+x][j+y]
                    except: pass
            if ng[i][j] == 1 and 2 <= crit - 1 <= 3:
                fld[i][j] = 1
            elif ng[i][j] == 0 and crit == 3:
                fld[i][j] = 1
            else:
                fld[i][j] = 0
    return fld
