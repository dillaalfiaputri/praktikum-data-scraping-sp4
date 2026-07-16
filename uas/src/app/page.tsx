'use client';

import { useEffect, useState } from 'react';
import { Inter } from 'next/font/google';
import LastUpdated from './components/LastUpdated';

const inter = Inter({ subsets: ['latin'], weight: ['400', '600'] });

// Helper to safely parse and format date strings or timestamps
function formatDate(value: any): string {
  let date = new Date(value);

  if (isNaN(date.getTime())) {
    // Try treating as Unix timestamp (seconds)
    const numeric = Number(value);
    if (!isNaN(numeric)) {
      date = new Date(numeric * 1000);
    }
  }

  if (isNaN(date.getTime())) {
    return 'Tanggal tidak valid';
  }

  return date.toLocaleDateString('id-ID');
}

export default function BeritaPage() {
  const [daftarBerita, setDaftarBerita] = useState([]);
  const [loading, setLoading] = useState(true);
  const [selectedBerita, setSelectedBerita] = useState<any>(null);
  const [currentPage, setCurrentPage] = useState(1);
  const itemsPerPage = 9; // 3 columns x 3 rows per page

  // Mengambil data dari API secara otomatis saat halaman dibuka
  useEffect(() => {
    fetch('/api/berita')
      .then((res) => res.json())
      .then((json) => {
        if (json.success) {
          setDaftarBerita(json.data);
        }
        setLoading(false);
      })
      .catch((err) => {
        console.error('Gagal mengambil data API:', err);
        setLoading(false);
      });
  }, []);

  if (loading) {
    return (
      <div className="flex justify-center items-center min-h-screen bg-gray-50">
        <p className="text-xl font-semibold text-blue-600 animate-pulse">Memuat Data Berita STIKOM...</p>
      </div>
    );
  }

  return (
    <div className={`${inter.className} min-h-screen bg-gradient-to-br from-indigo-100 via-purple-50 to-pink-50 flex flex-col`}>
      {/* HEADER */}
      <header className="bg-indigo-800 text-white shadow-lg p-4 flex items-center justify-between">
        <div className="container mx-auto flex items-center justify-between">
          <h1 className="text-xl font-bold tracking-wider">PORTAL DATA SCRAPING STIKOM</h1>
          <span className="bg-blue-800 text-xs px-3 py-1.5 rounded-full font-mono">XAMPP &amp; MySQL Active</span>
          <LastUpdated apiUrl="/api/berita" />
        </div>
      </header>

      {/* MAIN CONTENT */}
      <main className="flex-grow container mx-auto p-6">
        <h2 className="text-2xl font-bold text-gray-800 mb-6 border-b-2 border-blue-500 pb-2 inline-block">
          Hasil Scraping Detik Inet Terbaru
        </h2>

        {/* === TUGAS 1: DASHBOARD STATISTIK RINGKAS === */}
        <div className="bg-blue-50 border-l-4 border-blue-600 p-4 mb-6 rounded-r-lg shadow-sm flex items-center justify-between">
          <div>
            <h3 className="text-sm font-semibold text-blue-800 uppercase tracking-wider">Statistik Storage</h3>
            <p className="text-2xl font-black text-blue-900">
              {daftarBerita.length} <span className="text-sm font-normal text-gray-600">Berita Terarsip</span>
            </p>
          </div>
          <div className="text-xs text-gray-500 text-right">
            Status Database: <span className="text-green-600 font-bold">Sinkron</span> <br />
            Engine Data: <span className="text-blue-600 font-bold">Next API Node.js</span>
          </div>
        </div>

        {daftarBerita.length === 0 ? (
          <div className="bg-white p-8 rounded-lg shadow-md text-center">
            <p className="text-gray-600 text-lg">Belum ada data di database. Pastikan engine Python Anda sudah dijalankan.</p>
          </div>
        ) : (
          /* GRID SYSTEM: 1 Kolom di HP, 2 Kolom di Tablet, 3 Kolom di Laptop/PC */
          <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-3 gap-6">
            {daftarBerita.slice((currentPage - 1) * itemsPerPage, currentPage * itemsPerPage).map((berita: any) => (
              <div key={berita.id} className="cursor-pointer" onClick={() => setSelectedBerita(berita)}>
                <div className="bg-white/90 rounded-xl shadow-lg overflow-hidden hover:shadow-2xl hover:scale-105 transition-all duration-300 flex flex-col backdrop-blur-sm">
                  {/* Bagian Gambar Berita */}
                  <div className="h-48 w-full bg-gray-200 relative">
                    {berita.url_gambar ? (
                      <img
                        src={
                          berita.url_gambar?.startsWith("http")
                            ? berita.url_gambar
                            : berita.url_gambar
                        }
                        alt={berita.judul}
                        className="w-full h-full object-cover"
                      />
                    ) : (
                      <div className="w-full h-full flex items-center justify-center text-gray-400">
                        No Image Available
                      </div>
                    )}
                  </div>

                  {/* Konten Teks Kartu */}
                  <div className="p-5 flex-grow flex flex-col justify-between">
                    <div>
                      {/* === TUGAS 2: BADGE KATEGORI KONDISIONAL === */}
                      <span
                        className={`inline-block text-xs font-bold px-2.5 py-1 rounded uppercase mb-3 ${
                          berita.kategori === 'Teknologi'
                            ? 'bg-green-100 text-green-800 border border-green-200'
                            : 'bg-blue-100 text-blue-800 border border-blue-200'
                        }`}
                      >
                        {berita.kategori || 'Umum'}
                      </span>
                      <h3 className="font-bold text-gray-900 text-md leading-snug line-clamp-2 hover:text-indigo-600 transition-colors duration-200">
                        {berita.judul}
                      </h3>
                    </div>

                    <div className="mt-5 pt-3 border-t border-gray-100 flex items-center justify-between">
                      <span className="text-xs text-gray-400 font-mono">
                        {formatDate(berita.tanggal_scraping)}
                      </span>
                      <span className="text-sm text-indigo-600 font-bold hover:text-indigo-800 inline-flex items-center transition-colors duration-200">
                        Buka Sumber →
                      </span>
                    </div>
                  </div>
                </div>
              </div>
            ))}
          </div>
        )}
      </main>

      {/* PAGINATION */}
      {daftarBerita.length > itemsPerPage && (
        <div className="flex justify-center items-center space-x-4 mt-6">
          <button
            className="px-5 py-2 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors duration-200"
            onClick={() => setCurrentPage((prev) => Math.max(prev - 1, 1))}
            disabled={currentPage === 1}
          >
            ← Prev
          </button>
          <span className="text-gray-800 font-medium">
            Page {currentPage} of {Math.ceil(daftarBerita.length / itemsPerPage)}
          </span>
          <button
            className="px-5 py-2 bg-indigo-600 text-white rounded-full hover:bg-indigo-700 disabled:opacity-40 disabled:cursor-not-allowed transition-colors duration-200"
            onClick={() => setCurrentPage((prev) => Math.min(prev + 1, Math.ceil(daftarBerita.length / itemsPerPage)))}
            disabled={currentPage === Math.ceil(daftarBerita.length / itemsPerPage)}
          >
            Next →
          </button>
        </div>
      )}

      {/* MODAL DETAIL BERITA */}
      {selectedBerita && (
        <div className="fixed inset-0 bg-black/50 backdrop-blur-sm flex items-center justify-center z-50 p-4">
          <div className="bg-white rounded-2xl max-w-lg w-full p-6 relative max-h-[90vh] overflow-y-auto shadow-2xl">
            <button
              className="absolute top-4 right-4 text-gray-400 hover:text-gray-600 bg-gray-100 p-1 rounded-full"
              onClick={() => setSelectedBerita(null)}
            >
              ✖
            </button>
            <div className="h-64 w-full bg-gray-200 mb-4 flex-shrink-0 rounded-lg overflow-hidden">
              <img
                src={selectedBerita.url_gambar}
                alt={selectedBerita.judul}
                className="w-full h-full object-cover"
              />
            </div>
            <h2 className="font-bold text-xl mb-2 text-gray-900">{selectedBerita.judul}</h2>
            <p className="text-sm text-gray-500 mb-2">{selectedBerita.kategori || 'Umum'}</p>
            <p className="text-xs text-gray-400 mb-4">{formatDate(selectedBerita.tanggal_scraping)}</p>
            {selectedBerita.isi_berita && <p className="text-gray-700 mb-4 leading-relaxed">{selectedBerita.isi_berita}</p>}
            <a
              href={selectedBerita.url_link}
              target="_blank"
              rel="noopener noreferrer"
              className="mt-4 inline-block text-indigo-600 font-medium hover:text-indigo-800 transition-colors duration-200"
            >
              Buka Sumber →
            </a>
          </div>
        </div>
      )}

      {/* === TUGAS 3: FOOTER DENGAN IDENTITAS MAHASISWA === */}
      <footer className="bg-gray-800 text-gray-400 text-center p-4 text-xs border-t border-gray-700">
        <div className="container mx-auto">
          <p>&copy; {new Date().getFullYear()} Praktikum Data Scraping Full-Stack - S1 Sistem Informasi STIKOM PGRI Banyuwangi</p>
          <p className="mt-1 font-mono text-blue-400 text-[11px]">
            Developer: Dilla Alfia Putri | NIM: 1124102172 | Program Studi S1 Sistem Informasi
          </p>
        </div>
      </footer>
    </div>
  );
}