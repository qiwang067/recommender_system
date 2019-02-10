# -*- coding: utf-8 -*-
"""
@author: wq

"""
from math import sqrt

users={
      'A': {
              'soap': 2, 
              'book': 3,
              'football': 3, 
              'basketball': 3, 
              'tissue': 2, 
              'lamp': 3
            },
      'B': {
              'soap': 3, 
              'book': 3, 
              'football': 1, 
              'basketball': 5, 
              'lamp': 3, 
              'tissue': 3
            },      
      'C': {
              'soap': 2, 
              'book': 3,
              'basketball': 3, 
              'lamp': 4
            },     
      'D': {
              'book': 3, 
              'football': 3,
              'lamp': 4, 
              'basketball': 4, 
              'tissue': 2
            },     
      'E': {
              'soap': 3,
              'book': 4, 
              'football': 2,
              'basketball': 3, 
              'lamp': 3,
              'tissue': 2
            },      
      'F': {
              'soap': 3, 
              'book': 4,
              'lamp': 3,
              'basketball': 5, 
              'tissue': 3
            },     
      'G': {
              'book':4,
              'tissue':1,
              'basketball':4
            }
}

# 计算用户之间的相似度(欧几里得距离) ,prefs(preferences)
def sim_distance(prefs,person1,person2):
  si={}  #共有物品列表(share item)
  for item in prefs[person1]: 
    if item in prefs[person2]: si[item]=1
  if len(si)==0: return 0
  sum_of_squares=sum([pow(prefs[person1][item]-prefs[person2][item],2) 
                      for item in prefs[person1] if item in prefs[person2]])
  return 1/(1+sqrt(sum_of_squares))


#计算用户之间的相似度(皮尔逊相关系数)
def sim_pearson(prefs,p1,p2):
  si={}
  for item in prefs[p1]: 
    if item in prefs[p2]: si[item]=1
  if len(si)==0: return 0
  n=len(si)
  sum1=sum([prefs[p1][it] for it in si])
  sum2=sum([prefs[p2][it] for it in si])
  sum1Sq=sum([pow(prefs[p1][it],2) for it in si])  #square sum(平方和)
  sum2Sq=sum([pow(prefs[p2][it],2) for it in si])	
  pSum=sum([prefs[p1][it]*prefs[p2][it] for it in si])
  num=pSum-(sum1*sum2/n)  
  den=sqrt((sum1Sq-pow(sum1,2)/n)*(sum2Sq-pow(sum2,2)/n))
  if den==0: return 0
  r=num/den
  return r


#选出与指定目标最相似的人(使用皮尔逊相关)
def topMatches(prefs,person,n=5,similarity=sim_pearson):
  scores=[(similarity(prefs,person,other),other)   #列表推导式
                  for other in prefs if other!=person]
  scores.sort()
  scores.reverse()
  return scores[0:n]



#基于用户过滤(通过加权平均数来得到推荐结果)
def getRecsByUsers(prefs,person,similarity=sim_pearson):  #Recs(recommendations)
  totals={}  
  simSums={}
  ranking1=[]  #推荐物品列表
  for other in prefs:
    if other==person: continue
    sim=similarity(prefs,person,other)
    if sim<=0: continue
    for item in prefs[other]:
      if item not in prefs[person] or prefs[person][item]==0:   
        totals.setdefault(item,0)    #没有物品时设为0
        totals[item]+=prefs[other][item]*sim  # 用户相似度*评价值
        simSums.setdefault(item,0)
        simSums[item]+=sim   # 相似度之和
  rankings=[(total/simSums[item],item) for item,total in totals.items()]   # 归一化的列表
  rankings.sort()
  rankings.reverse()
  for x in rankings:
      ranking1.append(x[1]) 
  return ranking1


#将商品与用户对换
def transformprefs(prefs):
  result={}
  for person in prefs:
    for item in prefs[person]:
      result.setdefault(item,{})
      result[item][person]=prefs[person][item]  
  return result

#计算物品相似度
def calculateSimilarItems(prefs,n=10):
  result={}
  itemprefs=transformprefs(prefs) 
  c=0
  for item in itemprefs:
    c+=1
    if c%100==0: print (("%d / %d") % (c,len(itemprefs))) #针对大数据集，输出程序运行进度
    scores=topMatches(itemprefs,item,n=n,similarity=sim_distance)
    result[item]=scores
  return result

#基于物品过滤(通过加权和来得到推荐结果)
def getRecsByItems(prefs,itemMatch,user):
  userRatings=prefs[user]
  ranking1=[]
  scores={}
  totalSim={}
  for (item,rating) in userRatings.items( ):
    for (similarity,item2) in itemMatch[item]:
      if item2 in userRatings: continue
      scores.setdefault(item2,0)
      scores[item2]+=similarity*rating  #评价值与相似度的加权和
      totalSim.setdefault(item2,0)
      totalSim[item2]+=similarity
  rankings=[(score/totalSim[item],item) for item,score in scores.items( )]
  rankings.sort( )   
  rankings.reverse( )
  for x in rankings:
      ranking1.append(x[1]) 
  return ranking1





