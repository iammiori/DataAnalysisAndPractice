import numpy as np

class CalculSim(object):
    
    #cos sim
    def cos(self,rating_file):
        rating = np.load(rating_file)
        rating[np.isnan(rating)] = 0.0
        NumUsers = np.size(rating,axis=0)
        Sim = np.full((NumUsers,NumUsers),0.0)
        print("---- calculating cos similarity ----")
        for u in range(0,NumUsers):
            for v in range(u, NumUsers):
                InnerDot = np.dot(rating[u,],rating[v])
                NormU = np.linalg.norm(rating[u,])
                NormV = np.linalg.norm(rating[v,])
                Sim[u,v] = InnerDot/(NormU*NormV)
                Sim[v,u] = Sim[u,v]
                
        print("cos sim is : \n{}".format(Sim))
        return Sim
        
        
    #PCC sim
    ## 개개인의 평점 평균을 통해 비교해서 보는 것이 특징
    ## 대각행렬의 값은 항상 1이므로, nan 이라도 1로 출력
    ## nan 값일때 무시하는 코드를 짜려 했으나 이경우 계산값이 다르게 나오므로 0으로 대체
    ## 교안 값이랑 같은것으로 보아 코드를 잘 짬. :)
    
    def PCC(self, rating_file):
        rating = np.load(rating_file)
        rating[np.isnan(rating)] = 0.0
        
        # row 개수
        NumUsers = np.size(rating, axis=0)
        # Sim matrix 초기화
        Sim = np.full((NumUsers,NumUsers),0.0)
        # 각 row 마다 0은 제외하고 mean 값구하기
        mean = np.nanmean(np.where(rating!=0,rating,np.nan),axis=1)

        print("\n---- calculating PCC similarity ----")        
        for u in range(0,NumUsers):
            for v in range(u,NumUsers):
                arridx_u = np.where(rating[u,]==0)
                arridx_v = np.where(rating[v,]==0)
                arridx = np.concatenate((arridx_u,arridx_v),axis=None)
                
                U = np.delete(rating[u,],arridx)
                V = np.delete(rating[v,],arridx)
                
                U = U-mean[u]
                V = V-mean[v]
                
            # NaN 값이 들어가는 경우가 있어서 , 0으로 대체
                if len(U) == 0:
                    U = np.array([0.0])
                    V = np.array([0.0])
                    
                InnerDot = np.dot(U,V)
                NormU = np.linalg.norm(U)
                NormV = np.linalg.norm(V)
                
                if u==v:
                    # 자기 자신일때
                    Sim[u,v] = 1.0
                else:
                    if NormU == 0 or NormV==0:
                    # 하나라도 0이면
                        Sim[u,v] = 0.0
                    else:
                        Sim[u,v] = InnerDot/(NormU*NormV)
                        
                Sim[v,u] = Sim[u,v]
                
        print("PCC sim is : \n{}".format(Sim))
        return Sim
    
    
    def Jac(self,rating_file):
        rating = np.load(rating_file)
        rating[np.isnan(rating)] = 0.0
        
        # Jaccard measure = 둘다 평점을 한경우 / 둘중 한명이라고 평점을 한 경우
        # row 개수
        NumUsers = np.size(rating, axis=0)
        # Sim matrix 초기화
        Sim = np.full((NumUsers,NumUsers),0.0)
        # 각 row 마다 0은 제외하고 mean 값구하기
        
        print("\n---- calculating JAC similarity ----")        
        for u in range(0,NumUsers):
            for v in range(u,NumUsers):
                U = np.array(rating[u,]>0,dtype=np.int)
                V = np.array(rating[v,]>0,dtype=np.int)
                SumUV = U + V
                
                Inter = np.sum(np.array(SumUV>1, dtype=np.int))
                Union = np.sum(np.array(SumUV>0, dtype=np.int))
                
                tmp = Inter/Union
                Sim[u,v] = tmp
                Sim[v,u] = Sim[u,v]
                
        print("JAC sim is : \n{}".format(Sim))
        return Sim                
                