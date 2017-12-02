def listgame( A):
    n = len(A)
    scores = [ [ 0 for x in range(n)] for y in range(n)]
    h = 0
    for gap in range(n):
        i = 0
        j = gap
        for j in range(j,n):
            x = scores[i + 2][j] if ( (i + 2) <= j) else 0
            y = scores[i + 1][j - 1] if ((i +1) <= (j-1)) else 0
            z = scores[i][j - 2] if (i <= (j - 2)) else 0
            scores[i][j] = max( A[i] + min(x,y), A[j] + min(y,z))
            i += 1
    return scores
 
def listgameb( A):
    n = len(A)
    scores = [ [ 0 for x in range(n)] for y in range(2)]
    h = 0
    for gap in range(n):
        i = 0
        j = gap
        for j in range(j,n):
            if(i%2 == 0):
                x = scores[0][j] if ( (i + 2) <= j) else 0
                y = scores[0][j-1] if ((i +1) <= (j-1)) else 0
                z = scores[0][j-2] if (i <= (j - 2)) else 0
                scores[0][j] = max( A[i] + min(x,y), A[j] + min(y,z))
            else:
                x = scores[1][j] if ( (i + 2) <= j) else 0
                y = scores[1][j-1] if ((i +1) <= (j-1)) else 0
                z = scores[1][j-2] if (i <= (j - 2)) else 0
                scores[1][j] = max( A[i] + min(x,y), A[j] + min(y,z))                
            i += 1
    return scores

def listgamec( A):
    n = len(A)
    scores = [ [ 0 for x in range(n)] for y in range(3)]
    h = 0
    for gap in range(n):
        i = 0
        j = gap
        for j in range(j,n):
            if(i%3 == 0):
                x = scores[2][j] if ( (i + 2) <= j) else 0
                y = scores[1][j-1] if ((i +1) <= (j-1)) else 0
                z = scores[0][j-2] if (i <= (j - 2)) else 0
                scores[0][j] = max( A[i] + min(x,y), A[j] + min(y,z))
            elif(i%3 == 1):
                x = scores[0][j] if ( (i + 2) <= j) else 0
                y = scores[2][j-1] if ((i +1) <= (j-1)) else 0
                z = scores[1][j-2] if (i <= (j - 2)) else 0
                scores[1][j] = max( A[i] + min(x,y), A[j] + min(y,z))
            else:
                x = scores[1][j] if ( (i + 2) <= j) else 0
                y = scores[0][j-1] if ((i +1) <= (j-1)) else 0
                z = scores[2][j-2] if (i <= (j - 2)) else 0
                scores[2][j] = max( A[i] + min(x,y), A[j] + min(y,z))
            i += 1
    return scores[0][n-1]
    #return scores
    
    def randTest():
    try:
        import random
    except:
        random()
    x = 2**random.randint(1,4)
    a = []
    for i in range(x):
        a.append(random.randint(1,100))
    print(a)
    b = listgamec(a)
    c = rlist_game(a)
    if(b == c):
        return b
    else:
        return (b,c)

def main():
    #arr = [8,15,3,7]
    arr = [20, 30, 2, 2, 2, 10]
    result = listgameb(arr)
    result1 = listgame(arr)
    print(result,"##", result1)
    n = len(result[0])
    m = len(result1)
    for i in range(2):
        for j in range(n):
            print( result[i][j], " ", end="")
        print("")
    print("##########")

    for i in range(m):
        for j in range(m):
            print( result1[i][j], " ", end="")
        print("")

main()
