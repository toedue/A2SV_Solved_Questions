t = int(input())

for _ in range(t):
    n = int(input())
    a = list(map(int, input().split()))
    
    ans = 0
    largest = a[-1]  # largest element 
    
    for k in range(2, n):
        
        i = 0
        j = k - 1
        
        while i < j:
            
            total = a[i] + a[j] + a[k]
            
            if a[i] + a[j] > a[k] and total > largest:
                ans += (j - i)
                j -= 1
            
            else:
                i += 1
    
    print(ans)
