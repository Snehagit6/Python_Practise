l = [4, 5, 6, 8, 9]
s = 8
ixo, ixn = 0, len(l)-1

while ixn >= ixo:

    mid = (ixo + ixn) // 2

    if l[mid] == s:
        print(f'{s} found at position:{mid}')
        break
    if l[mid] > s:
        ixn = mid-1
    elif l[mid] < s:
        ixo = mid+1






