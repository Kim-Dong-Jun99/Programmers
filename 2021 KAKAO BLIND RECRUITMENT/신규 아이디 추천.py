def solution(new_id):
    valid = ['.','_','-','1','2','3','4','5','6','7','8','9','0']
    uppercase = []
    for i in range(26):
        uppercase.append(chr(i+65))
        valid.append(chr(i+97))
    if 3 <= len(new_id) and len(new_id) <= 15:
        if new_id[0] == '.' or new_id[len(new_id)-1] == '.':
            new_id = reform(new_id,valid,uppercase)
        else:
            check = True
            for i in range(len(new_id)):
                if (new_id[i] in valid) == False:
                    check = False
                    break
                else:
                    if new_id[i] == '.' and i != len(new_id)-1:
                        if new_id[i+1] == '.':
                            check = False
            if check == False:
                new_id = reform(new_id,valid,uppercase)
    else:
        new_id = reform(new_id,valid,uppercase)


    return new_id

def reform(id,valid,uppercase):
    step = 1
    while step < 8:
        if step == 1:
            i = 0
            while i < len(id):
                if (id[i] in uppercase):
                    id = id[:i]+chr(ord(id[i])+32)+id[i+1:]
                i += 1
        elif step == 2:
            i = 0
            while i < len(id):
                if (id[i] in valid ) == False:
                    id = id[:i] + id[i+1:]
                    i -= 1
                i += 1
        elif step == 3:
            i = 0
            while i < len(id):
                if id[i] == '.':
                    j = i
                    while j < len(id):
                        if id[j] == '.':
                            j += 1
                        else:
                            break
                    id = id[:i+1]+id[j:]
                i += 1
        elif step == 4:
            if len(id) > 0:
                if id[0] == '.':
                    id = id[1:]
                if len(id) > 0:
                    if id[len(id)-1] == '.':
                        id = id[:len(id)-1]
        elif step == 5:
            if id == '':
                id += 'a'
        elif step == 6:
            if len(id) >= 16:
                id = id[:15]
                if id[len(id)-1] == '.':
                    id = id[:len(id)-1]
        elif step == 7:
            if len(id) <= 2:
                temp = id[len(id)-1]
                while len(id) != 3:
                    id += temp
        step += 1
    return id