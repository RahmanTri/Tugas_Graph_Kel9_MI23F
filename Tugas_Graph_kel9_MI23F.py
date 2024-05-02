# deklarasi class peta
class Peta:

    # deklarasi constructor daftar kota
    def __init__(self):
        self.daftarkota = {}
    
    # membuat fungsi untuk menambahkan kota
    def tambahkanKota(self,kota,):
        # cek apakah kota yang di tambahkan sudah ada atau belum
        if kota not in self.daftarkota:
            self.daftarkota[kota] = []
            return True
        # jika sudah ada maka return ke false
        return False
    
    # membuat fungsi untuk menghapus kota
    def hapusKota(self,kotaDihapus):
        # mengecek apakah kota yang akan dihapus adda pada dictionary daftar kota atau tidak
        if kotaDihapus in self.daftarkota:
            # melakukan iterasi terhadap daftar kota untuk mencari kota yang akan dihapus pada kota lain
            for kotalain in self.daftarkota:
                # jika kota ditemukan
                if kotaDihapus in self.daftarkota[kotalain]:
                    #akses jalan dihapus
                    self.daftarkota[kotalain].remove(kotaDihapus)
            # dan terakhir hapus kota dari daftarkota
            del self.daftarkota[kotaDihapus]
            return True
        return False
    
    # membuat fungsi untuk menambahkan jalan antar kota
    def tambahkanJalan(self,kota1,kota2,):
        # cek apakah kkedua kota ada pada daftar kota atau tidak
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            # jika ada, maka masukkan kota 1 ke list kota 2 dan sebaliknya
            self.daftarkota[kota2].append(kota1)
            self.daftarkota[kota1].append(kota2)
            return True
        return False
    
    # membuat fungsi untuuk menghapus jalan antar kota
    def hapusJalan(self,kota1,kota2):
        # cek apakah kedua kota ada pada daftar kota atau tidak
        if kota1 in self.daftarkota and kota2 in self.daftarkota:
            # jika ada, maka hapus kota 1 pada list kota 2 dan sebaliknya
               self.daftarkota[kota2].remove(kota1)
            self.daftarkota[kota1].remove(kota2)
            return True
        return False

    # membuat fungsi untuk mengeprint daftar kota dan kota yang memiliki akses jalan ke kota lain
    def print(self):
        print('Berikut merupakan daftar kota yang terdaftar pada sistem peta:')
        # melakukan iterasi pada daftarkota untuk mendapatkan daftar kota yang telah terdaftar
        for kota in self.daftarkota:
            # print nama kota
            print("-", kota)
            # cek apakah list jalan kota kosong atau tidak
            if self.daftarkota[kota]:
                # jika list jalan terdapat nama kota, maka print :
                print("  Akses ke kota lain:")
                # dan iterasi list jalan yang ada pada kota dan print jalan aksesnya
                for jalan in self.daftarkota[kota]:
                    print("  *", jalan)
            # dan jika list kosong, maka print :
            else:
                print("  Tidak memiliki akses ke kota lain")




# membuat list peta
PetaJepang = Peta()

# tambahkan kota
PetaJepang.tambahkanKota("Ueno")
PetaJepang.tambahkanKota("Shimonita")
PetaJepang.tambahkanKota("Annaka")
PetaJepang.tambahkanKota("Takasaki")
PetaJepang.tambahkanKota("Ogano")
PetaJepang.tambahkanKota("Chichibu")
PetaJepang.tambahkanKota("Minano")
PetaJepang.tambahkanKota("Nagatoro")
PetaJepang.tambahkanKota("Yorii")
PetaJepang.tambahkanKota("Honjo")
PetaJepang.tambahkanKota("Isesaki")
PetaJepang.tambahkanKota("Maebashi")

# tambahkan jalan
PetaJepang.tambahkanJalan("Shimonita","Annaka")
