import type { Metadata } from 'next';
import './globals.css';

export const metadata: Metadata = {
  title: 'Portal Data Scraping STIKOM',
  description: 'Hasil scraping berita Detik Inet - Praktikum Data Scraping STIKOM PGRI Banyuwangi',
};

export default function RootLayout({
  children,
}: Readonly<{
  children: React.ReactNode;
}>) {
  return (
    <html lang="id">
      <body>{children}</body>
    </html>
  );
}