import streamlit as st

def project_info():
    st.title("About Project")

    # Latar Belakang
    st.subheader('Latar Belakang')
    st.markdown(
        "Perusahaan telekomunikasi menghadapi tantangan besar dalam mempertahankan pelanggan. Churn atau perpindahan pelanggan merupakan masalah signifikan yang memengaruhi pendapatan dan pertumbuhan bisnis. Ketika pelanggan memutuskan untuk berhenti menggunakan layanan, perusahaan kehilangan pendapatan yang tidak dapat dipulihkan. Hal ini menyebabkan meningkatnya biaya akuisisi pelanggan baru dan merugikan perusahaan dalam jangka panjang. Oleh karena itu, klasifikasi churn menjadi sangat penting untuk mengidentifikasi pelanggan yang berisiko untuk churn, sehingga perusahaan dapat mengambil tindakan preventif."
    )

    # Urgensi
    st.subheader('Urgensi')
    st.markdown(
        "Dalam dunia bisnis yang sangat kompetitif, perusahaan telekomunikasi harus menjaga loyalitas pelanggan untuk tetap berkembang. Meningkatnya tingkat churn tanpa penanganan yang tepat bisa berdampak buruk pada posisi finansial perusahaan. Dengan menggunakan data historis pelanggan, perusahaan dapat mengembangkan model prediksi yang akurat untuk mengidentifikasi tanda-tanda pelanggan yang berisiko tinggi churn. Pendekatan berbasis data ini akan memungkinkan perusahaan untuk fokus pada pelanggan yang membutuhkan perhatian lebih dan menawarkan solusi yang dapat memperpanjang hubungan mereka dengan perusahaan."
    )

    # Tujuan
    st.subheader('Tujuan')
    st.write("Tujuan dari project ini adalah untuk membangun model klasifikasi churn yang dapat memprediksi pelanggan yang berisiko untuk meninggalkan layanan perusahaan. Dengan menggunakan algoritma machine learning, seperti Logistic Regression, Random Forest, dan XGBoost, model ini akan dilatih menggunakan data historis yang mencakup berbagai faktor, seperti durasi penggunaan layanan, tingkat penggunaan, jenis kontrak, dan faktor demografis pelanggan. Tujuan spesifik dari project ini adalah:\n1. Membangun model klasifikasi yang akurat untuk memprediksi churn.\n2. Menganalisis faktor-faktor utama yang memengaruhi keputusan churn pelanggan.\n3. Menyediakan solusi berbasis data untuk tim pemasaran dan layanan pelanggan dalam mengurangi churn."
    )

    # Manfaat
    st.subheader('Manfaat')
    st.write("Proyek ini akan memberikan manfaat yang signifikan bagi perusahaan telekomunikasi, antara lain:\n1. Pengurangan tingkat churn: Dengan memprediksi pelanggan yang berisiko tinggi churn, perusahaan dapat mengambil langkah-langkah proaktif untuk meningkatkan kepuasan dan loyalitas pelanggan.\n2. Optimalisasi sumber daya: Mengarahkan upaya pemasaran dan layanan pelanggan untuk berfokus pada pelanggan yang lebih mungkin bertahan, menghemat waktu dan biaya.\n3. Peningkatan pengalaman pelanggan: Dengan memahami faktor-faktor yang memengaruhi churn, perusahaan dapat menyesuaikan produk dan layanan mereka untuk memenuhi kebutuhan pelanggan dengan lebih baik.\n4. Peningkatan profitabilitas: Dengan menurunkan churn, perusahaan dapat mengurangi biaya akuisisi pelanggan baru dan meningkatkan pendapatan dari pelanggan yang ada."
    )

    # Metodologi
    st.subheader('Metodologi')
    st.write("Untuk mencapai tujuan di atas, data pelanggan yang mencakup atribut seperti tenure, jenis kontrak, biaya bulanan, penggunaan layanan, dan metode pembayaran akan dianalisis. Model machine learning akan dilatih dan dievaluasi menggunakan metrik seperti akurasi, precision, recall, dan F1-score. Selain itu, analisis fitur penting juga akan dilakukan untuk memahami faktor-faktor utama yang memengaruhi churn."
    )

