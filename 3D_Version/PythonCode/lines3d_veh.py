import matplotlib as mpl
from mpl_toolkits.mplot3d import Axes3D
import numpy as np
import matplotlib.pyplot as plt
import math

cluster1=[15305,22384,24776,25495,25496,25497]					
cluster2=[28509,28510,28953,29264,31178,31339,31340,31790,32568,3478,36062]
cluster3=[41990,42137,42315,42467,42468,43621]					
cluster4=[44100,46857,47554,49932,50760,50761,50762,5716,60857]		
cluster5=[68849,70100,70648,92919,100223,102020,106343,114423,114750,115245,115755]
cluster6=[171778,171887,174183,174627,174722,176564]					
cluster7=[18766,19110,19508,19759,20613,21384,22593,23277,23567,24579,26265,26675,27256,27394,27395,28900,29355]	
cluster8=[52103,53849,54564,55114,55452,55637,18498]											
cluster9=[12394,14138,14621,15473,17482,17866]												
cluster10=[29960,30284,32216,33425,34075,44197,47656]											
cluster11=[83194,83195,83559,83917,85621,85996,87474,87477,87854,89679,91317,91681,93762,94868,95410,96600,97273,97793]
cluster12=[110140,110630,110632,113109,113403,114031,115335,118560,121223]									


#if __name__ == "__main__":
def writetoline():
    mpl.rcParams['legend.fontsize'] = 10
    rfile=open('plottrapython.csv','r')
    wfile=open('plotall.csv','w')
    tratable=[]
    tratable = np.array([ map(str,line.rstrip('\n').split(',')) for line in rfile ])
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    ax.set_xlim([1200, 2100])
    ax.set_ylim([2000, 3200])
    ax.set_zlim([90, 150])
    x=[]
    y=[]
    z=[]
    r=3959 #radius of world
    for i in range(1,len(tratable)-1):
        Pid=tratable[i][0]
        Pid2=tratable[i+1][0]
        lon=87.9+float(tratable[i][1])
        lat=float(tratable[i][2])-41.86
        x0=r*math.cos(lon)*math.sin(90-lat)
        y0=r*math.sin(lon)*math.sin(90-lat)
        t0=float(tratable[i][3])
        if Pid==Pid2:
            x.append(x0)
            y.append(y0)
            z.append(t0)
            wfile.write(str(x0)+';'+str(y0)+';'+str(t0)+',')
        else:
            #ax.plot(x, y, z, label='trajectory')
            wfile.write('\n')
            del x[0:len(x)]
            del y[0:len(y)]
            del z[0:len(z)]
    #ax.plot(x, y, z, label='trajectory')  
    rfile.close
    #plt.show()
    wfile.close
    #fig.savefig('out.png')
    return

def testt():
    fig = plt.figure()
    fa = fig.gca(projection='3d')
    a=[1556.621882152673, 1546.5368971542175, 1545.7975783235, 1550.0022387441093, 1552.364342975563, 1553.867015465439, 1555.5768408764188, 1574.6683939241607, 1580.5655138549646, 1609.829388661827, 1629.926189127353, 1643.800522696955, 1654.8682833676971, 1651.206784868303, 1651.7941121894155, 1654.8326154241934, 1663.3654439056304, 1666.4274559439023, 1669.1432474852677, 1667.2583401183015, 1664.924891438302, 1685.6009350914167, 1689.284280619327, 1693.700170997535, 1705.2494984128232, 1709.0321924102107, 1712.759779481918, 1723.1185914355524, 1726.6561560345285, 1730.2164143150324, 1743.294207737349, 1747.7540220691403, 1752.906212601009, 1752.0193305760051, 1735.0305001998938, 1717.1610521335235, 1704.6639263220259, 1699.8211650823882, 1680.717021087376, 1674.3969843035968, 1631.1491797224985, 1627.453993662078, 1600.9580599022709, 1577.4368296582984, 1569.7063701456646, 1563.411512578441, 1563.7195716662045, 1567.5669944379931, 1568.7835213394812, 1575.9803344565792, 1578.0806034169736, 1576.9461884127993, 1570.349087756459]
    b=[3127.3704904481165, 3107.525750496912, 3102.5501450688503, 3091.3985040551906, 3077.087386442378, 3065.496707481215, 3061.450069436329, 3040.841941170893, 3034.9228511632873, 3002.1722218024333, 2977.099668106009, 2957.8081486099895, 2902.3749856102527, 2895.2588655282216, 2883.4494882481868, 2878.7674868988447, 2866.4035065298217, 2854.6507431285295, 2841.7513123186686, 2834.966055961739, 2826.639264723779, 2782.3122283043313, 2773.040857691154, 2761.6681463395807, 2730.7201569219174, 2720.4995026612073, 2710.2547840644374, 2680.3309967820746, 2669.655509021345, 2658.940550058237, 2615.0403323474065, 2604.1768884702783, 2592.658153224086, 2583.745199986193, 2558.3394084881343, 2531.764884388973, 2520.940214266296, 2517.45784628155, 2504.8516443226813, 2500.226712259353, 2485.6415399135167, 2484.9803052768984, 2480.268039483129, 2478.8599006217432, 2475.833955943158, 2463.4549544452107, 2458.396933673241, 2429.186580812154, 2420.0523316894623, 2408.2924913736683, 2403.166394947103, 2395.1434922937974, 2377.4675024338426]
    c=[94.4, 94.7, 94.8, 95.1, 95.4, 95.7, 95.8, 96.2, 96.3, 97.0, 97.5, 97.9, 99.1, 99.3, 99.6, 99.7, 100.0, 100.3, 100.6, 100.8, 101.0, 101.9, 102.1, 102.3, 102.9, 103.1, 103.3, 104.0, 104.2, 104.4, 105.4, 105.6, 105.8, 106.0, 107.9, 108.9, 109.5, 109.6, 110.3, 110.4, 111.3, 111.4, 111.9, 112.3, 112.5, 112.8, 112.9, 113.5, 113.7, 113.9, 114.0, 114.2, 114.6]
    fa.plot(a,b,c)
    plt.show()
    return

if __name__ == "__main__":
#def draw():
    fig = plt.figure()
    ax = fig.gca(projection='3d')
    lookdata=open('plotall.csv','r')
    lines=lookdata.readlines()
    #lktable = np.array([ map(str,lines[0].rstrip('\n').split(' '))])
    for p in cluster1:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster2:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster3:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster4:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster12:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster6:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster11:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster8:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster9:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    for p in cluster10:
        i=p-1
        data=lines[i].rstrip('\n').split(',')
        x=[]
        y=[]
        z=[]
        for j in range(0,len(data)):
            item=data[j].split(';')
            if len(item)<=1:
                continue
            x.append(float(item[0]))
            y.append(float(item[1]))   
            z.append(float(item[2]))
        ax.plot(x,y,z)
    lookdata.close()
    ax.set_xlabel('X')
    ax.set_ylabel('Y')
    ax.set_zlabel('T')
    plt.show()
    #return
