# -*- coding: utf-8 -*-
"""
Created on Tue Nov 26 11:19:12 2019

@author: Pimprenelle
"""
import numpy as np
import matplotlib.pyplot as plt

n=6
U=[-1,1,-1,1,1,-1]
chem=[1,2,3,5,4,0]

def dessineStations(n,posStations):
    R=2
    for i in range(0,n):
        if U[i]==-1:
            plt.plot([R*np.cos(2*np.pi/n*i)],[R*np.sin(2*np.pi/n*i)],'bo')
        else:
            plt.plot([R*np.cos(2*np.pi/n*i)],[R*np.sin(2*np.pi/n*i)],'ro')
    
dessineStations(n,posStations)

def dessineChemin(n,chem):
    R=1.5
    dIni=2*np.pi/n*chem[0]
    posInix=R*np.cos(2*np.pi/n*chem[0])
    posIniy=R*np.sin(2*np.pi/n*chem[0])
    for i in range(n-1):
        print(chem[i],chem[i+1])
        dIni=2*np.pi/n*chem[i]
        dCible=2*np.pi/n*chem[i+1]
        posInix=R*np.cos(2*np.pi/n*chem[i])
        posIniy=R*np.sin(2*np.pi/n*chem[i])
        if chem[i]<chem[i+1]:
            val = np.linspace(dIni, dCible, 30)
        else:
            val = np.linspace(dIni, dCible+2*np.pi, 30)
        x=[R*np.cos(v) for v in val]
        y=[R*np.sin(v) for v in val]
        if U[i]==-1:#camion vide
            plt.plot([posInix],[posIniy],'ko')
            plt.plot(x,y,'k')
        else:
            plt.plot(x,y,'g')
            plt.plot([posInix],[posIniy],'go')
        R=R*0.9
    return()
    
dessineChemin(n,chem)