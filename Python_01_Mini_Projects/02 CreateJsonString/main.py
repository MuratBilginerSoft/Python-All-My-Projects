a = """{'storage_path': 'cantufekci/test_16_09', 'id': '3513', 'data_name': 'eren_urunref_seg_v14721.parquet', 'model_job': 'segmentation', 'model_names': 'kmeans', 'num_cols': 'KumSatisAdet_Guncel,SevkSTR_Guncel,SLSR_TL_Guncel,Satis_Ilk_Son_Guncel,SonSatis_Bugun,Karlilik_Guncel,KumSatisAdet_Eski,SevkSTR_Eski,SLSR_TL_Eski,Satis_Ilk_Son_Eski,Karlilik_Eski,SiparisAdet,SatisSapmasi_Guncel,SatisSapmasi_Eski,SezonSayisi,MerkezStokAdet', 'cat_cols': '', 'target_col': '', 'id_cols': '', 'drop_duplicates': 'True', 'eliminate_outlier': 'True', 'dim_red': 'True', 'penetrate_col': 'MerkezStokAdet'}

"""

b = a.replace("'",'"')

print(b)