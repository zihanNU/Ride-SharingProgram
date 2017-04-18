import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math



if __name__ == "__main__":
#def draw():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    lookdata=open('networklink_xy_node.csv','r')
    lines=lookdata.readlines()
    #lktable = np.array([ map(str,lines[0].rstrip('\n').split(' '))])
    for i in range(len(lines)):
        data=lines[i].rstrip('\n').split(',')
        y=[float(data[1]),float(data[3])]
        x=[float(data[0]),float(data[2])]
        z=[float(data[4]),float(data[4])]
        ax.plot(x,y,z,color='darkblue',linewidth = 0.3)
    ax.view_init(azim=-75)
    ax.set_ylim(ymin=41.85)
    ax.set_xlim(xmax=-87.60)
   # ax.set_ylim(ymin=0.10, ymax=0.45)
##    yl=[0.00,0.05,0.10,0.15,0.20,0.25,0.30,0.35,0.40]
##    ylabel=["41.96","42.01","42.06","42.11","42.16","42.21","42.26"]
##    xl=[0.10,0.15,0.20,0.25,0.30,0.35,0.40,0.45]
##    xlabel=["-87.80","-87.75","-87,70","-87,65","-87,60"]
    zlabel=["6:00","6:20","6:40","7:00","7:20","7:40","8:00","8:20","8:40","9:00"]
    ax.set_ylabel('Latitude')
##    ax.set_yticklabels(ylabel)
    #ax.set_xlim([-87,-88])
    ax.set_xlabel('Longitude')
##    ax.set_xticklabels(xlabel)
    #ax.set_ylim([41,42])
    ax.set_zlabel('T')
    ax.set_zlim([60,240])
    ax.set_zticklabels(zlabel)
    plt.show()
    #return
