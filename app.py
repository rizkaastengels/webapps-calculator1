import streamlit as st

def main():
    st.title("Kalkulator Sederhana Hak Milik Adit")
    st.write(" Di Appsweb ini saya membuat operator untuk menghitung dasar matematika seperti penjumlahan, pengurangan, perkalian, dan pembagian.")
    st.write("Saya Rizky Aditya Putra Nugraha Berkuliah di Politeknik AKA Bogor")
    st.write("PANGGIL SAYA ADIT GA ASIK KALO TIDAK KENAL SAYA :sunglasses: :kissing_closed_eyes:")
    st.write("SAYA SUKA MAKAN BAKSO")
    st.write("Saya pacar umayy :heartpulse:")
   
    # Input angka pertama
    num1 = st.number_input("Masukkan angka pertama:", value=0.0, step=1.0)

    # Input angka kedua
    num2 = st.number_input("Masukkan angka kedua:", value=0.0, step=1.0)
    
    # Pilihan operasi
    operation = st.selectbox(
        "Pilih operasi matematika:",
        ("Penjumlahan", "Pengurangan", "Perkalian", "Pembagian")
    )
    
    # Tombol untuk menghitung
    if st.button("Hitung"):
        if operation == "Penjumlahan":
            result = num1 + num2
            st.success(f"Hasil Penjumlahan: {result}")
        elif operation == "Pengurangan":
            result = num1 - num2
            st.success(f"Hasil Pengurangan: {result}")
        elif operation == "Perkalian":
            result = num1 * num2
            st.success(f"Hasil Perkalian: {result}")
        elif operation == "Pembagian":
            if num2 != 0:
                result = num1 / num2
                st.success(f"Hasil Pembagian: {result}")
            else:
                st.error("Kesalahan: Pembagian dengan nol tidak diperbolehkan.")
    
if __name__ == "__main__":
    main()
