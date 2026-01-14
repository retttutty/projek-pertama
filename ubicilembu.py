import json
import os
from datetime import datetime
from pathlib import Path

class ManajemenKeuangan:
    def __init__(self, nama_file='keuangan.json'):
        self.nama_file = nama_file
        self.data = self.muat_data()
    
    def muat_data(self):
        """Memuat data dari file JSON"""
        if os.path.exists(self.nama_file):
            try:
                with open(self.nama_file, 'r', encoding='utf-8') as f:
                    return json.load(f)
            except:
                return {'pemasukan': [], 'pengeluaran': []}
        return {'pemasukan': [], 'pengeluaran': []}
    
    def simpan_data(self):
        """Menyimpan data ke file JSON"""
        with open(self.nama_file, 'w', encoding='utf-8') as f:
            json.dump(self.data, f, ensure_ascii=False, indent=2)
    
    def tambah_pemasukan(self, jumlah, keterangan, tanggal=None):
        """Menambah data pemasukan"""
        if tanggal is None:
            tanggal = datetime.now().strftime('%Y-%m-%d')
        
        pemasukan = {
            'tanggal': tanggal,
            'jumlah': jumlah,
            'keterangan': keterangan
        }
        self.data['pemasukan'].append(pemasukan)
        self.simpan_data()
        print(f"✓ Pemasukan '{keterangan}' sebesar Rp {jumlah:,.0f} berhasil ditambahkan")
    
    def tambah_pengeluaran(self, jumlah, keterangan, tanggal=None):
        """Menambah data pengeluaran"""
        if tanggal is None:
            tanggal = datetime.now().strftime('%Y-%m-%d')
        
        pengeluaran = {
            'tanggal': tanggal,
            'jumlah': jumlah,
            'keterangan': keterangan
        }
        self.data['pengeluaran'].append(pengeluaran)
        self.simpan_data()
        print(f"✓ Pengeluaran '{keterangan}' sebesar Rp {jumlah:,.0f} berhasil ditambahkan")
    
    def hitung_total_pemasukan(self):
        """Menghitung total pemasukan"""
        return sum(item['jumlah'] for item in self.data['pemasukan'])
    
    def hitung_total_pengeluaran(self):
        """Menghitung total pengeluaran"""
        return sum(item['jumlah'] for item in self.data['pengeluaran'])
    
    def hitung_saldo(self):
        """Menghitung saldo (pemasukan - pengeluaran)"""
        return self.hitung_total_pemasukan() - self.hitung_total_pengeluaran()
    
    def tampilkan_ringkasan(self):
        """Menampilkan ringkasan keuangan bulanan"""
        total_pemasukan = self.hitung_total_pemasukan()
        total_pengeluaran = self.hitung_total_pengeluaran()
        saldo = self.hitung_saldo()
        
        print("\n" + "="*60)
        print("        RINGKASAN KEUANGAN BULANAN".center(60))
        print("="*60)
        print(f"Total Pemasukan    : Rp {total_pemasukan:>15,.0f}")
        print(f"Total Pengeluaran  : Rp {total_pengeluaran:>15,.0f}")
        print("-"*60)
        
        if saldo >= 0:
            print(f"Saldo (Surplus)    : Rp {saldo:>15,.0f}")
        else:
            print(f"Saldo (Defisit)    : Rp {saldo:>15,.0f}")
        print("="*60 + "\n")
    
    def tampilkan_detail_pemasukan(self):
        """Menampilkan detail semua pemasukan"""
        if not self.data['pemasukan']:
            print("\nTidak ada data pemasukan\n")
            return
        
        print("\n" + "="*80)
        print("DETAIL PEMASUKAN".center(80))
        print("="*80)
        print(f"{'No':<4} {'Tanggal':<12} {'Keterangan':<30} {'Jumlah':>20}")
        print("-"*80)
        
        total = 0
        for i, item in enumerate(self.data['pemasukan'], 1):
            jumlah = item['jumlah']
            total += jumlah
            print(f"{i:<4} {item['tanggal']:<12} {item['keterangan']:<30} Rp {jumlah:>18,.0f}")
        
        print("-"*80)
        print(f"{'TOTAL':<46} Rp {total:>18,.0f}")
        print("="*80 + "\n")
    
    def tampilkan_detail_pengeluaran(self):
        """Menampilkan detail semua pengeluaran"""
        if not self.data['pengeluaran']:
            print("\nTidak ada data pengeluaran\n")
            return
        
        print("\n" + "="*80)
        print("DETAIL PENGELUARAN".center(80))
        print("="*80)
        print(f"{'No':<4} {'Tanggal':<12} {'Keterangan':<30} {'Jumlah':>20}")
        print("-"*80)
        
        total = 0
        for i, item in enumerate(self.data['pengeluaran'], 1):
            jumlah = item['jumlah']
            total += jumlah
            print(f"{i:<4} {item['tanggal']:<12} {item['keterangan']:<30} Rp {jumlah:>18,.0f}")
        
        print("-"*80)
        print(f"{'TOTAL':<46} Rp {total:>18,.0f}")
        print("="*80 + "\n")
    
    def hapus_pemasukan(self, index):
        """Menghapus data pemasukan berdasarkan index"""
        if 0 <= index < len(self.data['pemasukan']):
            item = self.data['pemasukan'].pop(index)
            self.simpan_data()
            print(f"✓ Pemasukan '{item['keterangan']}' berhasil dihapus")
        else:
            print("✗ Index tidak valid")
    
    def hapus_pengeluaran(self, index):
        """Menghapus data pengeluaran berdasarkan index"""
        if 0 <= index < len(self.data['pengeluaran']):
            item = self.data['pengeluaran'].pop(index)
            self.simpan_data()
            print(f"✓ Pengeluaran '{item['keterangan']}' berhasil dihapus")
        else:
            print("✗ Index tidak valid")


def menu_utama():
    """Menampilkan menu utama aplikasi"""
    keuangan = ManajemenKeuangan()
    
    while True:
        print("\n" + "="*50)
        print("      APLIKASI MANAJEMEN KEUANGAN".center(50))
        print("="*50)
        print("1. Tambah Pemasukan")
        print("2. Tambah Pengeluaran")
        print("3. Lihat Ringkasan Keuangan")
        print("4. Lihat Detail Pemasukan")
        print("5. Lihat Detail Pengeluaran")
        print("6. Hapus Pemasukan")
        print("7. Hapus Pengeluaran")
        print("8. Keluar")
        print("="*50)
        
        pilihan = input("Pilih menu (1-8): ").strip()
        
        if pilihan == '1':
            print("\n--- Tambah Pemasukan ---")
            try:
                jumlah = float(input("Masukkan jumlah pemasukan (Rp): "))
                keterangan = input("Masukkan keterangan: ").strip()
                tanggal = input("Masukkan tanggal (YYYY-MM-DD) [Enter untuk hari ini]: ").strip()
                
                if not keterangan:
                    print("✗ Keterangan tidak boleh kosong")
                    continue
                
                if jumlah <= 0:
                    print("✗ Jumlah harus lebih dari 0")
                    continue
                
                keuangan.tambah_pemasukan(jumlah, keterangan, tanggal if tanggal else None)
            except ValueError:
                print("✗ Input tidak valid. Gunakan angka untuk jumlah.")
        
        elif pilihan == '2':
            print("\n--- Tambah Pengeluaran ---")
            try:
                jumlah = float(input("Masukkan jumlah pengeluaran (Rp): "))
                keterangan = input("Masukkan keterangan: ").strip()
                tanggal = input("Masukkan tanggal (YYYY-MM-DD) [Enter untuk hari ini]: ").strip()
                
                if not keterangan:
                    print("✗ Keterangan tidak boleh kosong")
                    continue
                
                if jumlah <= 0:
                    print("✗ Jumlah harus lebih dari 0")
                    continue
                
                keuangan.tambah_pengeluaran(jumlah, keterangan, tanggal if tanggal else None)
            except ValueError:
                print("✗ Input tidak valid. Gunakan angka untuk jumlah.")
        
        elif pilihan == '3':
            keuangan.tampilkan_ringkasan()
        
        elif pilihan == '4':
            keuangan.tampilkan_detail_pemasukan()
        
        elif pilihan == '5':
            keuangan.tampilkan_detail_pengeluaran()
        
        elif pilihan == '6':
            print("\n--- Hapus Pemasukan ---")
            keuangan.tampilkan_detail_pemasukan()
            try:
                index = int(input("Masukkan nomor pemasukan yang ingin dihapus: ")) - 1
                keuangan.hapus_pemasukan(index)
            except ValueError:
                print("✗ Input tidak valid")
        
        elif pilihan == '7':
            print("\n--- Hapus Pengeluaran ---")
            keuangan.tampilkan_detail_pengeluaran()
            try:
                index = int(input("Masukkan nomor pengeluaran yang ingin dihapus: ")) - 1
                keuangan.hapus_pengeluaran(index)
            except ValueError:
                print("✗ Input tidak valid")
        
        elif pilihan == '8':
            print("\nTerima kasih telah menggunakan Aplikasi Manajemen Keuangan!")
            break
        
        else:
            print("✗ Pilihan tidak valid. Silakan pilih 1-8")


if __name__ == "__main__":
    menu_utama()
