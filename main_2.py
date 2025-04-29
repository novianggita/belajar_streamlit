import streamlit as st
from PIL import Image

st.set_page_config(
    page_title="Portfolio Novia",
    page_icon=":rocket:",
    layout="wide"
)

# Sidebar Navigasi
with st.sidebar:
    st.title("🚀 Navigasi")
    page = st.radio("Pilih Halaman", ["Tentang Saya", "Project Info", "Visualisasi", "Prediksi"])

# Tampilan Utama
st.markdown(
    """
    <style>
    .main-title {
        font-size: 48px;
        font-weight: 800;
        color: #00E6F6;
    }
    .sub-title {
        font-size: 20px;
        color: #FFFFFF;
    }
    </style>
    """, unsafe_allow_html=True
)

if page == "Visualisasi":
    import visualisasi
    visualisasi.visualisasi_start()

elif page == "Prediksi":
    import app
    app.prediksi()

elif page == "Project Info":
    import project_info
    project_info.project_info()


# Tampilan depan saat pertama dibuka
if page == "Tentang Saya":
    st.title("MY PORTFOLIO")
    st.header("Data Enthusiast")
    col1, col2 = st.columns([1, 2])

    with col1:
        st.image("Foto.JPG", width=250)

    with col2:
        st.markdown('<p class="main-title">Hai, saya Novia! 👋</p>', unsafe_allow_html=True)
        st.markdown(
            '<p class="sub-title">Selamat datang di portofolio saya. Di sini Anda bisa melihat visualisasi data interaktif, prediksi machine learning, dan berbagai proyek data science yang telah saya kerjakan.</p>',
            unsafe_allow_html=True)
        st.write('\n')
        st.markdown('<p class="sub-title">Analis Data yang berpengalaman dan berdedikasi, dengan pengalaman beberapa tahun dalam mengidentifikasi efisiensi serta permasalahan dalam alur data, sekaligus mampu mengomunikasikan kebutuhan proyek secara efektif. Terampil dalam menerima dan memantau data dari berbagai sumber, termasuk basis data SQL dan file Excel. Memiliki kemampuan untuk menyintesis informasi kuantitatif serta berinteraksi secara profesional dengan rekan kerja maupun klien. Dengan komitmen tinggi terhadap keunggulan dan rekam jejak yang terbukti dalam berbagai peran, saya siap untuk menerapkan keahlian saya dan memberikan dampak yang bermakna di bidang data.</p>',
            unsafe_allow_html=True)
        st.markdown("✨ Gunakan menu di sidebar untuk menjelajah.")

        st.write('\n')
        import kontak
        kontak.tampilkan_kontak()
