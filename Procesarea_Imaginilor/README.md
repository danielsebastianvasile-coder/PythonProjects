# Editor Imagini PRO

##  Descriere proiect
**Editor Imagini PRO** este un mini-editor de imagini dezvoltat în Python folosind `customtkinter` și `PIL`/`OpenCV`.
Scopul proiectului este de a oferi utilizatorului un instrument rapid și intuitiv pentru editarea imaginilor, aplicarea de ajustări, filtre și unelte avansate, toate într-un UI modern și prietenos.

Proiectul oferă funcționalități precum filtre predefinit, crop, rotire, flip, ajustări de luminozitate, contrast, saturație, tonuri luminoase/întunecate, claritate, vinietă și un Magic Eraser care elimină obiecte nedorite din imagini.

---

##  Obiective
- Import și export imagini în diverse formate ("*.png *.jpg *.jpeg *.jfif *.webp *.bmp")
- Aplicarea de ajustări individuale sau preseturi de filtre
- Implementarea unui istoric pentru undo/redo și reset imagine
- Crop și transformări (rotire, flip)
- Magic Eraser folosind OpenCV pentru eliminarea selectivă a obiectelor
- Interfață modernă și intuitivă

---

##  Funcționalități principale

| Funcționalitate                | Descriere                                                                           |
|--------------------------------|-------------------------------------------------------------------------------------|
| **Import / Salvare imagine**    | Încarcă imagini și le salvează după editare                                        |
| **Ajustări imagine**            | Luminozitate, contrast, saturație, tonuri luminoase/întunecate, claritate, vinietă |
| **Filtre preset**               | Original, Intens, Dramatic, Mono, Noir                                             |
| **Transformări**                | Crop, rotire 90°, flip orizontal și vertical                                       |
| **Magic Eraser **               | Elimină obiecte selectate folosind masca și funcția `cv2.inpaint`                  |
| **Istoric**                     | Undo, redo, reset image                                                            |
| **Comparare imagine**           | Apăsare lungă pentru a vedea imaginea originală                                    |
| **UI modern**                   | Tabs pentru ajustări, filtre și unelte, slidere și switch-uri                      |

---

##  Scenariu de utilizare
1. **Import**: Utilizatorul selectează o imagine din calculator.
2. **Ajustări și filtre**: Ajustează luminozitatea, contrastul, saturația sau aplică filtre preset.
3. **Transformări**: Poate decupa, roti sau face flip imaginii.
4. **Magic Eraser**: Selectează zona nedorită și o elimină inteligent.
5. **Comparare**: Apasă lung pe butonul "Apasă lung pt. Original" pentru a compara cu imaginea inițială.
6. **Salvare**: Salvează imaginea finală.

---

##  Fundamente teoretice

### Ajustări
- **Luminozitate**: Modifică nivelul mediu de gri al imaginii
- **Contrast**: Crește diferența dintre zonele luminoase și întunecate
- **Saturație**: Controlează intensitatea culorilor
- **Tonuri luminoase / întunecate**: Ajustează zonele luminoase sau întunecate independent
- **Claritate**: Folosește `ImageEnhance.Sharpness` pentru a accentua detalii
- **Vinietă**: Creează un efect de întunecare sau iluminare la marginea imaginii

### Filtre preset
- Combină ajustări de luminozitate, contrast și saturație pentru a crea efecte vizuale rapide

### Magic Eraser
- Folosește masca desenată de utilizator și `cv2.inpaint` pentru a elimina obiecte selectate inteligent, reconstruind pixelii din jur

---

##  Tehnologii folosite
- **Python 3.x**
- **customtkinter** - UI modern și responsive
- **Pillow (PIL)** - Procesare și manipulare imagini
- **OpenCV (cv2)** - Magic Eraser (inpainting)
- **numpy** - Conversie între imagini PIL și OpenCV



