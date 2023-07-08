import math 
import csv
import numbers
from numpy._typing import _CharLike_co
from numpy.core.umath import empty
from pandas.io import excel
import streamlit as st


import numpy as np 
import pandas as pd
st.markdown("""
<style>
.css-1a1tcp.e1ewe7hr3{
  visibility: hidden;
}
.css-h5rgaw.e1g8pov61{
  visibility: hidden;
   
            </style>         
""", unsafe_allow_html=True)

mahm=st.header(" بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
mahoud=st.header("صلي ع الرسول")
mahmo=st.subheader("بند الجسات")
N_GASAT,D_gasa,Cost_gasa=st.columns(3)
n_GASAT=N_GASAT.number_input("عدد الجسات", -10000)
d_gasa=D_gasa.number_input("عمق الجسة(M)",-10000)
cost_gasa=Cost_gasa.number_input("تكلفة متر الجسة الواحد",-10000)
a=st.button("تكلفة الجسات")
if a:
      st.latex(d_gasa*n_GASAT*cost_gasa)
st.subheader("بند الحفر")
N_ASAT,D_g,Cst_gas,uu=st.columns(4)
A_L=N_ASAT.number_input("مساحة الحفر",-10000)
D_7fr=D_g.number_input("عمق الحفر",-10000)
V_C=Cst_gas.number_input("سعة الناقلة",-10000)
COST_ONE_TANK=uu.number_input("تكلفة النقلة الواحدة",-10000)
NSAT,Dlg,Cstas,moon,tnzi=st.columns(5)
NTFASH=NSAT.number_input("معامل الانتفاش",-10000 )
ENTAG_EL7FAR=Dlg.number_input("انتاجية الحفار لليوم",-10000)
COST_7FAR=Cstas.number_input("تكلفة الحفار لليوم",-10000)
nnnnnn=moon.number_input("عدد مسطحات الحفر",-10000)
tttnzil=tnzi.number_input("الاضافات بالموجب ولو تنزيلات",-10000)
Q_7fr=((A_L*D_7fr*NTFASH))
n1nonon=(nnnnnn*Q_7fr)
N_TANK=(Q_7fr/V_C)
n2nonon=(nnnnnn*N_TANK)
COST_TANK=(N_TANK*COST_ONE_TANK)
n3nonon=(nnnnnn*COST_TANK)
COST_EL7FAR=((Q_7fr/ENTAG_EL7FAR)*COST_7FAR)
n4nonon=(nnnnnn*COST_EL7FAR)
CO_7FR=(COST_EL7FAR + COST_TANK)
n5nonon=(nnnnnn*CO_7FR)
qtanzil=(Q_7fr+tttnzil)
n1nonontnz=(nnnnnn*qtanzil)
COST_EL7FARtaz=((qtanzil/ENTAG_EL7FAR)*COST_7FAR)
n4nonontnz=(nnnnnn*COST_EL7FARtaz)
N_TANKtan=(qtanzil/V_C)
n2nonontnz=(nnnnnn*N_TANKtan)
COST_TANKtnz=(N_TANKtan*COST_ONE_TANK)
n3nonontnz=(nnnnnn*COST_TANKtnz)
CO_7FRtnz=(COST_EL7FARtaz + COST_TANKtnz)
n5nonontnz=(nnnnnn*CO_7FRtnz)
df= pd.DataFrame({
        "ملاحظات":["","","","","",""],
        "بعد التنزيلات":["--",n1nonontnz,"--","--","--","--"],
        "التنزيلات":["--",tttnzil,"--","--","--","--"],       
        "اجمالي المسطح":["--",n1nonon,"--","--","--","--"],
        "الارتفاع":["--",D_7fr,"--","--","--","--"],
        "المساحة":["--",A_L,"--","--","--","--"],
        "عدد": ["--",nnnnnn,"--","--","--","--"],
        "وحدة القياس": ["متر مكعب","متر مكعب","--","--","--","--"],
        "الأعمال": ["الحفر","مسطح الحفر","--","--","--","--"],
        "رقم البند": ["1","--","--","--","--","--"]})
o=st.button("الحصر الكمي المبدأي")
if o:
     st.data_editor(df)
df3= pd.DataFrame({
       "التكلفة الكلية":[CO_7FRtnz,],
       "تكلفة النقل":[COST_TANKtnz,],
       "عدد النقلات": [N_TANKtan],
       "تكلفة الحفار": [COST_EL7FARtaz],
       "كمية الحفر": [qtanzil],
       "بند الحفر  ": ["بعد التنزيلات"]})
b=st.button("جدول التفاصيل")
if b:
      st.data_editor(df3)

st.subheader("بند الخرسانة العادية اسفل الاساسات")
asAT,D_gmk,Coit_gas=st.columns(3)
a_1a=asAT.number_input("مساحة الأرض(M²)", -10000)
a_2a=D_gmk.number_input("سمك الخرسانة العادية(M)",-10000)
a_a=Coit_gas.number_input("المحتوى الأسمنتي ل 1 متر مكعب(kgm)",-10000)
asomAT,D_gomk,hh=st.columns(3)  
a_na=asomAT.number_input("نسبة الماء من محتوى الأسمنت",-10000)
dddd=D_gomk.number_input("نسبة الاضافات من محتوى الاسمنت",-10000)
ddd=hh.number_input("تكلفة الاضافات ل 1متر مكعب خرسانة ",-10000)
Coiit_gas,asopmAT,D_pgomk,Copiit_gas=st.columns(4)
ddtd=Coiit_gas.number_input("تكلفة متر مكعب رمل",-10000)
dtdd=asopmAT.number_input("تكلفة متر مكعب سن",-10000)
dgdd=D_pgomk.number_input("تكلفة طن الأسمنت",-10000)
fff=Copiit_gas.number_input("تكلفة لتر الماء",-10000)
Copiiit_gas,coiii=st.columns(2)
fffnn=Copiiit_gas.number_input("عدد الاعمال",-10000)
tnziloo=coiii.number_input("كمية التنزيلات(M³)",-10000)
qua1_n_c=(a_1a*(a_2a))
tnzilqo=(qua1_n_c - tnziloo)
qua_sn=(qua1_n_c*0.8+(qua1_n_c*0.8*.05))
tnzilaa=(tnzilqo*0.8+(qua1_n_c*0.8*.05))
qua_rml=(qua1_n_c*0.48+(qua1_n_c*0.4*0.1))
tzilrm=(tnzilqo*0.48+(qua1_n_c*0.4*0.1))
qua_asmnt=((qua1_n_c*a_a)/1000)
tnzilas=((tnzilqo*a_a)/1000)
one_m_c=(a_na*qua1_n_c)
tnziloma=(tnzilqo*a_na)
qua_wa=(ddtd*qua_rml)
quarmltnzi=(ddtd*tzilrm)
aeda=(dddd*tnzilqo*a_a)
jjk=(qua_sn*dtdd)
tziljjk=(tnzilaa*dtdd)
asmnto=(dgdd*qua_asmnt)
asmtzilo=(dgdd*tnzilas)
watro=(one_m_c*fff)
wartotzilo=(fff*tnziloma)
dddco=(ddd*qua1_n_c)
dddcotnz=(ddd*tnzilqo)
coooo=(qua_wa+jjk+dddco+qua_wa+asmnto)
cooootnzilo=(dddcotnz+tziljjk+dddcotnz+quarmltnzi+asmtzilo)
df2= pd.DataFrame({
       "ملاحظات":["","","","","",""],
       "بعد التنزيلات":[0,tnzilqo,0,0,0,0],
       "التنزيلات":["--",tnziloo,0,0,0,0],       
       "اجمالي المسطح":["--",qua1_n_c,0,0,0,0],
       "الارتفاع":["--",a_2a,0,0,0,0],
       "المساحة":["--",a_1a,0,0,0,0],
       "عدد": ["--",fffnn,0,0,0,0],
       "وحدة القياس": ["متر مكعب","متر مكعب","--","--","--","--"],
       "الأعمال": ["الحفر","مسطح الحفر","--","--","--","--"],
       "رقم البند": [0,0,0,0,0,0]})
y=st.button("الحصر  الكمي المبدأي")
if y:
      st.data_editor(df2)

df4= pd.DataFrame({
       "الخرسانة(M³)":[tnzilqo,cooootnzilo],
       "الاضافات(M³)":[aeda,dddcotnz],
       "الماء(L)": [tzilrm,wartotzilo],
       "الاسمنت(tan)": [tnzilas,asmtzilo],
       "السن(M³)": [tnzilaa,n1nonontnz],
       " الرمل(M³)": [tzilrm,quarmltnzi],
       " بند الخرسانة العادية اسفل الاساسات": ["الكمية","(التكلفة)"]})

b=st.button("جدول  التفاصيل")
if b:
      st.data_editor(df4)
   
   

    

