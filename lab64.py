import matplotlib.pyplot as plt
import numpy as np


T=int(input(' 1) лог спираль 2) архимедова спираль 3) жезл 4) роза :  ') )


def risuem():
    if T == 1:
        fi = np.arange(0, 8 * np.pi , np.pi / 180 )
        b = float(input(' b ')) 
        r = 2.718** ( b * fi ) 
        
        x = r * np.cos(fi)
        y = r * np.sin(fi)
        
        plt.plot( x , y )
        plt.axis('equal')
        plt.show()
   
    
    elif T == 2 :
        fi = np.arange(0, 8 * np.pi , np.pi / 180 )
        k = float(input(' k '))

        r = k * fi 

        x = r * np.cos(fi)
        y = r * np.sin(fi)
        
        plt.plot( x , y )
        plt.axis('equal')
        plt.show()

        
    elif T == 3:
        fi = np.arange( 0.1 , 8 * np.pi , np.pi / 180 )
        k = float(input(' k '))

        r = k / ( fi )**0.5

        x = r * np.cos(fi)
        y = r * np.sin(fi)
        
        plt.plot( x , y )
        plt.axis('equal')
        plt.show()
        

    elif T == 4:
        
        fi = np.arange( 0.1 , 13 * np.pi , np.pi / 180 )
        k = float(input(' k ( положительное )'))

        r = k / ( fi )**0.5

        x = r * np.cos(fi)
        y = r * np.sin(fi)
        
        plt.plot( x , y )
        plt.axis('equal')
        plt.show()
        
    else:
        print('нипонятно чеов вы там хотите')


risuem()