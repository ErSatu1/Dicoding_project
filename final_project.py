import pandas as pd
import matplotlib.pyplot as plt
import streamlit as st
import datetime






min_date = datetime.date(2013, 1, 1)
max_date = datetime.date(2017, 2, 28)



aoti_sample = pd.read_csv('aoti_sample.csv')
chang_sample = pd.read_csv('chang_sample.csv')
ding_sample= pd.read_csv('ding_sample.csv')
dong_sample = pd.read_csv('dong_sample.csv')
guan_sample = pd.read_csv('guan_sample.csv')
gucheng_sample = pd.read_csv('gucheng_sample.csv')
hua_sample = pd.read_csv('hua_sample.csv')
nong_sample = pd.read_csv('nong_sample.csv')
shun_sample = pd.read_csv('shun_sample.csv')
tian_sample = pd.read_csv('tian_sample.csv')
wanliu_sample = pd.read_csv('wanliu_sample.csv')
wanshou_sample = pd.read_csv('wanshou_sample.csv')

aoti_sample['tanggal'] = pd.to_datetime(aoti_sample['tanggal'])
aoti_sample = aoti_sample.reset_index()


chang_sample['tanggal'] = pd.to_datetime(chang_sample['tanggal'])
chang_sample.reset_index()

ding_sample['tanggal'] = pd.to_datetime(ding_sample['tanggal'])
ding_sample.reset_index()

dong_sample['tanggal'] = pd.to_datetime(dong_sample['tanggal'])
dong_sample.reset_index()

guan_sample['tanggal'] = pd.to_datetime(guan_sample['tanggal'])
guan_sample.reset_index()

gucheng_sample['tanggal'] = pd.to_datetime(gucheng_sample['tanggal'])
gucheng_sample.reset_index()

hua_sample['tanggal'] = pd.to_datetime(hua_sample['tanggal'])
hua_sample.reset_index()

nong_sample['tanggal'] = pd.to_datetime(nong_sample['tanggal'])
nong_sample.reset_index()

shun_sample['tanggal'] = pd.to_datetime(shun_sample['tanggal'])
shun_sample.reset_index()

tian_sample['tanggal'] = pd.to_datetime(tian_sample['tanggal'])
tian_sample.reset_index()

wanliu_sample['tanggal'] = pd.to_datetime(wanliu_sample['tanggal'])
wanliu_sample.reset_index()

wanshou_sample['tanggal'] = pd.to_datetime(wanshou_sample['tanggal'])
wanshou_sample.reset_index()

with st.sidebar:
    st.subheader('Hi! Selamat Datang')
    

    kota = st.selectbox(
        label="Kota mana yang ingin kamu ketahui?",
        options=('Aotizhongxin', 'Changping', 'Dingling', 'Dongsi',
                'Guanyuan', 'Gucheng', 'Huairou', 'Nongzhanguan', 
                'Shunyi', 'Tiantan', 'Wanliu', 'Whanshouxigong')
    )
    if kota == 'Aotizhongxin':
        kota = aoti_sample
        nama = 'Aotizhongxin'
    elif kota == 'Gucheng':
        kota = gucheng_sample
        nama = 'Gucheng'
    elif kota == 'Changping':
        kota = chang_sample
        nama = 'Changping'
    elif kota == 'Dingling':
        kota = ding_sample
        nama = 'Dingling'
    elif kota == 'Dongsi':
        kota = dong_sample
        nama = 'Dongsi'
    elif kota == 'Guanyuan':
        kota = gucheng_sample
        nama = 'Guanyuan'
    elif kota == 'Huairou':
        kota = hua_sample
        nama = 'Huairou'
    elif kota == 'Nongzhanguan':
        kota = nong_sample
        nama = 'Nongzhanguan'
    elif kota == 'Shunyi':
        kota = shun_sample
        nama = 'Shunyi'
    elif kota == 'Tiantan':
        kota = tian_sample
        nama = 'Tiantan'
    elif kota == 'Wanliu':
        kota = wanliu_sample
        nama = 'Wanliu'
    elif kota == 'Whanshouxigong':
        kota = wanshou_sample
        nama = 'Whanshouxigong'
    else:
        kota = kota

    start_date, end_date = st.date_input(
    label='Rentang Waktu',min_value=min_date,
    max_value=max_date,
    value=[min_date, max_date]
    )

main_df = kota[(kota["tanggal"] >= str(start_date)) & 
                (kota["tanggal"] <= str(end_date))]




st.title('Kondisi Udara Beberapa Kota di China')
st.markdown('<div style="text-align: justify;">Seperti yang kita ketahui polusi udara yang sekarang kian meningkat adanya. \nMaka dari itu kami memiliki data dari tahun 2013 hingga 2017 \nmengenai komposisi udara di beberapa kota di China dan juga PM2.5 serta PM10.\n</div>', unsafe_allow_html=True)

st.subheader('Grafik Polusi PM2.5 serta PM10 di kota %s' %nama)
fig, ax1 = plt.subplots(figsize=(20, 5))
ax1.plot(
        main_df["tanggal"],
        main_df["PM2.5"],
        marker='o',
        linewidth=2,
        color="#72BCD4",
        label = 'PM 2.5'
    )

ax1.set_title("Grafik kenaikan polusi PM2.5 dan PM10", loc="center", fontsize=20)
#tick_count = 15
#tick_spacing = len(main_df.index) // (tick_count - 1)
#ax1.set_xticks(main_df["tanggal"])
ax1.tick_params(axis='x', labelrotation=45)
ax1.tick_params(axis='both', labelsize=10)

ax2 = ax1.twinx()
ax2.plot(
        main_df["tanggal"],
        main_df["PM10"],
        marker='s',
        linewidth=2,
        color="#FFA07A",
        label='PM10'
    )

ax2.tick_params(axis='y', labelsize=10)
ax2.yaxis.set_visible(False)
ax1.legend(loc='upper left')
ax2.legend(loc='upper right')
st.pyplot(fig)

with st.expander("Apa itu PM 2.5?"):
    st.write(
        """PM2.5 adalah partikel kecil berukuran 2.5 mikrometer atau kurang yang terdapat
        dalam polusi udara. Sumber utama termasuk gas buang kendaraan, industri, pembakaran 
        biomassa, dan aktivitas konstruksi. Partikel ini dapat merugikan kesehatan manusia 
        karena dapat masuk ke dalam saluran pernapasan. Pemantauan dan pengendalian polusi 
        PM2.5 penting untuk melindungi kesehatan dan lingkungan. Banyak negara telah mengambil 
        langkah-langkah untuk mengurangi emisi dan membatasi paparan terhadap PM2.5.
        """
    )

import streamlit as st

with st.expander("Apa itu PM 10?"):
    st.write(
        """PM10 adalah partikel udara dengan diameter kurang dari atau sama dengan 10 mikrometer. 
        Sumber utama PM10 meliputi debu dari jalan raya, industri, dan kegiatan konstruksi. 
        Seperti PM2.5, partikel ini dapat memiliki dampak negatif pada kesehatan manusia karena 
        dapat terhirup dan masuk ke dalam saluran pernapasan. Pengawasan polusi PM10 juga 
        penting untuk menjaga kualitas udara dan kesehatan masyarakat. Upaya pengendalian 
        emisi dan tindakan mitigasi serupa telah diimplementasikan di banyak wilayah untuk 
        mengurangi dampak polusi PM10."""
    )


mean_values = main_df[['SO2','NO2','CO','O3']].mean()

st.subheader('Komposisi Udara pada Kota %s'%nama)
fig, ax = plt.subplots(figsize=(16, 8))
labels = mean_values.index
sizes = mean_values.values
colors = ['#FFF689', '#E03616', '#58355E', '#5998C5']
explode = (0.1, 0.1, 0.1, 0.1)
plt.pie(sizes, labels=labels, colors=colors, autopct=lambda p: '{:.1f}%'.format(p) if p > 0 else '', explode=explode)
plt.title('Komposisi Udara kota %s' % nama)
st.pyplot(fig)

import streamlit as st

st.write(
    """
    **SO2 (Dioksida Belerang):**
    - **Sumber:** Emisi industri, pembakaran bahan bakar fosil, dan aktivitas vulkanik.
    - **Dampak:** Pada kadar tinggi, dapat menyebabkan iritasi saluran pernapasan, masalah pernapasan, dan kontributor utama hujan asam.

    **NO2 (Dioksida Nitrogen):**
    - **Sumber:** Kendaraan bermotor, pembakaran bahan bakar, dan proses industri.
    - **Dampak:** Menyebabkan iritasi saluran pernapasan, meningkatkan risiko infeksi pernapasan.

    **CO (Karbon Monoksida):**
    - **Sumber:** Pembakaran bahan bakar fosil, kendaraan bermotor, dan proses industri.
    - **Dampak:** Menghambat transportasi oksigen dalam darah, dapat menyebabkan keracunan dan masalah kardiovaskular.

    **O3 (Ozon):**
    - **Sumber:** Reaksi kimia antara oksigen dan polutan lain di bawah sinar matahari.
    - **Dampak:** Iritasi saluran pernapasan, masalah pernapasan, dan dapat memperburuk kondisi kesehatan yang sudah ada, seperti asma.
    """
)
