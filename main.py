import streamlit as st

# session state agar ketika pindah page tidak berubah data yang tersedia

st.session_state.pindah = True

Homepage = st.Page("Halaman Utama/halaman_utama.py",
    title=" Profil Kelompok",
    default=True)


Mahasiswa8 = st.Page(
    "Buku Kating/075_Aliya Ammara Ananta.py",
    title="075 - Aliya Ammara Ananta",
    icon=":material/person:",
)

#Perlu diperhatikan perubahannya


#Perlu diperhatikan perubahannya
if st.session_state.pindah:
    pg = st.navigation(
        {
            "Halaman Utama": [Homepage],
            "Buku Kating": [Mahasiswa8],
            
        }
    )
else:
    st.write("Maaf Anda kurang beruntung :(") 
pg.run()

