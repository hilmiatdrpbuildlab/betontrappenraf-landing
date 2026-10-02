# Color Palette: Betontrappen Raf Geerts

Dokumen ini berisi spesifikasi palet warna yang diekstrak dari situs web [Betontrappen Raf Geerts](https://www.betontrappenraf.be/).

---

## 🎨 Ringkasan Warna

| Peran Warna | Hex Code | RGB | Visual | Deskripsi & Penggunaan |
| :--- | :--- | :--- | :---: | :--- |
| **Primary Accent** | `#E83E4D` | `rgb(232, 62, 77)` | 🔴 | Warna aksen utama (branding "BETONTRAPPEN", tombol CTA, garis penekanan). |
| **Dark Neutral** | `#000000` | `rgb(0, 0, 0)` | ⬛ | Warna teks utama, header, dan elemen navigasi. |
| **Concrete Gray** | `#8A8F94` | `rgb(138, 143, 148)` | 🔘 | Warna sekunder representasi material beton, digunakan untuk teks pendukung. |
| **Light Background** | `#FFFFFF` | `rgb(255, 255, 255)` | ⚪ | Warna latar belakang area konten utama. |

---

## 💻 Kode Variabel CSS

Anda dapat menggunakan potongan kode CSS berikut untuk mengimplementasikan palet warna ini ke dalam proyek Anda:

```css
:root {
  /* Primary Colors */
  --color-primary-red: #E83E4D;
  --color-dark-neutral: #000000;
  
  /* Secondary & Background Colors */
  --color-concrete-gray: #8A8F94;
  --color-bg-light: #FFFFFF;
}

/* Contoh Penerapan Elemen */
body {
  background-color: var(--color-bg-light);
  color: var(--color-dark-neutral);
  font-family: system-ui, -apple-system, sans-serif;
}

.btn-primary {
  background-color: var(--color-primary-red);
  color: var(--color-bg-light);
  border: none;
  padding: 0.75rem 1.5rem;
  border-radius: 4px;
}

.text-muted {
  color: var(--color-concrete-gray);
}
```

---

## 📐 Rekomendasi Kombinasi Kontras

- **Teks Hitam (`#000000`) di atas Latar Putih (`#FFFFFF`)**: Memiliki kontras sangat tinggi (21:1), sangat mudah dibaca.
- **Teks Putih (`#FFFFFF`) di atas Tombol Merah (`#E83E4D`)**: Memenuhi standar keterbacaan WCAG AA untuk elemen interaktif dan tombol call-to-action.