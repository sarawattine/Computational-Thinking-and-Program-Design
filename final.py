#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Fri Jun  5 15:53:45 2020

@author: melody16
"""
import random


n="again"
list1=["Lauv-Paris in the rain","王若琳-I love you","陳鴻宇-理想三旬","Talor Swift-bad blood","伍百-與妳到永久","周華健-雨人","賴慈泓-我只能在夢裡","鄭興-台北下的雨","好妹妹樂隊-往事只能回味","鄭興-過於喧囂的孤獨"]
list2=["The Walters-I love you so","Ed Sheeren&Justin Bieber-I don't care","Peach it-peach it","王若琳-檸檬樹","Soulfa-Lover song","椅子樂團-日常的鏡頭","椅子樂團-Rollin on","白安-所愛之初","五月天-笑忘歌","無妄合作社-山頭"]
list3=["郁可唯-時間煮雨","Frozen-Do you want to build a snowman","蘇打綠-痛快的哀豔","蘇打綠-牆外的風景","蘇打綠-everyone","蘇打綠-未了","馬頔-傲寒","劉昊霖-兒時","劉昊霖-landing guy","Carpenters-yesterday once more"]
while n=="again":
    a=input("請輸入今日的天氣:")
    if a=="雨天":
        print("那推薦你幾首歌來搭配今天的天氣吧")
        list4=random.sample(list1,3)
        for i in range(3):
            w=list4[i]
            print(w)
        n=input("如果要在執行一次請輸入again，若要結束請按enter:")   
        
    elif a=="晴天":
        print("那推薦你幾首歌來搭配今天的天氣吧")
        list4=random.sample(list2,3)
        for i in range(3):
            w=list4[i]
            print(w)
        n=input("如果要在執行一次請輸入again，若要結束請按enter:") 
       
    elif a=="下雪":
        print("那推薦你幾首歌來搭配今天的天氣吧")
        list4=random.sample(list3,3)
        for i in range(3):
            w=list4[i]
            print(w)
        n=input("如果要在執行一次請輸入again，若要結束請按enter:") 
        
    else:
        print("此天氣不在服務範圍內")
        n=input("如果要在執行一次請輸入again，若要結束請按enter:") 
print("那我們下次再見吧！祝你有美好的一天！另外，記得出門要勤洗手和戴口罩歐～")
