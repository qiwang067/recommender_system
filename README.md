# Recommend-System
## 介绍
1. 分别使用基于用户的协作型过滤算法和基于物品的协作型过滤算法来达到推荐商品的目的
2. 用欧几里得距离或皮尔逊相关系数来计算相似度。
3. 用0 ~ 5来表示用户对商品的评价，标准如下。

| 商品记录 |评分 |
| --- | --- |
|  商品未购买|  0|
|  商品已浏览 | 1 |
| 商品已收藏 | 2 |
|商品已购买   |3  |
|商品已好评   | 4 |
| 商品追评为好评| 5 |


4. 程序中共创建了7个用户和6个商品。7个用户即 A，B，C，D，E，F，G；6个商品即soap ，book，football，basketball ，tissue，lamp。
5. 对于稀疏数据集，基于物品的过滤算法要优于基于用户过滤的算法，对于密集数据集，两者效果几乎相同。

## 运行程序
### 基于用户协同过滤（推荐给用户G的商品）
![图片1](https://github.com/qiwang067/MarkdownPhotos/blob/master/%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F1.png)

### 基于物品的协作型过滤（推荐给用户G的商品）
![图片2](https://github.com/qiwang067/MarkdownPhotos/blob/master/%E6%8E%A8%E8%8D%90%E7%B3%BB%E7%BB%9F2.png)

说明：itemsim是商品相似度的数据集
