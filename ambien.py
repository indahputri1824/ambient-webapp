import streamlit as st

st.set_page_config(page_title="SmartAmbient", page_icon=":cloud:", layout="wide")

st.subheader('Hi, I am Smart Ambient :cloud: :wave:')
st.title('__**APLIKASI PENENTUAN KUALITAS UDARA AMBIEN**__')


st.write("---")
left_column, middle_column, right_column= st.columns(3)
with left_column:
    st.write('__**INTRO**__ - Sebuah aplikasi yang dibuat untuk memudahkan pengguna agar dapat menentukan kualitas __**udara ambien**__ di suatu daerah dengan mudah.') 
with middle_column:
    st.write('''Aplikasi ini dibuat dan dikembangkan oleh Kelompok 2 LPK, Kelas Akselerasi 2022:
1. Aisyatul Fajriyani (2240190)
2. Fadhil Ahmad Fahrezi (2240193)
3. Lucky Ramadhan (2240197)
4. Putri Indah Nuraini (2240206)
5. Stevie Evan Hardiyanto (2240213)
''')

with right_column:
    st.write('Aplikasi ini mengacu pada __**Peraturan Pemerintah Republik Indonesia No.41 Tahun 1999 tentang Pengendalian Pencemaran Udara**__.')
    st.write("[Click here to view >](https://drive.google.com/file/d/1APHCbTCCitBioA48q_a2a2aVE-PCa-Tu/view?usp=drivesdk)")

st.write("---")

st.markdown('__**PENGINPUTAN DATA**__')

company = st.text_input('Masukkan nama perusahaan')

ppc = st.text_input('Masukkan nama petugas pengambil contoh uji')

loc = st.text_input('Masukkan titik/lokasi pengambilan contoh uji ')
d=st.text_input('Masukkan hari dan tanggal pengambilan contoh uji (hari, dd/mm/yyyy)')

import datetime
tstart = st.time_input('Masukkan waktu mulai pengambilan contoh uji', datetime.time())
tfinish = st.time_input('Masukkan waktu selesai pengambilan contoh uji', datetime.time())

st.write("---")
import streamlit as st
st.markdown('__**PENGINPUTAN DATA PENGUKURAN**__ ')
st.caption('Sampling Udara Ambien dengan Metode HVAS')
flowmean=st.number_input('Masukkan rata-rata laju (L/menit) :')
time=st.number_input('Masukkan lama waktu pengukuran (jam) :')
if time!=24:
    xv=st.warning('Masukkan lama pengambilan hanya 24 jam')

Pa=st.number_input('Masukkan tekanan aktual (hpa) :')
Ta=st.number_input('Masukkan suhu udara / temperatur aktual (derajat celcius) :')
digit=4
bptsp=bptspr=bptsprr=st.number_input('Masukkan bobot partikulat yang dijerap [TSP] (gram) :',format='%.'+str(digit)+'f')
bppmten=bppmtenr=bppmtenrr=st.number_input('Masukkan bobot partikulat yang dijerap [PM10] (gram) :',format='%.'+str(digit)+'f')
bppmtwopointfive=bppmtwopointfiver=bppmtwopointfiverr=st.number_input('Masukkan bobot partikulat yang dijerap [PM2.5] (gram) :',format='%.'+str(digit)+'f')

st.write("---")
st.caption('Sampling Udara Ambien dengan Metode AGIS')
flowmeanx=st.number_input('Masukkan rata-rata laju (L/menit) [AGIS] :')
timex=st.number_input('Masukkan lama waktu pengukuran (jam) [AGIS] :')
st.warning('Masukkan lama pengambilan hanya 1 jam atau 24 jam')
if timex==24:
    soxvol=st.number_input('Masukkan volume larutan sampel (SOx) (L) :')
    sox=st.number_input('Masukkan konsentrasi terukur SOx secara spektrofotometri (ppm) :')
    noxvol=st.number_input('Masukkan volume larutan sampel (NOx) (L) :')
    nox=st.number_input('Masukkan konsentrasi terukur NOx secara spektrofotometri (ppm) :')

if timex==1:
    soxvoly=st.number_input('Masukkan volume larutan sampel (SOx) (L) :')
    soxy=st.number_input('Masukkan konsentrasi terukur SOx secara spektrofotometri (ppm) :')
    noxvoly=st.number_input('Masukkan volume larutan sampel (NOx) (L) :')
    noxy=st.number_input('Masukkan konsentrasi terukur NOx secara spektrofotometri (ppm) :')
    oxvoly=st.number_input('Masukkan volume larutan sampel (Ox) (L) :')
    oxy=st.number_input('Masukkan konsentrasi terukur Ox secara spektrofotometri (ppm) :')    
    
Pax=st.number_input('Masukkan tekanan aktual (hpa) [AGIS] :')
Tax=st.number_input('Masukkan suhu udara / temperatur aktual (derajat celcius) [AGIS] :')  
    
st.write("---")
tombol=st.button('TAMPILKAN HASIL ANALISIS [HVAS & AGIS 24 jam]')
pencet=st.button('TAMPILKAN HASIL ANALISIS [HVAS & AGIS 1 jam]')
press=st.button('TAMPILKAN KESIMPULAN')

if tombol:
    V=(flowmean)*(time*60)*((Pa*0.75)/(Ta+273))*(298/760)
    Vkonversi=V/1000
    massatsp=bptsp*1000000
    massapmten=bppmten*1000000
    massapmtwopointfive=bppmtwopointfive*1000000
    TSP=massatsp/Vkonversi
    PM10=massapmten/Vkonversi
    PM2point5=massapmtwopointfive/Vkonversi
   
    Vx=(flowmeanx)*(timex*60)*((Pax*0.75)/(Tax+273))*(298/760)
    massasoxx=sox*soxvol*1000
    massanox=nox*noxvol*1000
    NOXCONC=(massanox/Vx)*1000
    SOXCONC=(massasoxx/Vx)*1000
    
    st.success(f'Nilai TSP yang diperoleh adalah {TSP} mikrogram/Nm^3')
    if TSP<230:
        tspx=st.write('Parameter telah memenuhi standar')
    elif TSP>=230:
        tspxnd=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Nilai PM10 yang diperoleh adalah {PM10} mikrogram/Nm^3')
    if PM10<150:
        pmx=st.write('Parameter telah memenuhi standar')
    elif PM10>=150:
        pmxnd=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Nilai PM2.5 yang diperoleh adalah {PM2point5} mikrogram/Nm^3')
    if PM2point5<65:
        pmtwo=st.write('Parameter telah memenuhi standar')
    elif PM2point5>=65:
        pmtwond=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Konsentrasi SO2 yang diperoleh adalah {SOXCONC} mikrogram/Nm3')
    if SOXCONC<365:
        soxd=st.write('Parameter telah memenuhi standar')
    elif SOXCONC>=365:
        soxdnd=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Konsentrasi NO2 yang diperoleh adalah {NOXCONC} mikrogram/Nm^3')
    if NOXCONC<150:
        noxd=st.write('Parameter telah memenuhi standar')
    elif NOXCONC>=150:
        noxdnd=st.write('Parameter tidak memenuhi standar')
        

if pencet:
    V=(flowmean)*(time*60)*((Pa*0.75)/(Ta+273))*(298/760)
    Vkonversi=V/1000
    massatsp=bptsp*1000000
    massapmten=bppmten*1000000
    massapmtwopointfive=bppmtwopointfive*1000000
    TSPnd=massatsp/Vkonversi
    PM10nd=massapmten/Vkonversi
    PM2point5nd=massapmtwopointfive/Vkonversi
    
    Vy=(flowmeanx)*(timex*60)*((Pax*0.75)/(Tax+273))*(298/760)
    massasoxy=soxy*soxvoly*1000
    massanoxy=noxy*noxvoly*1000
    massaoxy=oxy*oxvoly*1000
    NOXCONCnd=(massanoxy/Vy)*1000
    SOXCONCnd=(massasoxy/Vy)*1000
    OXCONCnd=(massaoxy/Vy)*1000
    
    st.success(f'Nilai TSP yang diperoleh adalah {TSPnd} mikrogram/Nm^3')
    if TSPnd<230:
        tspndx=st.write('Parameter telah memenuhi standar')
    elif TSPnd>=230:
        tspndxnd=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Nilai PM10 yang diperoleh adalah {PM10nd} mikrogram/Nm^3')
    if PM10nd<150:
        pmndx=st.write('Parameter telah memenuhi standar')
    elif PM10nd>=150:
        pmndxnd=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Nilai PM2.5 yang diperoleh adalah {PM2point5nd} mikrogram/Nm^3')
    if PM2point5nd<65:
        pmndtwo=st.write('Parameter telah memenuhi standar')
    elif PM2point5nd>=65:
        pmndtwond=st.write('Parameter tidak memenuhi standar')
        
    st.success(f'Konsentrasi SO2 yang diperoleh adalah {SOXCONCnd} mikrogram/Nm^3')
    if SOXCONCnd<365:
        soxe=st.write('Parameter telah memenuhi standar')
    elif SOXCONCnd>=365:
        soxend=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Konsentrasi NO2 yang diperoleh adalah {NOXCONCnd} mikrogram/Nm^3')
    if NOXCONCnd<150:
        noxe=st.write('Parameter telah memenuhi standar')
    elif NOXCONCnd>=150:
        noxend=st.write('Parameter tidak memenuhi standar')
    
    st.success(f'Konsentrasi O3 yang diperoleh adalah {OXCONCnd} mikrogram/Nm^3')
    if OXCONCnd<235:
        oxd=st.write('Parameter telah memenuhi standar')
    elif OXCONCnd>=235:
        oxdnd=st.write('Parameter tidak memenuhi standar')
        
    
    
if press:
    if timex==24:
        Vr=(flowmean)*(time*60)*((Pa*0.75)/(Ta+273))*(298/760)
        Vkonversir=Vr/1000
        massatspr=bptspr*1000000
        massapmtenr=bppmtenr*1000000
        massapmtwopointfiver=bppmtwopointfiver*1000000
        TSPr=massatspr/Vkonversir
        PM10r=massapmtenr/Vkonversir
        PM2point5r=massapmtwopointfiver/Vkonversir
        
        Vxr=(flowmeanx)*(timex*60)*((Pax*0.75)/(Tax+273))*(298/760)
        massasoxxr=sox*soxvol*1000
        massanoxr=nox*noxvol*1000
        NOXCONCr=(massanoxr/Vxr)*1000
        SOXCONCr=(massasoxxr/Vxr)*1000
        
        import numpy as np
        a=TSPr
        b=PM10r
        c=PM2point5r
        d=NOXCONCr
        e=SOXCONCr
    
        if a<230 and b<150 and c<65 and d<150 and e<365:
            st.write('__**BERITA ACARA SAMPLING**__')
            st.write('Pada hari', d, 'dan pada pukul', tstart, 'hingga', tfinish, 'telah dilakukan pengambilan contoh uji pada :')
            st.write('Nama Perusahaan :',company)
            st.write('Nama PPC :',ppc)
            ()
            st.write('Diperoleh Hasil :')
            st.write('Kualitas Udara Ambien pada lokasi',loc,'dinyatakan BAIK')
        else:
            st.write('__**BERITA ACARA SAMPLING**__')
            st.write('Pada hari', d, 'dan pada pukul', tstart, 'hingga', tfinish, 'telah dilakukan pengambilan contoh uji pada :')
            st.write('Nama Perusahaan :',company)
            st.write('Nama PPC :',ppc)
            ()
            st.write('Diperoleh Hasil :')
            st.write('Kualitas Udara Ambien pada lokasi',loc,'dinyatakan BURUK')
        
        
    if timex==1:      
        Vrr=(flowmean)*(time*60)*((Pa*0.75)/(Ta+273))*(298/760)
        Vkonversirr=Vrr/1000
        massatsprr=bptsprr*1000000
        massapmtenrr=bppmtenrr*1000000
        massapmtwopointfiverr=bppmtwopointfiverr*1000000
        TSPndr=massatsprr/Vkonversirr
        PM10ndr=massapmtenrr/Vkonversirr
        PM2point5ndr=massapmtwopointfiverr/Vkonversirr
        
        Vyr=(flowmeanx)*(timex*60)*((Pax*0.75)/(Tax+273))*(298/760)
        massasoxyr=soxy*soxvoly*1000
        massanoxyr=noxy*noxvoly*1000
        massaoxyr=oxy*oxvoly*1000
        NOXCONCndr=(massanoxyr/Vyr)*1000
        SOXCONCndr=(massasoxyr/Vyr)*1000
        OXCONCndr=(massaoxyr/Vyr)*1000
        
        import numpy as np
        f=TSPndr
        g=PM10ndr
        h=PM2point5ndr
        i=NOXCONCndr
        j=SOXCONCndr
        k=OXCONCndr
    
        if f<230 and g<150 and h<65 and i<150 and j<365 and k<235:
            st.write('__**BERITA ACARA SAMPLING**__')
            st.write('Pada hari', d, 'dan pada pukul', tstart, 'hingga', tfinish, 'telah dilakukan pengambilan contoh uji pada :')
            st.write('Nama Perusahaan :',company)
            st.write('Nama PPC :',ppc)
            ()
            st.write('Diperoleh Hasil :')
            st.write('Kualitas Udara Ambien pada lokasi',loc,'dinyatakan BAIK')
        else:
            st.write('__**BERITA ACARA SAMPLING**__')
            st.write('Pada hari', d, 'dan pada pukul', tstart, 'hingga', tfinish, 'telah dilakukan pengambilan contoh uji pada :')
            st.write('Nama Perusahaan :',company)
            st.write('Nama PPC :',ppc)
            ()
            st.write('Dan diperoleh Hasil :')
            st.write('Kualitas Udara Ambien pada lokasi',loc,'dinyatakan BURUK')

st.write("---")
st.header("Let Us Know!")
st.caption("saran dan pengembangan apa yang kalian inginkan dari aplikasi ini,:point_down:")
st.write('##')
contact_form=('''
<form action="https://formsubmit.co/putriindah18004@gmail.com" method="POST">
     <input type="hidden" name="_captcha" value="false">
     <input type="text" name="name" placeholder="Your name" required>
     <input type="email" name="email" placeholder="Your email" required>
     <textarea name="message" placeholder="your message here" required></textarea>
     <button type="submit">Send</button>
</form>
''')
left_column, right_column= st.columns(2)
with left_column:
    st.markdown(contact_form, unsafe_allow_html=True)
with right_column:
    st.empty()
       
    


    
  