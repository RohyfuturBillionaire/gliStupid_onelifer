import numpy as np
def convert_numpy(obj):    
    if isinstance(obj, dict):        
        return {k: convert_numpy(v) for k, v in obj.items()}    
    elif isinstance(obj, list):        
        return [convert_numpy(v) for v in obj]    
    elif isinstance(obj, np.generic):        
        return obj.item()  
# Convertit float32, int32 etc. en float, int natifs    
    else:return obj