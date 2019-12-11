import numpy as np
import pandas as pd
from surprise import SVD
from surprise import Dataset
from surprise import Reader
from surprise.model_selection import cross_validate
from surprise import KNNBasic
from surprise import KNNWithMeans
from surprise import KNNWithZScore
from surprise import SVD
from surprise import SVDpp
from surprise.accuracy import rmse
from surprise import accuracy
from surprise.model_selection import train_test_split
from surprise.model_selection import KFold
from collections import defaultdict



class cal_surprise(object):
    def load(self,review_file,save_file1,algorithm,save_file2):
        df = pd.read_csv(review_file)
        print("df shape : {}".format(df.shape))
        
        # surprise load 
        reader = Reader(rating_scale=(0,5))
        data = Dataset.load_from_df(df[['user','store','stars']],reader)        
        
        trainset = data.build_full_trainset()

        algo = SVD()
        cross_validate(algo, data, measures=['RMSE','MAE'],cv=5,verbose=True)
        
        #Algorithm 별 비교

        for_df = []
        for algo in [KNNBasic(),KNNWithMeans(),KNNWithZScore(),SVD()]:
            results = cross_validate(algo,data,measures=['RMSE','MAE'],cv=5,verbose=True)

            tmp = pd.DataFrame.from_dict(results).mean(axis=0)
            #print(tmp)
            tmp = tmp.append(pd.Series([str(algo).split(' ')[0].split('.')[-1]],index=['algorithm']))
            for_df.append(tmp)
        vs = pd.DataFrame(for_df).set_index('algorithm') 
        vs.to_csv(save_file1)


        
        def cal_SVD(trainset,df):
            algo_svd = SVD(n_factors=100,n_epochs=20,biased=False,lr_all=0.005,reg_all=0)
            algo_svd.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)   
            print("end")
            df2 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df2['user'] = users
            df2['item'] = items
            df2['r_ui'] =real
            df2['est'] = estimate
            df2['est'] = df2['est'].apply(lambda x: x[-2]) 
            df2['err'] = abs(df2.est - df2.r_ui) 
            df2.to_csv(save_file2)
        
        
        def cal_KNNBasic(trainset,df):
            # KNNBasic

            sim_options = {'name':'cosine','user-based':True}
            algo_knnb = KNNBasic(k=40, min_k=1, sim_options=sim_options)
            algo_knnb.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)
            print("end")            
            # knn basic
            df3 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df3['user'] = users
            df3['item'] = items
            df3['r_ui'] =real
            df3['est'] = estimate
            #df3.head()
            df3['est'] = df3['est'].apply(lambda x: x[-2])
            df3['err'] = abs(df3.est - df3.r_ui)            
            df3.to_csv(save_file2)
            
        def cal_KNNWithMeans(trainset,df):
            # KNNWithMeans

            sim_options = {'name':'cosine','user-based':True}
            algo_knnm = KNNWithMeans(k=40, min_k=1, sim_options=sim_options)
            algo_knnm.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)
            print("end")      
            # knn With Means
            df4 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df4['user'] = users
            df4['item'] = items
            df4['r_ui'] =real
            df4['est'] = estimate
            #df3.head()
            df4['est'] = df4['est'].apply(lambda x: x[-2])
            df4['err'] = abs(df4.est - df4.r_ui)            
            df4.to_csv(save_file2)
            
        def cal_KNNWithZScore(trainset,df):
            # KNN With ZScore

            sim_options = {'name':'cosine','user-based':True}
            algo_knnz = KNNWithZScore(k=40, min_k=1, sim_options=sim_options)
            algo_knnz.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)
            print("end")
            # knn With Means
            df5 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df5['user'] = users
            df5['item'] = items
            df5['r_ui'] =real
            df5['est'] = estimate
            #df3.head()
            df5['est'] = df5['est'].apply(lambda x: x[-2])
            df5['err'] = abs(df5.est - df5.r_ui)
            df5.to_csv(save_file2)
            
        def cal_PMF(trainset,df):
            # pmf
            algo_pmf = SVD(n_factors=100,n_epochs=20,biased=False,lr_all=0.005,reg_all=0.02)
            algo_pmf.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)            
            print("end")                    
            # PMF
            df6 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df6['user'] = users
            df6['item'] = items
            df6['r_ui'] =real
            df6['est'] = estimate
            #df3.head()
            df6['est'] = df6['est'].apply(lambda x: x[-2])
            df6['err'] = abs(df6.est - df6.r_ui)
            df6.to_csv(save_file2)      
            
        def cal_PMFwithbiased(trainset,df):
            # pmf with biased
            algo_pmfb = SVD(n_factors=100,n_epochs=20,biased=True,lr_all=0.005,reg_all=0.02)
            # bias = True 로 바꿔
            algo_pmfb.fit(trainset)
            users = []
            items = []
            real = []
            estimate = []
            for i in range(len(df)):
                uid = df[i:i+1].user.values[0]
                users.append(uid)
                iid = df[i:i+1].store.values[0]
                items.append(iid)
                r_ui = df[i:i+1].stars.values[0]
                real.append(r_ui)
                pred = algo.predict(uid,iid,r_ui,verbose=True)
                estimate.append(pred)
            print("end") 
            # PMF with biased
            df7 =pd.DataFrame(columns=['user','item','r_ui','est'])
            df7['user'] = users
            df7['item'] = items
            df7['r_ui'] =real
            df7['est'] = estimate
            #df3.head()
            df7['est'] = df7['est'].apply(lambda x: x[-2])
            df7['err'] = abs(df7.est - df7.r_ui) 
            df7.to_csv(save_file2)             
            
        if (algorithm == 'SVD'):
            cal_SVD(trainset,df)
        elif (algorithm == "KNNBasic"):
            cal_KNNBasic(trainset,df)            
        elif (algorithm == "KNNWithZScore"):
            cal_KNNWithZScore(trainset,df)        
        elif (algorithm == "KNNWithMeans"):
            cal_KNNWithMeans(trainset,df)      
        elif (algorithm == "PMF"):
            cal_PMF(trainset,df)   
        elif (algorithm == "PMFwithbiased"):
            cal_PMFwithbiased(trainset,df)      
            
    def evaluation(self,review_file):
        df = pd.read_csv(review_file)
        print("df shape : {}".format(df.shape))        
        # surprise load 
        reader = Reader(rating_scale=(0,5))
        data = Dataset.load_from_df(df[['user','store','stars']],reader)        
        for_df = []
        for algo in [KNNBasic(),KNNWithMeans(),KNNWithZScore(),SVD()]:
            results = cross_validate(algo,data,measures=['RMSE','MAE'],cv=5,verbose=True)

            tmp = pd.DataFrame.from_dict(results).mean(axis=0)
            #print(tmp)
            tmp = tmp.append(pd.Series([str(algo).split(' ')[0].split('.')[-1]],index=['algorithm']))
            for_df.append(tmp)
        pd.DataFrame(for_df).set_index('algorithm') 
        #precision_recall_at_k 함수

        def precision_recall_at_k(predictions, k=10, threshold=3.5):


            # 각 user에서 prediction mapping
            # default dic = dictionary의 기본값 정의, 값없어도 에러 없이 출력
            user_est_true = defaultdict(list)
            for uid, _, true_r, est, _ in predictions:
                user_est_true[uid].append((est, true_r))

            precisions = dict()
            recalls = dict()
            for uid, user_ratings in user_est_true.items():

                # estimated value로 sort 내림차순
                user_ratings.sort(key=lambda x: x[0], reverse=True)

                # Revlevant 
                n_rel = sum((true_r >= threshold) for (_, true_r) in user_ratings)

                # k까지 추천된 아이템
                n_rec_k = sum((est >= threshold) for (est, _) in user_ratings[:k])

                # relevant and recommended items in top k
                n_rel_and_rec_k = sum(((true_r >= threshold) and (est >= threshold))
                                      for (est, true_r) in user_ratings[:k])

                # Precision@K
                precisions[uid] = n_rel_and_rec_k / n_rec_k if n_rec_k != 0 else 1

                # Recall@K:
                recalls[uid] = n_rel_and_rec_k / n_rel if n_rel != 0 else 1

            return precisions, recalls     
        # kfold import 위에서 함
        kf = KFold(n_splits=5)
        for algo in [KNNBasic(),KNNWithMeans(),KNNWithZScore(),SVD()]:
            algoname = str(algo).split(' ')[0].split('.')[-1]
            for trainset , testset in kf.split(data):
                algo.fit(trainset)
                predictions = algo.test(testset)
                precisions, recalls = precision_recall_at_k(predictions, k=5, threshold=3)

                P = sum(prec for prec in precisions.values()) / len(precisions)
                R = sum(rec for rec in recalls.values()) / len(recalls)
                F1 = 2*P*R/(P+R)

                print("algo : {}\n precision : {} recall: {} F1 : {}".format(algoname,P,R,F1))
            print("\n\n")        