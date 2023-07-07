# -*- coding: utf-8 -*-
"""
Spyder Editor

This is a temporary script file.
"""


#tringle_high=float(input("h: "))
#tringle_base=float(input("b: "))
#tringle_area=(0.5*tringle_high*tringle_base)
#print("area.:" , tringle_area)

#x=float(input("enter x: "))
#x_sequre=(x**2)
#print(x_sequre)
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
}      
.stException{
  visibility: hidden;
}            
            </style>
""", unsafe_allow_html=True)

mahm=st.header(" بِسْمِ اللَّهِ الرَّحْمَٰنِ الرَّحِيمِ")
st.markdown("""
<style>
.css-1a1tcp.e1ewe7hr3{
  visibility: hidden;
}
.css-h5rgaw.e1g8pov61{
  visibility: hidden;
}       
            </style>
""", unsafe_allow_html=True)
op=st.selectbox("حصر ",["الجسات","الخوازيق","الحفر", "الخرسانة العادية(فرشة بكامل مسطح الموقع)",
                        "الخرسانة العادية(حول القواعد المسلحة واسفل السملات(الشدات))"])
if op == "الجسات":
    N_GASAT,D_gasa,Cost_gasa=st.columns(3)
    n_GASAT=N_GASAT.number_input("عدد الجسات")
    d_gasa=D_gasa.number_input("عمق الجسة(M)")
    cost_gasa=Cost_gasa.number_input("تكلفة متر الجسة الواحد",  )
    a=st.button("تكلفة الجسات")
    if a:
      st.latex(d_gasa*n_GASAT*cost_gasa)
elif op == "الخوازيق":
    k_GASAT,b_gasa,nost_gasa,nn=st.columns(4)
    N_Khazok=k_GASAT.number_input("عدد الخوازيق")
    L_Khazok=b_gasa.number_input("طول الخازوق الواحد (M)")
    D_Khazok=nost_gasa.number_input("قطر الخازوق الواحد (M) ")
    Cost_m3_c=nn.number_input("تكلفة واحد متر مكعب خرسانة")
    s_GASAT,s_gasa,sost_gasa,snn=st.columns(4)
    N_S_R_Qfs_Tslih_khazok=s_GASAT.number_input("عدد اسياخ حديد التسليح الرئيسي")
    D_R_R_Qfs_Tslih_khazok=s_gasa.number_input("قطر سيخ التسليح الرئيسي (Mm) ")
    D_Canat_7alzonia=sost_gasa.number_input("قطر الكانة الحلزونية(Mm)")
    Khatoa_Canat_7alzonia=snn.number_input("خطوة(التقسيط)للكانات (M)")
    ms_GASAT,ms_gasa,msost_gasa,msnn=st.columns(4)
    D_Atoak_daklia=ms_GASAT.number_input("قطر 1 من الأطواق الداخلية(Mm)")
    Khatoa_Atoak=ms_gasa.number_input("خطوة (التقسيط) للأطواق (M)")
    GHta_KHRSANY=msost_gasa.number_input("الغطاء الخرساني(M)")
    Cost_tan_s=msnn.number_input("تكلفة واحد طن حديد")
    ms_GASA,ms_gas=st.columns(2)
    halk_c=ms_GASA.number_input("نسبة الهالك من الخرسانة")
    halk_s=ms_gas.number_input("نسبة الهالك من الحديد")
    qua_b=((D_Khazok**2)*L_Khazok*math.pi*.25)
    qua_c=((D_Khazok**2)*L_Khazok*math.pi*.25*N_Khazok)
    co_d=(Cost_m3_c*qua_b)
    co_f=(Cost_m3_c*qua_c)
    Quantity_S_R=(N_S_R_Qfs_Tslih_khazok*(D_R_R_Qfs_Tslih_khazok**2)*L_Khazok/162)
    Quantity_S_R_all=(Quantity_S_R*N_Khazok)
    tan_r=(Quantity_S_R_all/1000)
    Quantity_canat_7alzonia=((D_Khazok - (GHta_KHRSANY*2))*math.pi*(L_Khazok - 1.5)/(Khatoa_Canat_7alzonia)*(D_Canat_7alzonia**2)/162)
    Quantity_canat_7alzonia_all=(Quantity_canat_7alzonia*N_Khazok)
    tan_c=(Quantity_canat_7alzonia_all/1000)
    di=((D_Khazok - (2*GHta_KHRSANY))-((D_Canat_7alzonia/1000) + (D_Canat_7alzonia/1000) + (D_R_R_Qfs_Tslih_khazok/1000) + (D_R_R_Qfs_Tslih_khazok/1000)))
    Quantity_S_Atoak=((L_Khazok/Khatoa_Atoak)*((math.pi*di) + .1)*(D_Atoak_daklia**2)/162)
    Quantity_S_Atoak_all=(Quantity_S_Atoak*N_Khazok)
    tan_a=(Quantity_S_Atoak_all/1000)
    Quantity_s_one=((Quantity_canat_7alzonia + Quantity_S_R + Quantity_S_Atoak)/1000 )
    Quantity_all_tan=(tan_a + tan_c + tan_r)
    cost_one=(Cost_tan_s*Quantity_s_one)
    cost_all=(Quantity_all_tan*Cost_tan_s)
    af_ha_c=( qua_c+(qua_c*halk_c))
    co_hs=(af_ha_c*Cost_m3_c)
    onek_ha=(qua_b+(qua_b*halk_c))
    q_af_ha_s_k=((halk_s*tan_r)+tan_r)
    q_af_ha_s_c=((halk_s*tan_c)+tan_c)
    af_ha_s_a=((halk_s*tan_a)+tan_a)
    af_h_a_s=((Quantity_all_tan)+(Quantity_all_tan*halk_s))
    Quantity_S_R_h=((Quantity_S_R)+(Quantity_S_R*halk_s))
    Quantity_canat_7alzonia_h=((Quantity_canat_7alzonia)+(Quantity_canat_7alzonia*halk_s))
    cost_all_h=(af_h_a_s*Cost_tan_s)
    c_onek_ha=(onek_ha*Cost_m3_c)
    af_h_one_k=(Quantity_s_one+(Quantity_s_one*halk_s))
    co_af_h_o_k=(af_h_one_k*Cost_tan_s)
    sum_co=(co_f+cost_all)
    sumcoh=(co_hs+cost_all_h)
    cooh=(cost_one+co_d)
    coho=(co_af_h_o_k+c_onek_ha)
    S_GsASAT,s_gsasa,snost_sgasa,mnn=st.columns(4)
    op=st.radio("select",["خرسانة الخوازيق(M³)","حديد الخوازيق(tan)",
                      "التكلفة الكلية للخوازيق(حديد+خرسانة)","كمية الخرسانة لخازوق واحد","كمية الحديد لخازوق واحد"])
    if op == "خرسانة الخوازيق(M³)":
        st.write("الكمية بدون نسبة هالك", qua_c)
        st.write("التكلفة", co_f)
        st.write("بإضافة نسبة هالك", af_ha_c )
        st.write("التكلفة", co_hs)
    elif op == "حديد الخوازيق(tan)":
        abbs=st.button("بدون نسبة هالك(tan)")
        if abbs:
          st.write("التسليح الرئيسي", tan_r, "قطر", D_R_R_Qfs_Tslih_khazok)
          st.write("الكانات الحلزونية للخوازيق ", tan_c, "قطر", D_Canat_7alzonia)
          st.write("حديد الاطواق الداخلية", tan_a, "قطر",  D_Atoak_daklia)
          st.write("كل حديد الخوازيق", Quantity_all_tan)
          st.write("التكلفة", cost_all)
        abbn=st.button("بإضافة نسبة هالك(tan)")
        if abbn:
           st.write("الكانات الحلزونية للخوازيق ", q_af_ha_s_c, "قطر", D_Canat_7alzonia)
           st.write("التسليح الرئيسي ", q_af_ha_s_k, "قطر", D_R_R_Qfs_Tslih_khazok)
           st.write("كمية حديد الاطواق الداخلية للخوايق", af_ha_s_a, "قطر",  D_Atoak_daklia)
           st.write("كمية كل حديد الخوازيق", af_h_a_s)
           st.write("التكلفة", cost_all_h)
    elif op=="التكلفة الكلية للخوازيق(حديد+خرسانة)":
      st.write("بدون نسبة هالك",sum_co)
      st.write("بإضافة نسبة هالك",sumcoh)
    elif op== "الخرسانة لخازوق واحد(M³)":
      st.write("بدون نسبة هالك", qua_b)
      st.write("التكلفة",co_d) 
      st.write(" بإضافة نسبة هالك", onek_ha)
      st.write("التكلفة",c_onek_ha)
    elif op== "الحديد لخازوق واحد":
      st.write("كل الحديد بدون نسبة هالك (tan)", Quantity_s_one)
      st.write("التكلفة", cost_one)
      st.write("كل الحديد بإضافة نسبة هالك(tan)", af_h_one_k)
      st.write("التكلفة", co_af_h_o_k)
      st.write("التسليح الرئيسي(kgm)",Quantity_S_R, "قطر",  D_R_R_Qfs_Tslih_khazok )
      st.write("الأطواق(kgm)", Quantity_S_Atoak, "قطر", D_Atoak_daklia)
      st.write("الكانات الحلزونية(kgm)", Quantity_canat_7alzonia, "قطر", D_Canat_7alzonia)
      st.write("طول السيخ لعمل الكانات للخازوق", (D_Khazok - (GHta_KHRSANY*2))*math.pi*(L_Khazok - 1.5)/(Khatoa_Canat_7alzonia),)
      st.write("طول السيخ لعمل لفه(كانة) حلزونية واحده", (D_Khazok - (GHta_KHRSANY*2))*math.pi, )
      st.write("عدد الحلقات(الكانات)اللازمة لتحيط بالخازوق ", (L_Khazok - 1.5)/(Khatoa_Canat_7alzonia), )
    elif op==("التكلفة الكلية لخازوق واحد(حديد+خرسانة)"):
       st.write("بدون نسبة هالك",cooh)
       st.write("بإضافة نسبة هالك",coho)
elif op == "الحفر":
  N_ASAT,D_g,Cst_gas,uu=st.columns(4)
  A_L=N_ASAT.number_input("مساحة الحفر")
  D_7fr=D_g.number_input("عمق الحفر")
  V_C=Cst_gas.number_input("سعة الناقلة")
  COST_ONE_TANK=uu.number_input("تكلفة النقلة الواحدة")
  NSAT,Dlg,Cstas=st.columns(3)
  NTFASH=NSAT.number_input("معامل الانتفاش" )
  ENTAG_EL7FAR=Dlg.number_input("انتاجية الحفار في اليوم")
  COST_7FAR=Cstas.number_input("تكلفةالحفار باليوم")
  Q_7fr=(A_L*D_7fr*NTFASH)
  N_TANK=(Q_7fr/V_C)
  COST_TANK=(N_TANK*COST_ONE_TANK)
  COST_EL7FAR=((Q_7fr/ENTAG_EL7FAR)*COST_7FAR)
  CO_7FR=(COST_EL7FAR + COST_TANK)
  st.write("كمية الحفر", Q_7fr)
  st.write("تكلفة الحفار", COST_EL7FAR )
  st.write("عدد النقلات", N_TANK)
  st.write("تكلفة النقل", COST_TANK)
  st.write("تكلفة الحفر",CO_7FR )
elif op == "الخرسانة العادية(فرشة بكامل مسطح الموقع)":
  asAT,D_gmk,Coit_gas=st.columns(3)
  a_1a=asAT.number_input("مساحة الأرض(M²)")
  a_2a=D_gmk.number_input("سمك الخرسانة العادية(CM)")
  a_a=Coit_gas.number_input("المحتوى الأسمنتي ل 1 متر مكعب(kgm)")
  asomAT,D_gomk,hh=st.columns(3)  
  a_na=asomAT.number_input("نسبة الماء من محتوى الأسمنت")
  dddd=D_gomk.number_input("نسبة الاضافات من محتوى الاسمنت")
  ddd=hh.number_input("تكلفة الاضافات ل 1متر مكعب خرسانة ")
  Coiit_gas,asopmAT,D_pgomk,Copiit_gas=st.columns(4)
  ddtd=Coiit_gas.number_input("تكلفة متر مكعب رمل")
  dtdd=asopmAT.number_input("تكلفة متر مكعب سن")
  dgdd=D_pgomk.number_input("تكلفة طن الأسمنت")
  fff=Copiit_gas.number_input("تكلفة لتر الماء")
  qua1_n_c=(a_1a*(a_2a/100))
  qua_sn=(qua1_n_c*0.8+(qua1_n_c*0.8*.05))
  qua_rml=(qua1_n_c*0.48+(qua1_n_c*0.4*0.1))
  qua_asmnt=((qua1_n_c*a_a)/1000)
  one_m_c=(a_na*qua1_n_c)
  qua_wa=(ddtd*qua_rml)
  jjk=(qua_sn*dtdd)
  asmnto=(dgdd*qua_asmnt)
  watro=(one_m_c*fff)
  dddco=(ddd*qua1_n_c)
  coooo=(qua_wa+jjk+dddco+qua_wa+asmnto)
  op=st.radio("select",["خرسانة","الرمل","السن","الأسمنت","الماء"])
  if op=="خرسانة":
    st.write("كمية الخرسانة(M³)", qua1_n_c)
    st.write("التكلفة",coooo )
  elif op=="الرمل":
    st.write("كمية الرمل(M³)", qua_rml)
    st.write("التكلفة",qua_wa )
  elif op=="السن":
    st.write("كمية السن(M³)", qua_sn )
    st.write("التكلفة",jjk )
  elif op=="الأسمنت":
    st.write("كمية الأسمنت(tan)", qua_asmnt)
    st.write("التكلفة",asmnto )
  elif op=="الماء":
    st.write("كمية الماء(L)",one_m_c )
    st.write("التكلفة",watro )
elif op == "الخرسانة العادية(حول القواعد المسلحة واسفل السملات(الشدات))":
  N_xSAT,Dxg,Cxt_gas=st.columns(3)
  l_ba=N_xSAT.number_input("طول القاعدة(M)")
  s_ba=Dxg.number_input("عرض القاعدة(M)")
  z_ba=Cxt_gas.number_input("سمك القاعدة(M)")
  Dxog,Cxot_gas=st.columns(2)
  n_ba=Dxog.number_input("طول السمل(الشداد) من رفرفرة القاعدتين العادية(M)")
  u_ba=Cxot_gas.number_input("عرض السمل(الشداد) مضاف اليه رفرفة العادية من الاتجاهين(M)")
  t_ba=st.number_input("سمك طبقة العادية اسفل السمل(الشداد)(M)")
  conqua=(l_ba*s_ba*z_ba)
  coonqua=(n_ba*u_ba*t_ba)


