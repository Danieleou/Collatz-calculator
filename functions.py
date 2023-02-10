def next_collatz(n):
    if n%2==0:
        return n//2
    else:
        return 3*n+1

def path_collatz(n):
    path='{}'.format(n)
    while n!=1:
        n=next_collatz(n)
        path+=' '+str(n)
    return path

def array_collatz(n):
    array=path_collatz(n).split()
    return array

def max_collatz(n):
    array=array_collatz(n)
    for i in range(len(array)):
        array[i]=int(array[i])
    maximum=max(array)
    return maximum
    
def length_path_collazt(n):
    size=len(array_collatz(n))
    return size