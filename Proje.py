import tkinter as tk
from tkinter import ttk, messagebox
import mysql.connector


def giris_kontrol():
    # Kullanıcının girdiği ad ve soyadı al
    kullanici_adi = entry_adi.get()
    soyadi = entry_soyadi.get()

    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanında kullanıcı adı ve soyadı ile uyuşan bir kayıt var mı kontrol et
    cursor.execute("SELECT * FROM antrenorler WHERE Antrenorler_Ad=%s AND Antrenorler_Soyad=%s", (kullanici_adi, soyadi))
    row = cursor.fetchone()

    # Veritabanı bağlantısını kapat
    conn.close()

    if row:
        # Kullanıcı adı ve soyadı veritabanındaki bilgilerle uyuşuyorsa yeni pencere aç
        yeni_pencere()


    else:
        messagebox.showerror("Hata", "Kullanıcı adı veya soyadı hatalı!")


def yeni_pencere():
    # Ana Ekran
    root = tk.Tk()
    root.title("Üye İşlemleri")
    root.geometry("400x400+750+300")
    root.configure(bg="black")


    # Üye Ekle Butonu
    btn_uye_ekle = tk.Button(root, text="Üye Ekle", command=uye_ekle_pencere,bg="red",width=17,height=2)
    btn_uye_ekle.pack(pady=3)

    # Ölçüm Ekle Butonu
    btn_olcum_ekle = tk.Button(root, text=" Üyeye Ölçüm Ekle", command=olcum_ekle_pencere,bg="red",width=17,height=2)
    btn_olcum_ekle.pack(pady=3)

    # Ek Gıda Ekle Butonu
    btn_ek_gida_ekle = tk.Button(root, text=" Üyeye Ek Gıda Ekle", command=ek_gida_ekle_pencere,bg="red",width=17,height=2)
    btn_ek_gida_ekle.pack(pady=3)

    # antrenor ekleme
    btn_antrenor_ekle = tk.Button(root, text="Üyeye Antrenor Ekle", command=antrenor_ekle_pencere,bg="red",width=17,height=2)
    btn_antrenor_ekle.pack(pady=3)

    # diyet ekleme
    btn_diyet_ekle = tk.Button(root, text="Üyeye Diyet Ekle", command=diyet_ekle_pencere,bg="red",width=17,height=2)
    btn_diyet_ekle.pack(pady=3)

    # diyetisyen ekleme
    btn_diyetisyen_ekle = tk.Button(root, text="Üyeye Diyetisyen Ekle", command=diyetisyen_ekle_pencere,bg="red",width=17,height=2)
    btn_diyetisyen_ekle.pack(pady=3)

    btn_program_ekle= tk.Button(root,text="Üyeye Program Ekleme",command=program_ekle_pencere,bg="red",width=17,height=2)
    btn_program_ekle.pack(pady=3)



    root.mainloop()

def uye_ekle_pencere():
    def uye_ekle():
        # Üye Ekleme Fonksiyonu
        ad = entry_uye_adi.get()
        soyad = entry_uye_soyadi.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına üye bilgilerini ekle
        cursor.execute("INSERT INTO uyeler (Uye_Ad, Uye_Soyad) VALUES (%s, %s)", (ad, soyad))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Üye başarıyla eklendi!")

    # Üye Ekle Penceresi
    uye_ekle_pencere = tk.Toplevel()
    uye_ekle_pencere.title("Üye Ekle")
    uye_ekle_pencere.geometry("400x400+750+300")
    uye_ekle_pencere.configure(bg="black")

    # Ad Giriş Kutusu
    label_uye_adi = tk.Label(uye_ekle_pencere, text="Adı:",bg="black",fg="red")
    label_uye_adi.pack()
    entry_uye_adi = tk.Entry(uye_ekle_pencere)
    entry_uye_adi.pack()

    # Soyad Giriş Kutusu
    label_uye_soyadi = tk.Label(uye_ekle_pencere, text="Soyadı:",bg="black",fg="red")
    label_uye_soyadi.pack()
    entry_uye_soyadi = tk.Entry(uye_ekle_pencere)
    entry_uye_soyadi.pack()

    # Üye Ekle Düğmesi
    btn_uye_ekle = tk.Button(uye_ekle_pencere, text="Üye Ekle", command=uye_ekle,bg="red")
    btn_uye_ekle.pack(pady=10)

def olcum_ekle_pencere():
    def olcum_ekle():
        # Ölçüm Ekleme Fonksiyonu
        uye_id = combo_uyeler.get()
        boy = entry_boy.get()
        bacak = entry_bacak.get()
        bel = entry_bel.get()
        kilo = entry_kilo.get()
        kol = entry_kol.get()
        dogum_tarihi = entry_dogum_tarihi.get()
        olcum_tarihi = entry_olcum_tarihi.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına ölçüm bilgilerini ekle
        cursor.execute(
            "INSERT INTO olcumler (olcum_id, boy, bacak, bel, kilo, kol, dogumtarihi, olcumtarih) VALUES (%s, %s, %s, %s, %s, %s, %s, %s)",
            (uye_id, boy, bacak, bel, kilo, kol, dogum_tarihi, olcum_tarihi))
        conn.commit()

        olcum_id = cursor.lastrowid

        sql_uye_olcum = "INSERT INTO uye_olcumler (uye_id, olcum_id) VALUES (%s, %s)"
        values_uye_olcum = (uye_id,olcum_id)

        cursor.execute(sql_uye_olcum, values_uye_olcum)
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Ölçüm başarıyla eklendi!")

    # Ölçüm Ekle Penceresi
    olcum_ekle_pencere = tk.Toplevel()
    olcum_ekle_pencere.title("Ölçüm Ekle")
    olcum_ekle_pencere.geometry("400x400+750+300")
    olcum_ekle_pencere.configure(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(olcum_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()
    members = get_all_members()
    combo_uyeler = ttk.Combobox(olcum_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Boy Giriş Kutusu
    label_boy = tk.Label(olcum_ekle_pencere, text="Boy:",bg="black",fg="red")
    label_boy.pack()
    entry_boy = tk.Entry(olcum_ekle_pencere)
    entry_boy.pack()

    # Bacak Giriş Kutusu
    label_bacak = tk.Label(olcum_ekle_pencere, text="Bacak:",bg="black",fg="red")
    label_bacak.pack()
    entry_bacak = tk.Entry(olcum_ekle_pencere)
    entry_bacak.pack()

    # Bel Giriş Kutusu
    label_bel = tk.Label(olcum_ekle_pencere, text="Bel:",bg="black",fg="red")
    label_bel.pack()
    entry_bel = tk.Entry(olcum_ekle_pencere)
    entry_bel.pack()

    # Kilo Giriş Kutusu
    label_kilo = tk.Label(olcum_ekle_pencere, text="Kilo:",bg="black",fg="red")
    label_kilo.pack()
    entry_kilo = tk.Entry(olcum_ekle_pencere)
    entry_kilo.pack()

    # Kol Giriş Kutusu
    label_kol = tk.Label(olcum_ekle_pencere, text="Kol:",bg="black",fg="red")
    label_kol.pack()
    entry_kol = tk.Entry(olcum_ekle_pencere)
    entry_kol.pack()

    # Doğum Tarihi Giriş Kutusu
    label_dogum_tarihi = tk.Label(olcum_ekle_pencere, text="Doğum Tarihi:",bg="black",fg="red")
    label_dogum_tarihi.pack()
    entry_dogum_tarihi = tk.Entry(olcum_ekle_pencere)
    entry_dogum_tarihi.pack()

    # Ölçüm Tarihi Giriş Kutusu
    label_olcum_tarihi = tk.Label(olcum_ekle_pencere, text="Ölçüm Tarihi:",bg="black",fg="red")
    label_olcum_tarihi.pack()
    entry_olcum_tarihi = tk.Entry(olcum_ekle_pencere)
    entry_olcum_tarihi.pack()

    # Ölçüm Ekle Düğmesi
    btn_olcum_ekle = tk.Button(olcum_ekle_pencere, text="Ölçüm Ekle", command=olcum_ekle,bg="red")
    btn_olcum_ekle.pack(pady=10)

def get_all_programs():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm programları çek
    cursor.execute("SELECT program_id, program_ad FROM programlar")
    programs = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Program adları veya ID'leri içeren bir liste döndür
    return programs

def get_all_dietitians():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm diyetisyenleri çek
    cursor.execute("SELECT  diyetisyen_ID,diyetisyen_Ad, diyetisyen_soyad FROM diyetisyenler")
    dietitians = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Diyetisyen adları veya ID'leri içeren bir liste döndür
    return dietitians

def get_all_diets():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm diyetleri çek
    cursor.execute("SELECT Diyet_ID, Diyet_Ad FROM diyet")
    diets = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Diyet adları veya ID'leri içeren bir liste döndür
    return diets
def get_all_additional_foods():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm ek gıdaları çek
    cursor.execute("SELECT gida_id,gida_ad FROM ek_gidalar")
    additional_foods = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Ek gıda adları veya ID'leri içeren bir liste döndür
    return additional_foods

def get_all_members():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm üyeleri çek
    cursor.execute("SELECT Uye_ID, Uye_Ad, Uye_Soyad FROM uyeler")
    members = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Üye adları veya ID'leri içeren bir liste döndür
    return members
def get_all_trainers():
    # MySQL veritabanına bağlan
    conn = mysql.connector.connect(
        host="localhost",
        user="root",
        password="",
        database="burakPython"
    )
    cursor = conn.cursor()

    # Veritabanından tüm antrenörleri çek
    cursor.execute("SELECT Antrenorler_ID, Antrenorler_Ad, Antrenorler_Soyad FROM antrenorler")
    trainers = cursor.fetchall()

    # Veritabanı bağlantısını kapat
    conn.close()

    # Antrenör adları veya ID'leri içeren bir liste döndür
    return trainers
def program_ekle_pencere():
    def program_ekle():
        uye_id = combo_uyeler.get()
        secilen_program = combo_program.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına program bilgilerini ekle
        cursor.execute("INSERT INTO uye_program (Uye_ID, Program_ID) VALUES (%s, %s)", (uye_id, secilen_program))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Program başarıyla eklendi!")

        # Program Ekle Penceresi

    program_ekle_pencere = tk.Toplevel()
    program_ekle_pencere.title("Program Ekle")
    program_ekle_pencere.geometry("400x400+750+300")
    program_ekle_pencere.config(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(program_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()

    # get_all_members fonksiyonu ile üyeler tablosundan üye ID'lerini ve isimlerini al
    members = get_all_members()
    combo_uyeler = ttk.Combobox(program_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Program Seçim Kutusu
    label_program = tk.Label(program_ekle_pencere, text="Program Seç:",bg="black",fg="red")
    label_program.pack()

    # get_all_programs fonksiyonu ile programlar tablosundan program ID'lerini al
    programs = get_all_programs()
    combo_program = ttk.Combobox(program_ekle_pencere, values=programs)
    combo_program.pack()

    # Program Ekle Düğmesi
    btn_program_ekle = tk.Button(program_ekle_pencere, text="Program Ekle", command=program_ekle,bg="red")
    btn_program_ekle.pack(pady=10)


def antrenor_ekle_pencere():
    def antrenor_ekle():
        # Antrenör Ekleme Fonksiyonu
        uye_id = combo_uyeler.get()
        secilen_antrenor = combo_antrenor.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına antrenör bilgilerini ekle
        cursor.execute("INSERT INTO uye_antrenor (Uye_ID, Antrenorler_ID) VALUES (%s, %s)", (uye_id, secilen_antrenor))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Antrenör başarıyla eklendi!")

    # Antrenör Ekle Penceresi
    antrenor_ekle_pencere = tk.Toplevel()
    antrenor_ekle_pencere.title("Antrenör Ekle")
    antrenor_ekle_pencere.geometry("400x400+750+300")
    antrenor_ekle_pencere.configure(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(antrenor_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()

    # get_all_members fonksiyonu ile üyeler tablosundan üye ID'lerini ve isimlerini al
    members = get_all_members()
    combo_uyeler = ttk.Combobox(antrenor_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Antrenör Seçim Kutusu
    label_antrenor = tk.Label(antrenor_ekle_pencere, text="Antrenör:",bg="black",fg="red")
    label_antrenor.pack()

    # get_all_trainers fonksiyonu ile antrenorler tablosundan antrenör ID'lerini al
    trainers = get_all_trainers()
    combo_antrenor = ttk.Combobox(antrenor_ekle_pencere, values=trainers)
    combo_antrenor.pack()

    # Antrenör Ekle Düğmesi
    btn_antrenor_ekle = tk.Button(antrenor_ekle_pencere, text="Antrenör Ekle", command=antrenor_ekle,bg="red")
    btn_antrenor_ekle.pack(pady=10)


def diyetisyen_ekle_pencere():
    def diyetisyen_ekle():
        try:
            # Diyetisyen Ekleme Fonksiyonu
            uye_id = combo_uyeler.get()
            secilen_diyetisyen = combo_diyetisyen.get()

            # MySQL veritabanına bağlan
            conn = mysql.connector.connect(
                host="localhost",
                user="root",
                password="",
                database="burakPython"
            )
            cursor = conn.cursor()

            # Veritabanına diyetisyen bilgilerini ekle
            cursor.execute("INSERT INTO uye_diyetisyen (Uye_ID, Diyetisyen_ID) VALUES (%s, %s)",(uye_id, secilen_diyetisyen))
            conn.commit()

            # Veritabanı bağlantısını kapat
            conn.close()

            messagebox.showinfo("Başarılı", "Diyetisyen başarıyla eklendi!")

        except Exception as e:
            messagebox.showerror("Hata", "Diyetisyen eklenirken bir hata oluştu: " + str(e))

    # Diyetisyen Ekle Penceresi
    diyetisyen_ekle_pencere = tk.Toplevel()
    diyetisyen_ekle_pencere.title("Diyetisyen Ekle")
    diyetisyen_ekle_pencere.geometry("400x400+750+300")
    diyetisyen_ekle_pencere.configure(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(diyetisyen_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()

    # get_all_members fonksiyonu ile üyeler tablosundan üye ID'lerini ve isimlerini al
    members = get_all_members()
    combo_uyeler = ttk.Combobox(diyetisyen_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Diyetisyen Seçim Kutusu
    label_diyetisyen = tk.Label(diyetisyen_ekle_pencere, text="Diyetisyen:",bg="black",fg="red")
    label_diyetisyen.pack()

    # get_all_dietitians fonksiyonu ile diyetisyenler tablosundan diyetisyen ID'lerini al
    dietitians = get_all_dietitians()
    combo_diyetisyen = ttk.Combobox(diyetisyen_ekle_pencere, values=dietitians)
    combo_diyetisyen.pack()

    # Diyetisyen Ekle Düğmesi
    btn_diyetisyen_ekle = tk.Button(diyetisyen_ekle_pencere, text="Diyetisyen Ekle", command=diyetisyen_ekle,bg="red")
    btn_diyetisyen_ekle.pack(pady=10)



def diyet_ekle_pencere():
    def diyet_ekle():
        # Diyet Ekleme Fonksiyonu
        uye_id = combo_uyeler.get()
        secilen_diyet = combo_diyet.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına diyet bilgilerini ekle
        cursor.execute("INSERT INTO uye_diyet (Uye_ID, Diyet_ID) VALUES (%s, %s)", (uye_id, secilen_diyet))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Diyet başarıyla eklendi!")

    # Diyet Ekle Penceresi
    diyet_ekle_pencere = tk.Toplevel()
    diyet_ekle_pencere.title("Diyet Ekle")
    diyet_ekle_pencere.geometry("400x400+750+300")
    diyet_ekle_pencere.configure(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(diyet_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()

    # get_all_members fonksiyonu ile üyeler tablosundan üye ID'lerini ve isimlerini al
    members = get_all_members()
    combo_uyeler = ttk.Combobox(diyet_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Diyet Seçim Kutusu
    label_diyet = tk.Label(diyet_ekle_pencere, text="Diyet:",bg="black",fg="red")
    label_diyet.pack()

    # get_all_diets fonksiyonu ile diyet tablosundan diyet ID'lerini al
    diets = get_all_diets()
    combo_diyet = ttk.Combobox(diyet_ekle_pencere, values=diets)
    combo_diyet.pack()

    # Diyet Ekle Düğmesi
    btn_diyet_ekle = tk.Button(diyet_ekle_pencere, text="Diyet Ekle", command=diyet_ekle,bg="red")
    btn_diyet_ekle.pack(pady=10)

def ek_gida_ekle_pencere():
    def ek_gida_ekle():
        # Ek Gıda Ekleme Fonksiyonu
        uye_id = combo_uyeler.get()
        secilen_ek_gida = combo_ek_gida.get()

        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına ek gıda bilgilerini ekle
        cursor.execute("INSERT INTO uye_ek_gida (uye_id, gida_id) VALUES (%s, %s)", (uye_id, secilen_ek_gida))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Ek Gıda başarıyla eklendi!")

    # Ek Gıda Ekle Penceresi
    ek_gida_ekle_pencere = tk.Toplevel()
    ek_gida_ekle_pencere.title("Ek Gıda Ekle")
    ek_gida_ekle_pencere.geometry("400x400+750+300")
    ek_gida_ekle_pencere.configure(bg="black")

    # Üye Seçim Kutusu
    label_uyeler = tk.Label(ek_gida_ekle_pencere, text="Üye Seç:",bg="black",fg="red")
    label_uyeler.pack()
    members = get_all_members()
    combo_uyeler = ttk.Combobox(ek_gida_ekle_pencere, values=members)
    combo_uyeler.pack()

    # Ek Gıda Seçim Kutusu
    label_ek_gida = tk.Label(ek_gida_ekle_pencere, text="Ek Gıda:",bg="black",fg="red")
    label_ek_gida.pack()
    ek_gidalar = get_all_additional_foods()
    combo_ek_gida = ttk.Combobox(ek_gida_ekle_pencere, values=ek_gidalar)
    combo_ek_gida.pack()

    # Ek Gıda Ekle Düğmesi
    btn_ek_gida_ekle = tk.Button(ek_gida_ekle_pencere, text="Ek Gıda Ekle", command=ek_gida_ekle,bg="red")
    btn_ek_gida_ekle.pack(pady=10)

    # Pencereyi ve combo box'ları güncelle
    ek_gida_ekle_pencere.update()
    combo_uyeler.update()
    combo_ek_gida.update()

def antrenor_kayit_ekle():
    antrenor_adi = entry_antrenor_adi.get()
    antrenor_soyadi = entry_antrenor_soyadi.get()
    sifre = entry_sifre.get()

    if sifre == "Proje":
        # MySQL veritabanına bağlan
        conn = mysql.connector.connect(
            host="localhost",
            user="root",
            password="",
            database="burakPython"
        )
        cursor = conn.cursor()

        # Veritabanına antrenör kayıt bilgilerini ekle
        cursor.execute("INSERT INTO antrenorler (Antrenorler_Ad, Antrenorler_Soyad) VALUES (%s, %s)", (antrenor_adi, antrenor_soyadi))
        conn.commit()

        # Veritabanı bağlantısını kapat
        conn.close()

        messagebox.showinfo("Başarılı", "Antrenör kaydı başarıyla eklendi!")
        antrenor_kayit_pencere.destroy()  # Pencereyi kapat

    else:
        messagebox.showerror("Hata", "Şifre uyumsuz!")

def antrenor_kayit_penceresi():
    global antrenor_kayit_pencere, entry_antrenor_adi, entry_antrenor_soyadi, entry_sifre
    antrenor_kayit_pencere = tk.Toplevel(root)
    antrenor_kayit_pencere.title("Antrenör Kayıt")
    antrenor_kayit_pencere.geometry("400x250+750+300")
    antrenor_kayit_pencere.configure(bg="black")

    label_antrenor_adi = tk.Label(antrenor_kayit_pencere, text="Antrenör Adı:",bg="black",fg="red")
    label_antrenor_adi.pack()
    entry_antrenor_adi = tk.Entry(antrenor_kayit_pencere)
    entry_antrenor_adi.pack()

    label_antrenor_soyadi = tk.Label(antrenor_kayit_pencere, text="Antrenör Soyadı:",bg="black",fg="red")
    label_antrenor_soyadi.pack()
    entry_antrenor_soyadi = tk.Entry(antrenor_kayit_pencere)
    entry_antrenor_soyadi.pack()

    label_sifre = tk.Label(antrenor_kayit_pencere, text="Şifre:",bg="black",fg="red")
    label_sifre.pack()
    entry_sifre = tk.Entry(antrenor_kayit_pencere, show="*",bg="black",fg="red")
    entry_sifre.pack()

    btn_kayit = tk.Button(antrenor_kayit_pencere, text="Kayıt Yap", command=antrenor_kayit_ekle,bg="red")
    btn_kayit.pack(pady=10)




# Ana Ekran
root = tk.Tk()
root.title("Giriş Ekranı")
root.geometry("400x400+750+300")
root.configure(bg="black")

# Ad ve Soyad Giriş Kutuları
label_adi = tk.Label(root, text="Ad",bg="black",fg="red",font="12")
label_adi.pack()
entry_adi = tk.Entry(root)
entry_adi.pack()

label_soyadi = tk.Label(root, text="Şifre",bg="black",fg="red",font="12")
label_soyadi.pack()
entry_soyadi = tk.Entry(root,show="*")
entry_soyadi.pack()

# Giriş Düğmesi
btn_giris = tk.Button(root, text="Giriş Yap", command=giris_kontrol,bg="red",width=8,height=2)
btn_giris.pack(pady=10)

# Antrenör Kayıt Düğmesi
btn_antrenor_kayit = tk.Button(root, text="Antrenör Kayıt", command=antrenor_kayit_penceresi,bg="red",width=12,height=2)
btn_antrenor_kayit.pack(pady=10)

root.mainloop()

