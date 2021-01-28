# -*- coding: utf-8 -*-
"""
Created on Tue Sep 29 15:25:19 2020

@author: GEUGYFH
"""

import scipy as sc
from scipy import signal
import pyqtgraph as pg
import numpy as np
import pandas as pd
import sys
import glob, os
import mdfreader
import matplotlib.pyplot as plt
from matplotlib.pyplot import figure

# file1 = open("20200831_SK216220050_OBD_DL_DIAGRA_LOGS_After DTC Clear_MQ.txt","r") 

# Ora_l=file1.readlines()
# print(Ora_l[2812])


i=0
base=r'\\vfesseatmare\EA\EA_1\Proyectos_VW\1,0 TSI EA211 MQB27 RdW 350bar\14_Emission_Abgas\VW216000388_WVGZZZC1ZLY000040_T_Cross_DQ_Negro'
files=os.listdir(base)
Data=[]
Time=[]

info=mdfreader.MdfInfo()

for root, directories, files in os.walk(base, topdown=False):
    for name in files:
        if name.endswith('.mf4') or name.endswith('.dat'):
            
            print(root + '/' + name)
            # label='DFC_st.DFC_TWCDPriCatB1'
            channels=info.list_channels(root + '/' + name)
            channels.sort()
            
            Channel_list=['DFC_st.DFC_TWCDPriCatB1','APP_r','ExhMod_tCat1B1','tmot','VehV_v']
            for idlaod in range(0,len(Channel_list)):
                yop=mdfreader.Mdf(root + '/' + name, channel_list=[Channel_list[idlaod]], convert_after_read=True)
                Load_D=yop.get_channel(Channel_list[idlaod])
                Data.append(Load_D['data'])
                time_Name=yop.get_channel_master(Channel_list[idlaod])
                Load_T=yop.get_channel(time_Name)
                Time.append(Load_T['data'])
                
        
           
            figure(num=None, figsize=(14, 8), dpi=120, facecolor='w', edgecolor='k')
            
            ax1=plt.subplot(2, 1, 1)
            plt.title(name)
            plt.xlabel('Time')
            plt.ylabel('VehV_v')
            plt.plot(Time[4+i],Data[4+i],'r')
            plt.plot(Time[3+i],Data[3+i],'r')
            plt.plot(Time[i],Data[i],'b')
            plt.grid(True, color="k",)
            plt.ylim(0,140)
            
            ax1=plt.subplot(2, 1, 2)
            plt.plot(Time[2+i],Data[2+i],'r')
            plt.plot(Time[1+i],Data[1+i],'b')
            plt.grid(True, color="k",)
            plt.ylim(0,700)
            
            i=i+5
            plt.show()
            


                        
# Data_AQ=[Date_AQ,[float(i) for i in Ora_AQ],[float(i) for i in Fra_AQ],[float(i) for i in Fho_AQ],[float(i) for i in tmot_AQ],[float(i) for i in tans_AQ],[float(i) for i in tumg_AQ]]

# Data_MQ=[Date_MQ,[float(i) for i in Ora_MQ],[float(i) for i in Fra_MQ],[float(i) for i in Fho_MQ],[float(i) for i in tmot_MQ],[float(i) for i in tans_MQ],[float(i) for i in tumg_MQ]]

# df = pd.DataFrame(Data_AQ)      
#     ## save to xlsx file       
# filepath = 'DataAQ.xlsx'
#     # with pd.ExcelWriter(filepath, engine="openpyxl",mode='a') as writer:  
#     #     df.to_excel(writer)
# df.to_excel(filepath, index=False)
# df = pd.DataFrame(Data_MQ)      
#     ## save to xlsx file       
# filepath = 'DataMQ.xlsx'
#     # with pd.ExcelWriter(filepath, engine="openpyxl",mode='a') as writer:  
#     #     df.to_excel(writer)
# df.to_excel(filepath, index=False)

            
            
#             # print(Ora_l[2812])
            
# # 	for name in directories:
# 		print(os.path.join(root, name))