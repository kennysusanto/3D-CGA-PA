def clipMY(x, y, minx, miny, maxx, maxy):
    
    m = None
    c = None
    
    
    if(x[0]!=x[1]):
        
        
        if(y[0]!=y[1]):
         
             
            m=(y[0]-y[1])/(x[0]-x[1])
            
            c=(x[0]*y[1]-x[1]*y[0])/(x[0]-x[1])
        
            for i in range(2): 
                
                if(x[i]<minx) :
                
                    x[i]=minx
                    y[i]=m*minx+c
                
                elif(x[i]>maxx):
                
                    x[i]=maxx
                    y[i]=m*maxx+c
                
                if(y[i]<miny):
                
                    x[i]=(miny-c)/m
                    y[i]=miny
                
                elif(y[i]>maxy):
                
                    x[i]=(maxy-c)/m
                    y[i]=maxy
                
            
            
            if((x[0]-x[1]<1) and (x[1]-x[0]<1)):
                print('do nothing')
            
            else:
                print(x[0], y[0], x[1], y[1])
            
        
        
        else: 
        
            
            if((y[0]<=miny) or (y[0]>=maxy)):
            
                print('do nothing')
            else:
                
                for i in range(2):
                
                    if(x[i]<minx):
                    
                        x[i]=minx
                    
                    elif(x[i]>maxx):
                    
                        x[i]=maxx
                    
                
                
                if((x[0]-x[1]<1) and (x[1]-x[0]<1)):
                    print('do nothing')
                
                else: 
                    print(x[0], y[0], x[1], y[1])
            
        
    
    
    
    else :
        
        
        if(y[0]==y[1]):
        
            
            if((y[0]<=miny) or (y[0]>=maxy)):
                print('do nothing')
            
            elif((x[0]<=minx) or (x[0]>=maxx)):
                print('do nothing')
            
            else:
                print(x[0], y[0], x[1], y[1])
        
        
        elif((x[0]<=minx) or (x[0]>=maxx)):
            print('do nothing')

        else:
        
            for i in range(2):
             
                if(y[i]<miny):
                
                    y[i]=miny
                
                elif(y[i]>maxy):
                
                    y[i]=maxy
                
            if((y[0]-y[1]<1) and (y[1]-y[0]<1)):
                print('do nothing')

            else:
                print(x[0], y[0], x[1], y[1])
        

def clipMY3D(X, Y, Z, minx, miny, minz, maxx, maxy, maxz):
    a = None
    b = None

    x = list(X)
    y = list(Y)
    z = list(Z)

    if((x[0] != x[1]) and (y[0] != y[1]) and (z[0] != z[1])):
        
        a = (x[1] - x[0]) / (y[1] - y[0]) 
        b = (y[1] - y[0]) / (z[1] - z[0]) 
        
        for i in range(2):
            
            if(x[i] < minx):
                y[i] = (minx - x[0])/a + y[0]
                z[i] = (minx - x[0])/(a*b) + z[0]
                x[i] = minx
            
            elif(x[i] > maxx):
            
                y[i] = (maxx - x[0])/a + y[0]
                z[i] = (maxx - x[0])/(a*b) + z[0]
                x[i] = maxx
            
            if(y[i] < miny):
            
                x[i] = a*(miny - y[0]) + x[0]
                z[i] = (miny - y[0])/b + z[0]
                y[i] = miny
            
            elif(y[i] > maxy):
            
                x[i] = a*(maxy - y[0]) + x[0]
                z[i] = (maxy - y[0])/b + z[0]
                y[i] = maxy
            
            if(z[i] < minz):
            
                x[i] = a*b*(minz - z[0]) + x[0] 
                y[i] = b*(minz - z[0]) + y[0]
                z[i] = minz
            
            elif(z[i] > maxz):
            
                x[i] = a*b*(maxz - z[0]) + x[0]
                y[i] = b*(maxz - z[0]) + y[0]
                z[i] = maxz
            
            
        
        if((x[0]  - x[1] < 1) and (x[1]  - x[0] < 1)):
            print('do nothing')
        else:
            print(x[0], y[0], z[0], x[1], y[1], z[1])
        
        
        
    elif(z[0] == z[1]):
        clipMY(x, y, minx, miny, maxx, maxy)
    
    elif(x[0] != x[1]):
    
        clipMY(x, z, minz, minx, maxz, maxx); 
    
    elif(y[0] != y[1]):
    
        clipMY(y, z, miny, minz, maxy, maxz); 
    
    else:
    
        if((x[0]  <=  minx)  or  (x[0]  >=  maxx) or  (y[0]  <=  miny)  or (y[0] >= maxy)):
            print('do nothing')
            
        else: 
            for i in range(2): 
                 
                if(z[i] < minz): 
                    z[i] = minz
             
                elif(z[i] > maxz):
                    z[i] = maxz

                if((z[0] - z[1] < 1) and (z[1] - z[0] < 1)): 
                    print('do nothing')
                
                else :
                    print(x[0], y[0], z[0], x[1], y[1], z[1])
        
    
clipMY3D((-3, 3), (-3, 1), (3, 1), -2, -2, 2, 2, 2, -2)