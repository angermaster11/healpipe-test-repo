import numpy as np

def add(a, b):
    # Use numpy.char.add for string concatenation, fallback for numeric addition
    if isinstance(a, str) or isinstance(b, str):
        return np.char.add(str(a), str(b))
    try:
        return np.add(a, b)
    except TypeError:
        # fallback to python addition if numpy fails
        return a + b

def divide(a, b):
    return np.divide(a, b)

def sum(a,b){
    return a+b;
}

for (int i=0; i<10; i++){
    print(i);
}

lolu