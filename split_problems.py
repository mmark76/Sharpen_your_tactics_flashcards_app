import fitz
from PIL import Image
import os

# Φάκελος που περιέχει τα 134 PDFs
INPUT_DIR = r"C:\Users\marke\Desktop\Personal\Markellos\my projects\Sharpen Your Tactics – Flashcards\split_pages"

# Φάκελος εξόδου
OUTPUT_DIR = os.path.join(INPUT_DIR, "problems")
os.makedirs(OUTPUT_DIR, exist_ok=True)

print(f"Output directory: {OUTPUT_DIR}")  # Προσωρινή εκτύπωση για έλεγχο

# Πάρε όλα τα PDF με σειρά
files = sorted([
    f for f in os.listdir(INPUT_DIR)
    if f.lower().endswith(".pdf")
])

problem_no = 1

for file in files:
    path = os.path.join(INPUT_DIR, file)
    doc = fitz.open(path)

    # κάθε αρχείο έχει 1 σελίδα
    page = doc[0]
    pix = page.get_pixmap(dpi=250)
    img = Image.frombytes("RGB", [pix.width, pix.height], pix.samples)

    W, H = img.size
    cols, rows = 4, 3                 # 4x3 = 12 διαγράμματα ανά σελίδα
    cell_w = W // cols
    cell_h = H // rows

    for r in range(rows):
        for c in range(cols):
            left   = c * cell_w
            top    = r * cell_h
            right  = left + cell_w
            bottom = top + cell_h

            crop = img.crop((left, top, right, bottom))
            crop = crop.resize((120, 120), Image.LANCZOS)

            out_name = f"problem_{problem_no:04d}.png"
            out_path = os.path.join(OUTPUT_DIR, out_name)
            crop.save(out_path)

            print(f"Saved: {out_name}")  # Εκτύπωση για κάθε εικόνα που αποθηκεύεται

            problem_no += 1

print(f"ΤΕΛΟΣ! Δημιουργήθηκαν προβλήματα μέχρι: {problem_no - 1}")
