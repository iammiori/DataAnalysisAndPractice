import numpy as np

class CalBase(object):
    
    
    
    # Basic CF
    def basic_CF(self, rating_file, sim, k):
        mat = np.load(rating_file)
        mat[np.isnan(mat)] = 0.0       
        # 구하고자 하는거 : predicted rating of a targer user u for an item i 
        predicted_rating = np.array([[0.0 for col in range(21601)] for row in range(380)])

        def COS(mat):
            # 행 개수 
            NumUsers = np.size(mat,axis=0)
            # 초기화
            Sim = np.full((NumUsers,NumUsers),0.0)
            for u in range(NumUsers):
                # 한 row 씩 보면서 0인 index 찾아
                arridx_u = np.where(mat[u,]==0)
                #print("arridx_u {} = {}\n".format(u, arridx_u))
                for v in range(u+1,NumUsers):
                    arridx_v = np.where(mat[v,]==0)
                    #print("arridx_v {} = {}\n".format(v, arridx_v))
                    arridx = np.unique(np.concatenate((arridx_u,arridx_v),axis=None))
                    #print("arridx {} = {}\n".format(v, arridx))

                    U = np.delete(mat[u,],arridx)
                    V = np.delete(mat[v,],arridx)

                    if (np.linalg.norm(U)==0 or np.linalg.norm(V)==0):
                        Sim[u,v] = 0
                    else:
                        Sim[u,v] = np.dot(U,V)/(np.linalg.norm(U)*np.linalg.norm(V))
                    Sim[v,u] = Sim[u,v]

            #print(arridx)

            return Sim        

        def PCC(mat):
            NumUsers = np.size(mat,axis=0)
            Sim = np.full((NumUsers,NumUsers),-1.0)

            mean = np.nanmean(np.where(mat!=0.0,mat,np.nan),axis=1)

            for u in range(NumUsers):
                arridx_u = np.where(mat[u,]==0)
                for v in range(u+1, NumUsers):
                    arridx_v = np.where(mat[v,]==0)
                    arridx = np.unique(np.concatenate((arridx_u,arridx_v),axis=None))

                    U = np.delete(mat[u,],arridx) - mean[u]
                    V = np.delete(mat[v,],arridx) - mean[v]

                    if (np.linalg.norm(U)==0 or np.linalg.norm(V)==0):
                        Sim[u,v] = 0
                    else:
                        Sim[u,v] = np.dot(U,V)/(np.linalg.norm(U)*np.linalg.norm(V))

                    Sim[v,u] = Sim[u,v]

                return Sim        
        
        
        if (sim == 'COS'):
            Sim = COS(mat)
        elif (sim == "PCC"):
            Sim = PCC(mat)

        k_neighbors = np.argsort(-Sim)
        k_neighbors = np.delete(k_neighbors,np.s_[k:],1)

        NumUsers = np.size(mat,axis=0)

        for u in range(NumUsers):
            list_sim = Sim[u,k_neighbors[u,]]
            list_rating = mat[k_neighbors[u,],].astype('float64')

            predicted_rating[u,] = np.sum(list_sim.reshape(-1,1)*list_rating,axis=0)/np.sum(list_sim)

        return predicted_rating   
    
    
    #Base line CF code
    #- 우선 모든 평균은 nan 을 제거 한 상태로 계산했다. \n

    #- 1. 전체평균을 구하기 위해, 이중포문으로 Null 이 아닐때만 읽고 그 수를 카운트해서, 전체 평균을 구했다 ( mean_all)
    #- 2. bvi 는 분자에 들어가는 변수로, 식을 정리하면 " user v의 평균 + 아이템의 평균 - 전체평균" 이라서 이를 정의하고 후에 reshape 해줌
    # - 3. bui 부분도 식을 정리하면, "user u 의 평균 + 아이템의 평균 - 전체평균" 이라서 이를 넣어주었다.
    def baseline(self,rating_file,sim,k):
        mat = np.load(rating_file)
        mat[np.isnan(mat)] = 0.0           
        predicted_rating = np.array([[0.0 for col in range(21601)] for row in range(380)])


        def COS(mat):
            # 행 개수 
            NumUsers = np.size(mat,axis=0)
            # 초기화
            Sim = np.full((NumUsers,NumUsers),0.0)
            for u in range(NumUsers):
                # 한 row 씩 보면서 0인 index 찾아
                arridx_u = np.where(mat[u,]==0)
                #print("arridx_u {} = {}\n".format(u, arridx_u))
                for v in range(u+1,NumUsers):
                    arridx_v = np.where(mat[v,]==0)
                    #print("arridx_v {} = {}\n".format(v, arridx_v))
                    arridx = np.unique(np.concatenate((arridx_u,arridx_v),axis=None))
                    #print("arridx {} = {}\n".format(v, arridx))

                    U = np.delete(mat[u,],arridx)
                    V = np.delete(mat[v,],arridx)

                    if (np.linalg.norm(U)==0 or np.linalg.norm(V)==0):
                        Sim[u,v] = 0
                    else:
                        Sim[u,v] = np.dot(U,V)/(np.linalg.norm(U)*np.linalg.norm(V))
                    Sim[v,u] = Sim[u,v]

            #print(arridx)

            return Sim        

        def PCC(mat):
            NumUsers = np.size(mat,axis=0)
            Sim = np.full((NumUsers,NumUsers),-1.0)

            mean = np.nanmean(np.where(mat!=0.0,mat,np.nan),axis=1)

            for u in range(NumUsers):
                arridx_u = np.where(mat[u,]==0)
                for v in range(u+1, NumUsers):
                    arridx_v = np.where(mat[v,]==0)
                    arridx = np.unique(np.concatenate((arridx_u,arridx_v),axis=None))

                    U = np.delete(mat[u,],arridx) - mean[u]
                    V = np.delete(mat[v,],arridx) - mean[v]

                    if (np.linalg.norm(U)==0 or np.linalg.norm(V)==0):
                        Sim[u,v] = 0
                    else:
                        Sim[u,v] = np.dot(U,V)/(np.linalg.norm(U)*np.linalg.norm(V))

                    Sim[v,u] = Sim[u,v]

                return Sim            
        
        mean = np.nanmean(np.where(mat!=0,mat,np.nan),axis=1)
        mean_i = np.nanmean(np.where(mat!=0,mat,np.nan),axis=0)
        if (sim == 'COS'):
            Sim = COS(mat)
        elif (sim == "PCC"):
            Sim = PCC(mat)

        # 전체 평균
        all_sum = 0
        cnt = 0
        for i in range(380):
            for j in range(21601):
                if mat[i][j] >0 :
                    all_sum += mat[i][j]
                    cnt += 1
                    #print(mat[i][j])
                else: 
                    continue

        mean_all = all_sum/cnt 


        k_neighbors = np.argsort(-Sim)
        k_neighbors = np.delete(k_neighbors,np.s_[k:],1)

        NumUsers = np.size(mat,axis=0)


        for u in range(NumUsers):
            list_sim = Sim[u,k_neighbors[u,]]
            list_rating = mat[k_neighbors[u,],].astype('float64')
            list_mean = mean[k_neighbors[u,],]

            denominator = np.sum(list_sim)
            bvi = list_mean + mean_i[u] -mean_all
            numerator = np.sum(list_sim.reshape(-1,1)*(list_rating - bvi.reshape(-1,1)),axis=0)
            predicted_rating[u,] = mean[u]+mean_i[u]-mean_all + numerator/denominator        

        return predicted_rating 