"use client";

import { useEffect, useState } from "react";

/**
 * Komponen "Terakhir Diperbarui"
 * -------------------------------
 * Menampilkan waktu scraping dari baris data PALING ATAS (data terbaru)
 * yang dikembalikan oleh API Route Next.js (Pertemuan 6).
 *
 * Asumsi: API kalian (misal /api/berita) mengembalikan array JSON berita
 * yang sudah diurutkan terbaru di indeks [0], dengan field "waktu_scraping".
 * Jika field/nama endpoint kalian berbeda, sesuaikan `apiUrl` dan
 * `data[0].waktu_scraping` di bawah.
 */

interface BeritaItem {
  tanggal_scraping: string;
  [key: string]: unknown;
}

export default function LastUpdated({ apiUrl = "/api/berita" }: { apiUrl?: string }) {
  const [lastUpdate, setLastUpdate] = useState<string | null>(null);
  const [loading, setLoading] = useState(true);

  const fetchLastUpdate = async () => {
    try {
      const res = await fetch(apiUrl, { cache: "no-store" });
      const json = await res.json();
      const data: BeritaItem[] = json?.data ?? [];

      if (Array.isArray(data) && data.length > 0 && data[0].tanggal_scraping) {
        setLastUpdate(data[0].tanggal_scraping);
      }
    } catch (err) {
      console.error("Gagal mengambil waktu update terakhir:", err);
    } finally {
      setLoading(false);
    }
  };

  useEffect(() => {
    fetchLastUpdate();
    // Cek ulang otomatis setiap 30 detik agar penanda ikut ter-update
    const interval = setInterval(fetchLastUpdate, 30000);
    return () => clearInterval(interval);
  }, []);

  const formatWaktu = (isoString: string) => {
    const date = new Date(isoString);
    return date.toLocaleString("id-ID", {
      dateStyle: "medium",
      timeStyle: "medium",
    });
  };

  return (
    <div className="flex items-center gap-2 rounded-lg bg-slate-100 px-4 py-2 text-sm text-slate-700 shadow-sm dark:bg-slate-800 dark:text-slate-200">
      <span className="relative flex h-2 w-2">
        <span className="absolute inline-flex h-full w-full animate-ping rounded-full bg-green-400 opacity-75"></span>
        <span className="relative inline-flex h-2 w-2 rounded-full bg-green-500"></span>
      </span>
      {loading ? (
        <span>Memuat waktu pembaruan...</span>
      ) : lastUpdate ? (
        <span>
          Terakhir diperbarui otomatis: <b>{formatWaktu(lastUpdate)}</b>
        </span>
      ) : (
        <span>Belum ada data pembaruan.</span>
      )}
    </div>
  );
}