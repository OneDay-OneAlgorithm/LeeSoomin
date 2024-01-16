def solution(n, k, cmd):
    answer = ['O' for i in range(n)]
    up = []
    down = []
    delete = []
    now = k
    
    for i in range(0, k):
        up.append(i)
    for i in range(n-1, k, -1):
        down.append(i)
    
    for c in cmd:
        print(up, down)
        if c[0] == 'U':
            count = int(c.split(' ')[1])
            down.append(now)
            for c in range(count):
                if up:
                    down.append(up.pop())
            if up:
                now = up.pop()
            else: 
                now = down.pop(-1)
            continue
        
        if c[0] == 'D':
            count = int(c.split(' ')[1])
            up.append(now)
            for c in range(count):
                if down:
                    up.append(down.pop())
            if down:
                now = down.pop()
            else: 
                now = up.pop(-1)
            continue
            
        if c[0] == 'C':
            answer[now] = 'X'
            delete.append(now)
            if down:
                now = down.pop()
            else:
                now = up.pop()
            continue
        
        if c[0] == 'Z':
            if delete:
                poped = delete.pop()
                answer[poped] = 'O'
                if poped - now > 0:
                    up.insert(poped-now-1, poped)
                    continue
                if poped - now < 0:
                    down.insert(len(down)+(poped-now-1), poped)
        
    return ''.join(answer)