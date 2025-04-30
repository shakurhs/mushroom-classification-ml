# Survival Guide: "Is this Shroom Edible?"

## Repository Outline

Penjelasan Mengenai Isi dari Tiap File dan Folder:

1. best_rf_model.pkl - Model ML tebaik yang digunakan untuk Data Inference
2. P1M2_hafizal_shakur.ipynb - Notebook yang berisi pengolahan data dengan python dimulai dari loading dataset hingga evaluasi model ML
3. P1M2_hafizal_shakur_inf.ipynb - Notebook Data Inference yang berisi kegiatan mulai dari loading model hingga melakukan prediksi
4. secondary_data.csv - File bersumber dari website yang akan digunakan sebagai dataset untuk proyek membuat ML
5. url.txt - File yang berisikan url Dataset dan url Deployment
6. description.md - File Markdown yang berisi tentang gambaran mengenai proyek Machine Learning
6. Deployment - Folder yang berisikan file terkait untuk melakukan deployment ke HuggingFace


## Problem Background

Model Machine Learning yang saya buat digunakan sebagai pedoman untuk menentukan sebuah spesies jamur yang layak dikonsumsi sebagai subtitusi makanan dan yang tidak. Bagi para penjelajah alam atau petualang yang memiliki jam terbang yang tinggi tentu saja memiliki keilmuan tentang alam yang luas. Mereka memiliki kapabilitas dalam mencari makanan di alam liar dalam keadaan terdesak. Seperti yang kita tahu, tidak semua kalangan memiliki pengalaman kehabisan makanan dalam keadaan terdesak. Sangat disayangkan apabila seseorang yang sedang berusaha bertahan hidup bernasib naas ketika mengonsumsi hasil alam yang tidak tepat. Akibat mengonsumsi asupan yang salah, gejala keracunan akan muncul mulai dari yang ringan seperti mual, pusing, muntah. Hingga gejala paling parah menyebabkan kelumpuhan atau meregang nyawa. Dengan begitu, diharapkan model Machine Learning ini digunakan sebaik mungkin untuk menghindari kejadian-kejadian yang tidak diinginkan ketika salah mengonsumsi jamur.

## Project Output

Produk yang dihasilkan dari proyek ini adalah sebuah model Machine Learning yang ditampilkan menggunakan Python basic web app (streamlit) sebagai user interface.

## Data

Dataset yang saya dapatkan berasal dari website UC Irvine Machine Learning Repository, dimana data tersebut berisikan tentang spesifikasi dan atribut pada sebuah spesies jamur. Data terdiri atas 61069 baris dan 21 kolom. Pada saat dimuat ke dalam data frame, terlihat dataset memiliki missing value yang banyak. Bahkan untuk kasus dimana jumlah missing value mencapai lebih dari 80% pada sebuah kolom, akhirnya saya memutuskan untuk drop kolom-kolom tersebut. Selebihnya missing value saya handle menggunakan SimpleImputer.

## Method

Proyek ini adalah sebuah proyek mengenai Supervised Machine Learning Classification Problem untuk menentukan pembagian kelas dari spesies jamur. Model yang digunakan dalam proyek ini adalah Random Forest Classification yang telah melalui proses Hyperparameter Tuning. Model Random Forest dipilih berdasarkan performa model terbaik dari model lain seperti Super Vector Machine, K-Nearest Neighbors, Decision Tree, dan AdaBoost. Kelimamodel tersebut dilakukan pengujian menggunakan Cross Validation untuk menghasilkan nilai Recall terbaik.

## Stacks

1. Programming Language : Python
2. Tools                : Visual Studio Code, HuggingFace, GitHub
3. Library              : pandas, numpy, scipy, seaborn, matplotlib, scikit-learn, feature_engine, phik, pickle, streamlit,plotly, pillow

## Reference

URL Dataset   : https://archive.ics.uci.edu/dataset/848/secondary+mushroom+dataset
URL Deployment: https://huggingface.co/spaces/shakurhs/Predict_Edible_Mushroom

---