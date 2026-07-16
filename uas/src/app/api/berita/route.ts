import { NextResponse } from 'next/server';
import { pool } from '../../../lib/db';

export async function GET() {
  try {
    const [rows] = await pool.query(
      'SELECT * FROM tbl_berita ORDER BY tanggal_scraping DESC'
    );

    return NextResponse.json({
      success: true,
      data: rows,
    });
  } catch (error) {
    console.error('Database error:', error);

    return NextResponse.json(
      {
        success: false,
        message: 'Gagal mengambil data dari database',
      },
      { status: 500 }
    );
  }
}