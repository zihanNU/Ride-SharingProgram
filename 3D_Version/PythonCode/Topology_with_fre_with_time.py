__author__ = 'Zihan'

import math
import numpy as np
import matplotlib.pyplot as plt

def lookup():   #lktable is link to node pair look-up table, start from 1
    lookdata=open('networklink_lookup.csv','r')
    lktable=[]
    #lktable = np.array([ map(str,line.rstrip('\n').split(',')) for line in lookdata ])
    for line in lookdata:
        item=line.rstrip('\n').split(',')
        lktable.append(['L'+item[0],item[1],item[2],'0',item[3]])
    lookdata.close()
    return lktable

def xylookup(lktable):
    xydata=open('xy.dat','r')
    lines=xydata.readlines()
    xylist = [ map(float,line.split( )) for line in lines ]
    xy= np.array(xylist)
    xydata.close
    tra=open('links_path_time.csv','r')
    lines=tra.readlines()
##    traxy=open('plottrajectory.csv','w')
    traxyplot=open('plottrapython.csv','w')
##    traxy.write('PID,LID,n1,n2,x1,y1,x2,y2,t\n')
    traxyplot.write('PID,x,y,GX,GY,t\n')  #new
    j=0
    while j<len(lines):
        nodes=lines[j].split(',')
        times=lines[j+1].split(',')
        pid=nodes[0]
        traseq=[]
        r=3959
        for k in range(1,len(nodes)):
            #print nodes
            #print nodes[k]
            Lid=int(nodes[k].lstrip('L'))-1
            nodeid1=float(lktable[Lid][1])
            nodeid2=float(lktable[Lid][2])
            k1=list(xy[:,0]).index(nodeid1)
            x1=xy[k1][1]
            y1=-xy[k1][2]
            k2=list(xy[:,0]).index(nodeid2)
            x2=xy[k2][1]
            y2=-xy[k2][2]
            lon=113+x1
            lat=y1-40
            gx=r*math.cos(lon)*math.sin(90-lat)
            gy=r*math.sin(lon)*math.sin(90-lat)
##            traxy.write(nodes[0]+','+nodes[k].rstrip('\n')+','+str(int(nodeid1))+','+str(int(nodeid2))+','+str(x1)+','+str(y1)+','+str(x2)+','+str(y2)+','+times[k].rstrip('\n')+'\n')
            traseq.append([x1,y1,times[k]])
            traxyplot.write(pid+','+str(x1)+','+str(y1)+','+times[k].rstrip('\n')+'\n')  #new
        j=j+2
    tra.close
##    traxy.close
    traxyplot.close
    return               


def path(lktable):
    tra=open('vehicles.dat','r')
    lines=tra.readlines()
    trapath=open('links_path_time.csv','w')
    i=2
    pathlist=[]
    pathid=0
    while i < (len(lines)):
        pathid=pathid+1
        nodes=lines[i].rstrip('\n').split( )
        times=lines[i+1].rstrip('\n').split( )
        linkseq=['P'+str(pathid)]
        timeseq=['T'+str(pathid)]
        for j in range(1,len(nodes)):
            n1=nodes[j-1]
            n2=nodes[j]
            for k in range (0,len(lktable)):
                if n1==lktable[k][1] and n2==lktable[k][2]:
                    linkseq.append(lktable[k][0])  #pathid, path sequences
                    if len(linkseq)==2:
                        starttime=float(times[j-1])
                        timeseq.append(times[j-1])
                    else:
                        exittime=float(times[j-1])
                        timeseq.append(str(starttime+exittime))
        pathlist.append(linkseq)
        trapath.write(','.join(linkseq)+'\n')
        trapath.write(','.join(timeseq)+'\n')
        i=i+5
    tra.close
    trapath.close
    return pathlist

def connectlink(linklist,n1,n2):
    uplinklist=[]
    downlinklist=[]
    for i in range(len(linklist)):
        if linklist[i][2]==n1:
            uplinklist.append(linklist[i][0])
        if linklist[i][1]==n2:
            downlinklist.append(linklist[i][0])
    return uplinklist,downlinklist

def topo(mergelist):
    mergedata=open('topology.csv','w')
    mergedata2=open('topology_copy.csv','w')
    for i in range(len(mergelist)):
        n1=mergelist[i][1]
        n2=mergelist[i][2]
        up,down=connectlink(mergelist,n1,n2)
        mergedata2.write(','.join(mergelist[i])+','+str(len(up))+','+','.join(up)+','+str(len(down))+','+','.join(down)+'\n')
        mergedata.write(mergelist[i][0]+','+mergelist[i][-2]+','+mergelist[i][-1]+','+str(len(up))+','+','.join(up)+','+str(len(down))+','+','.join(down)+'\n')
    mergedata.close
    mergedata2.close
    return

def fre_connect(linklist,link,tag,theta):   # find the most frequent link
#tag, link in the middle, search two sides, 0; link in the upside,search up side, 1; link in downside,search down side,2
    uplinks=[]
    dnlinks=[]
    freup=[]
    fredn=[]
    target=int(link.lstrip('L'))-1  #find the target link, and it tells the connecting links
    up=int(linklist[target][3])  #3rd is up;
    down=int(linklist[target][4+max(up,1)])
    for i in range(up):   #link from 1, but Lid from 0
        Lid=int(linklist[target][4+i].lstrip('L'))-1
        uplinks.append(linklist[target][4+i])  #4 non linkid before
        if linklist[target][4+i] not in theta:
            freup.append(int(linklist[Lid][1]))
        else:
            freup.append(-1)   # if already in the theta, set the fre as -1
    for j in range(down):
        Lid=int(linklist[target][5+max(up,1)+j].lstrip('L'))-1
        dnlinks.append(linklist[target][5+max(up,1)+j])  #id,fre,length,up,down, 5 non linkid
        if linklist[target][5+max(up,1)+j] not in theta:
            fredn.append(int(linklist[Lid][1]))
        if linklist[target][5+max(up,1)+j] in theta:
            fredn.append(-1)
   # maxfreup=freup.index(max(freup))
   # maxfredn=fredn.index(max(fredn))   # still with logic error, becouse it could be that [1,2][]
    fre=freup+fredn
    if tag==0:
        if max(freup+fredn)<=0:
            return -1,'L-1',-1 # cannot find more links
        elif fre.index(max(fre))<up:   # if in the up list
            return 0,uplinks[freup.index(max(freup))],max(freup)   # 0 insert at the head, 1 append at the back
        else:
            return 1,dnlinks[fredn.index(max(fredn))],max(fredn)
    if tag==1 and np.any(freup):   # find the up link
        return 0,uplinks[freup.index(max(freup))],max(freup)
    if tag==2 and np.any(fredn):
        return 1,dnlinks[fredn.index(max(fredn))],max(fredn)
    return -1,'L-1',-1 # cannot find more links


def fre_count(linklist,pathlist,phi,flag):
    count=[0]*len(linklist)
    for pathid in phi:
        pid=int(pathid.lstrip('P'))-1
        for link in pathlist[pid][1:len(pathlist[pid])]:
            Lid=int(link.lstrip('L'))-1
            count[Lid]=count[Lid]+1
    for i in range (len(linklist)):
        linklist[i][1]=str(count[i])
    if flag:
        fredata=open('topology_copy'+str(flag)+'.csv','w')
        for i in range (len(linklist)):        
            fredata.write(','.join(linklist[i])+'\n')
        fredata.close
    return linklist,count.index(max(count))


def DBSCAN(alpha):
    cluster1=open('clusterfre'+str(alpha)+'.csv','w')
    cluster=open('cluster'+str(alpha)+'.csv','w')
    clusterpath=open('clusterpath'+str(alpha)+'.csv','w')
    linkdata=open('topology_copy.csv','r')
    linklist=[ map(str,line.rstrip('\n').split(',')) for line in linkdata ]
    pathdata=open('links_path.csv','r')
    pathlist=[ map(str,line.rstrip('\n').split(',')) for line in pathdata ]
    pathdata.close
    psi=[]
    pathidlist=[]
    t=1
    for i in range(len(pathlist)):
        pathidlist.append(pathlist[i][0])
    while (t):
        #print t
        t=t+1
        theta=[]
        fre_theta=[]   #record frequency
        phi=[]
        linklist,maxid=fre_count(linklist,pathlist,pathidlist,0)
        link=linklist[maxid][0]
        if int(linklist[maxid][1])<alpha:
            break
        theta.append(link)
        fre_theta.append(linklist[maxid][1])
        alphaflag=1
        #pathidlist=np.array(pathlist)[:,0].tolist()  too many indices
        for i in range(0,len(pathlist)):  #step4
            if link in pathlist[i]:
                phi.append(pathlist[i][0])
        while (alphaflag):   #step 7, repeat 5,6
            #theta_old=np.array(theta)
            #fre_theta_old=np.array(fre_theta)
            #phi_old=np.array(phi)
            if len(theta)==1:
                flag,conlink,fre=fre_connect(linklist,link,0,theta)
                Lid=int(conlink.lstrip("L"))-1
                if flag==0:
                    theta.insert(0,conlink)
                    fre_theta.insert(0,linklist[Lid][1])
                if flag>0:
                    theta.append(conlink)
                    fre_theta.append(linklist[Lid][1])
                if flag<0:
                    #print flag,fre,conlink,link
                    alphaflag=0  #no more connected more than alpha
                    cluster.write(','.join(theta)+'\n')
                    cluster1.write(','.join(theta)+'\n')
                    #print theta
                    cluster1.write(','.join(fre_theta)+'\n')
                    #print fre_theta
                    clusterpath.write(','.join(phi)+'\n')
                    psi.append(theta)  #step 8
                    break
                #print theta
            if len(theta)>1:
                link1=theta[0]
                link2=theta[-1]
                flag1,conlink1,fre1=fre_connect(linklist,link1,1,theta)
                flag2,conlink2,fre2=fre_connect(linklist,link2,2,theta)
                if fre2>=fre1 and fre2>alpha:
                    theta.append(conlink2)
                    Lid=int(conlink2.lstrip("L"))-1
                    fre_theta.append(linklist[Lid][1])
                elif fre1>fre2 and fre1>alpha:
                    #print 'fre1',fre1
                    theta.insert(0,conlink1)
                    Lid=int(conlink1.lstrip("L"))-1
                    fre_theta.insert(0,linklist[Lid][1])
                else:
                    alphaflag=0  #no more connected more than alpha
                    cluster.write(','.join(theta)+'\n')
                    cluster1.write(','.join(theta)+'\n')
                    #print theta
                    cluster1.write(','.join(fre_theta)+'\n')
                    #print fre_theta
                    clusterpath.write(','.join(phi)+'\n')
                    psi.append(theta)  #step 8
                    break  # after break, no need to update phi, but update pathlist
                #print theta
            #path_delete=[]  #store the phi id to be deleted
            for pathid in phi:  #step 6
                pid=int(pathid.lstrip('P'))-1
                #if theta not in pathlist[pid]:     #all the same
                if len(set(pathlist[pid]).intersection(set(theta)))!=len(theta):   #linkid start from 1   #activities, not to be all same
                    phi.remove(pathid)
            # update linklist after phi
            linklist,maxid=fre_count(linklist,pathlist,phi,0)
    #update pathlist  we can use set difference, but the sequence will be changed when we update
        for k in range (len(pathlist)):
            #pathlist[k]=list(set(pathlist[k]).difference(set(theta)))
            updatepath = [x for x in pathlist[k] if x not in theta]
            pathlist[k]=updatepath
    linkdata.close
    cluster.close
    clusterpath.close
    return len(psi)
#Another sorting: from operator import itemgetter

def vehmile(alpha,table):
    cluster=open('cluster'+str(alpha)+'.csv','r')
    CLU=cluster.readlines()
    clusterpath=open('clusterpath'+str(alpha)+'.csv','r')
    NUM=clusterpath.readlines()
    stat=open('cluster'+str(alpha)+'stat.csv','w')
    for i in range(0,len(CLU)):
        pathlist=NUM[i].split(',')
        IDlist=CLU[i].split(',')
        length=0
        for IDS in IDlist:
            Lid=int(IDS.lstrip('L'))-1
            length=float(table[Lid][-1])/5280+length
        stat.write('Cluster'+str(i+1)+','+str(length)+','+str(len(pathlist))+','+str(len(pathlist)*length)+'\n')
    stat.close
    cluster.close
    clusterpath.close
    return


if __name__ == "__main__":
    table=lookup()
    pathlist=path(table)
    #topo(table)
    xylookup(table)
 #   clusternumber=[]
    alphalist=[10,50,100,200,750,1000,2000]
    for alpha in alphalist:
        print 'alpha',alpha
        #clusternumber.append(DBSCAN(alpha))
        #vehmile(alpha,table)
#    plt.plot(range(1,2),clusternumber)
#    plt.xlabel("alpha")
#    plt.xlim(1,10)
#    plt.ylabel("number of clusters")
#    plt.ylim(0,100)
#    plt.show()
    print 'end'

def update_old(idlist,pathlist,pathidlist,phi):
    count=[0]*len(idlist)
    for pathid in phi:
        pid=pathidlist.index(pathid)
        for link in pathlist[pid][1:len(pathlist[pid])]:
            Lid=int(link.lstrip('L'))
            count[Lid]=count[Lid]+1
    return count
            
#    mergelist=merge(table)
def merge(lktable):
    mergelist=[]
    mergedata=open('link_fre_length.csv','w')
    fredata=open('link_fre.csv','r')
    fre = np.array([ map(str,line.rstrip('\n').split(',')) for line in fredata ])
    for i in range(0,len(fre)):
        n1=fre[i][0]
        n2=fre[i][1]
        for j in range (0,len(lktable)):
            if n1==lktable[j][1] and n2==lktable[j][2]:
                data=["L"+lktable[j][0],n1,n2,fre[i][2],lktable[j][3]]   #linkid, n1,n2,fre,length
                mergelist.append(data)
                mergedata.write("L"+lktable[j][0]+','+n1+','+n2+','+fre[i][2]+','+lktable[j][3]+'\n')
    mergedata.close
    fredata.close
    return mergelist
