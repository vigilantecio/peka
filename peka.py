import streamlit as st
import os
import base64

# 1. Konfigurasi Halaman Web
st.set_page_config(
    page_title="PEKA Pantau SP2DK",
    layout="wide",
    initial_sidebar_state="collapsed"
)

# Fungsi otomatis untuk mengubah file gambar lokal menjadi Base64
def get_image_base64(image_path):
    if os.path.exists(image_path):
        with open(image_path, "rb") as img_file:
            return f"data:image/png;base64,{base64.b64encode(img_file.read()).decode()}"
    return ""

# Memuat seluruh aset gambar yang ada di folder Anda
logo_kemenkeu_djp = get_image_base64("logo.png")
logo_djp_footer = get_image_base64("djp.png")
logo_kringpajak = get_image_base64("kringpajak.png")
img_berita1 = get_image_base64("berita 1.png")
img_berita2 = get_image_base64("berita 2.png")
img_dashboard = get_image_base64("bv (1).png")
img_berkas = get_image_base64("bv (2).png")
img_regulation = get_image_base64("bv (3).png")
img_judul_peka = get_image_base64("peka.png")

# 2. Gaya Desain Tingkat Lanjut (Custom CSS)
st.markdown("""
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Outfit:wght@300;400;600;700&display=swap');

    /* Global Typography */
    html, body, [class*="css"] {
        font-family: 'Outfit', sans-serif !important;
    }

    /* Set background aplikasi lebih soft (abu-abu sangat muda) untuk menonjolkan card */
    .stApp {
        background-color: #F8F9FA !important;
    }

    /* Reset layout default Streamlit agar penuh ke pinggir halaman */
    .block-container {
        padding-top: 0rem !important;
        padding-bottom: 0rem !important;
        padding-left: 0rem !important;
        padding-right: 0rem !important;
        max-width: 100% !important;
    }

    /* Sembunyikan elemen dekorasi atas bawaan Streamlit */
    [data-testid="stHeader"] {
        background-color: transparent !important;
        position: absolute !important;
        z-index: 1 !important;
    }

    /* HEADER STYLING - Ditambahkan Gradien dan Bayangan */
    .header-container {
        position: relative;
        width: 100vw;
        height: 160px; 
        background-color: #C10057; 
        box-shadow: 0 4px 20px rgba(193, 0, 87, 0.25);
        color: white;
        padding: 0px 50px;
        display: flex;
        justify-content: space-between;
        align-items: center;
        z-index: 99;
        box-sizing: border-box;
    }
    
    /* GAYA UNTUK GAMBAR JUDUL PEKA BESAR */
    .header-judul-img {
        display: flex;
        align-items: center;
        padding-top: 5px;
        transition: transform 0.3s ease;
    }
    .header-judul-img:hover {
        transform: scale(1.02);
    }
    .header-judul-img img {
        height: 130px; 
        width: auto;
        object-fit: contain;
    }
    
    /* LOGO INSTANSI KANAN ATAS */
    .header-logo {
        background-color: transparent;
        padding: 0;
        display: flex;
        align-items: center;
        justify-content: center;
        margin-right: 20px;
        transition: transform 0.3s ease;
    }
    .header-logo:hover {
        transform: scale(1.02);
    }
    .header-logo img {
        height: 65px;
        width: auto;
        object-fit: contain;
    }

    /* PURE CSS CAROUSEL BANNER BERITA */
    .slider-wrapper {
        position: relative;
        width: 100%;
        margin: 0px auto 35px auto;
        overflow: hidden;
        background: linear-gradient(to bottom, #FFF5F8 0%, #F8F9FA 100%);
        padding-bottom: 20px;
    }
    .slides {
        display: flex;
        overflow-x: auto;
        scroll-snap-type: x mandatory;
        scroll-behavior: smooth;
        padding: 20px 0;
    }
    .slides::-webkit-scrollbar {
        display: none;
    }
    .slide-item {
        scroll-snap-align: center;
        flex-shrink: 0;
        width: 100%;
        display: flex;
        justify-content: center;
        align-items: center;
        padding: 10px 0;
    }
    .slide-item a {
        display: flex;
        justify-content: center;
        align-items: center;
        width: 100%;
    }
    .slide-item img {
        width: 90%;
        max-width: 1200px;
        max-height: 450px;
        object-fit: cover;
        display: block;
        margin: 0 auto;
        border-radius: 20px;
        box-shadow: 0 12px 35px rgba(0,0,0,0.12);
        transition: transform 0.5s ease;
    }
    .slide-item img:hover {
        transform: scale(1.015);
    }
    .slider-nav {
        display: flex;
        justify-content: center;
        gap: 15px;
        margin-top: -15px;
        position: relative;
        z-index: 10;
        padding-bottom: 10px;
    }
    .slider-nav a {
        width: 14px;
        height: 14px;
        border-radius: 50%;
        background-color: rgba(193, 0, 87, 0.3); 
        text-decoration: none;
        transition: all 0.3s ease;
    }
    .slider-nav a:hover, .slider-nav a:focus {
        background-color: #C10057;
        transform: scale(1.2);
        box-shadow: 0 0 10px rgba(193, 0, 87, 0.4);
    }

    /* MENU UTAMA - MEMAKSA BERJEJER SEJAJAR 3 KE SAMPING */
    .menu-container-row {
        text-align: center !important;
        max-width: 1200px;
        margin: 40px auto 60px auto;
        display: flex !important;
        justify-content: center;
        align-items: stretch;
        gap: 30px;
        padding: 0 20px;
    }

    .menu-container-row a {
        text-decoration: none;
        width: 32%;
        display: flex;
    }

    .menu-clickable-card {
        width: 100% !important; 
        height: 100% !important;
        display: flex;
        align-items: center;
        justify-content: center;
        background: white;
        border: 1px solid rgba(193, 0, 87, 0.05);
        border-radius: 20px;
        padding: 12px;
        transition: all 0.4s cubic-bezier(0.175, 0.885, 0.32, 1.275);
        box-shadow: 0 10px 30px rgba(0,0,0,0.06);
        cursor: pointer;
    }
    .menu-clickable-card:hover {
        transform: translateY(-12px);
        border-color: rgba(193, 0, 87, 0.3);
        box-shadow: 0 20px 40px rgba(193, 0, 87, 0.15);
    }
    .menu-clickable-card img {
        width: 100%;
        height: 100%;
        object-fit: contain;
        display: block;
        border-radius: 12px;
    }

    /* FOOTER - Diperbaiki agar Rata Atas Sempurna */
    .footer-container {
        background: linear-gradient(135deg, #C10057 0%, #8E003E 100%);
        color: white;
        padding: 50px 60px; 
        margin-top: 60px;
        font-family: 'Outfit', sans-serif;
        font-size: 14px;
        line-height: 1.7;
        box-shadow: 0 -10px 30px rgba(0,0,0,0.1);
    }
    .footer-grid {
        display: grid;
        grid-template-columns: 1.1fr 1.4fr 1.2fr 1.8fr;
        gap: 40px;
        align-items: start;
        max-width: 1400px;
        margin: 0 auto;
    }
    .footer-title {
        font-weight: 700;
        font-size: 16px;
        text-transform: uppercase;
        border-bottom: 2px solid rgba(255,255,255,0.2);
        padding-bottom: 8px;
        margin-bottom: 16px;
        letter-spacing: 1px;
    }
    .footer-logos-row {
        display: flex;
        flex-direction: row;
        align-items: center;
        justify-content: flex-end;
        gap: 30px;
        height: 100%;
    }
    .img-footer-djp-flat {
        height: 160px; 
        width: auto;
        object-fit: contain;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.25));
        transition: transform 0.3s ease;
    }
    .img-footer-djp-flat:hover {
        transform: scale(1.05);
    }
    .img-footer-kring-flat {
        height: 125px; 
        width: auto;
        object-fit: contain;
        filter: drop-shadow(0 4px 8px rgba(0,0,0,0.25));
        transition: transform 0.3s ease;
    }
    .img-footer-kring-flat:hover {
        transform: scale(1.05);
    }
    </style>
""", unsafe_allow_html=True)

# ==================== IMPLEMENTASI STRUKTUR ====================

# --- 1. HEADER ---
st.markdown(f"""
    <div class="header-container">
        <div class="header-judul-img">
            <img src="{img_judul_peka}" alt="Judul PEKA App">
        </div>
        <div class="header-logo">
            <img src="{logo_kemenkeu_djp}" alt="Logo Kemenkeu DJP">
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 2. BANNER BERITA CAROUSEL ---
st.markdown(f"""
    <div class="slider-wrapper">
        <div class="slides" id="slider">
            <div class="slide-item" id="slide-1">
                <a href="https://www.instagram.com/p/DZNGs9Mk6G5/?igsh=MWgyODF3cW01NzV5" target="_blank">
                    <img src="{img_berita1}" alt="Berita 1">
                </a>
            </div>
            <div class="slide-item" id="slide-2">
                <a href="https://www.instagram.com/p/DYjFizVE17E/?igsh=bzMzYXoyejFoOTVq" target="_blank">
                    <img src="{img_berita2}" alt="Berita 2">
                </a>
            </div>
        </div>
        <div class="slider-nav">
            <a href="#slide-1" title="Slide 1"></a>
            <a href="#slide-2" title="Slide 2"></a>
        </div>
    </div>
""", unsafe_allow_html=True)

# --- 3. TOMBOL NAVIGASI MENU UTAMA ---
st.markdown(f"""
    <div class="menu-container-row">
        <a href="https://kemenkeu-my.sharepoint.com/:f:/r/personal/taufikismail1995_kemenkeu_go_id/Documents/2026/OJT%20CPNS/Pas/Monitoring%20SP2DK?csf=1&web=1&e=oPsnvv" target="_blank">
            <div class="menu-clickable-card">
                <img src="{img_dashboard}" alt="Dashboard">
            </div>
        </a>
        <a href="https://kemenkeu-my.sharepoint.com/:f:/r/personal/taufikismail1995_kemenkeu_go_id/Documents/2026/OJT%20CPNS/Pas/Berkas%20SP2DK?csf=1&web=1&e=FhwzCr" target="_blank">
            <div class="menu-clickable-card">
                <img src="{img_berkas}" alt="Berkas">
            </div>
        </a>
        <a href="https://kemenkeu-my.sharepoint.com/:f:/r/personal/taufikismail1995_kemenkeu_go_id/Documents/2026/OJT%20CPNS/Pas/Policy%20%26%20Regulation?csf=1&web=1&e=qSUO1g" target="_blank">
            <div class="menu-clickable-card">
                <img src="{img_regulation}" alt="Regulation">
            </div>
        </a>
    </div>
""", unsafe_allow_html=True)

# --- 4. FOOTER (Sudah Bersih & Sejajar) ---
st.markdown(f"""
    <div class="footer-container">
        <div class="footer-grid">
            <div>
                <div class="footer-title">Lokasi</div>
                <p><b>Jakarta</b><br>Alamat:<br>Jalan Rasuna Said Blok B Kav. 8</p>
            </div>
            <div>
                <div class="footer-title">Telepon / Kontak</div>
                <p>Telepon: 021-5254270, 5253553, 5254230<br>
                Fax: 021-5207557<br>
                Pos Elektronik: kpp.011@pajak.go.id<br>
                Akun Twitter: @kppsetiabudi1<br>
                Akun Instagram: @kppsetiabudisatu<br>
                Kantor Wilayah: Kantor Wilayah DJP Jakarta Selatan I</p>
            </div>
            <div>
                <div class="footer-title">Wilayah Kerja</div>
                <p><b>Provinsi/Kabupaten/Kota</b><br>Kota Adm. Jakarta Selatan<br>
                <b>Kecamatan</b><br>Setiabudi<br>
                <b>Desa/Kelurahan</b><br>1. Karet<br>2. Karet Kuningan</p>
            </div>
            <div>
                <div class="footer-logos-row">
                    <img class="img-footer-djp-flat" src="{logo_djp_footer}" alt="Logo DJP">
                    <img class="img-footer-kring-flat" src="{logo_kringpajak}" alt="Kring Pajak">
                </div>
            </div>
        </div>
    </div>
""", unsafe_allow_html=True)