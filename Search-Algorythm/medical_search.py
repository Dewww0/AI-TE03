
from collections import deque

# ==================================================
# MEDICAL DIAGNOSIS - SEARCH ALGORITHM
# Metode: Breadth-First Search (BFS) dan
#         Depth-First Search (DFS)
# ==================================================

# Pohon diagnosis sederhana untuk keperluan edukasi.
# Setiap kondisi mempunyai daftar gejala yang terkait.
MEDICAL_TREE = {
    "Medical Diagnosis": [
        "Gangguan Pernapasan",
        "Gangguan Pencernaan",
        "Gangguan Umum"
    ],
    "Gangguan Pernapasan": [
        "Kemungkinan Flu",
        "Kemungkinan Alergi"
    ],
    "Gangguan Pencernaan": [
        "Kemungkinan Gangguan Pencernaan"
    ],
    "Gangguan Umum": [
        "Kemungkinan Demam"
    ],
    "Kemungkinan Flu": [],
    "Kemungkinan Alergi": [],
    "Kemungkinan Gangguan Pencernaan": [],
    "Kemungkinan Demam": []
}

# Gejala yang berhubungan dengan setiap kandidat.
# Data ini hanya contoh ilustratif, bukan aturan klinis.
SYMPTOM_RULES = {
    "Kemungkinan Flu": {
        "demam", "batuk", "sakit tenggorokan", "nyeri otot"
    },
    "Kemungkinan Alergi": {
        "bersin", "hidung gatal", "mata gatal"
    },
    "Kemungkinan Gangguan Pencernaan": {
        "mual", "muntah", "sakit perut", "diare"
    },
    "Kemungkinan Demam": {
        "demam", "lemas", "sakit kepala"
    }
}


def bfs_search(start, symptoms):
    """Menelusuri pohon dari tingkat paling atas."""
    queue = deque([start])
    visited = []
    results = []

    while queue:
        node = queue.popleft()
        visited.append(node)

        # Memeriksa apakah node merupakan kandidat kondisi.
        if node in SYMPTOM_RULES:
            matched = SYMPTOM_RULES[node].intersection(symptoms)

            if matched:
                results.append({
                    "condition": node,
                    "matched": sorted(matched),
                    "count": len(matched)
                })

        # Menambahkan anak ke antrean BFS.
        for child in MEDICAL_TREE.get(node, []):
            queue.append(child)

    return results, visited


def dfs_search(start, symptoms):
    """Menelusuri satu cabang sedalam mungkin."""
    stack = [start]
    visited = []
    results = []

    while stack:
        node = stack.pop()
        visited.append(node)

        if node in SYMPTOM_RULES:
            matched = SYMPTOM_RULES[node].intersection(symptoms)

            if matched:
                results.append({
                    "condition": node,
                    "matched": sorted(matched),
                    "count": len(matched)
                })

        # Dibalik agar urutan penelusuran mengikuti
        # urutan anak pada pohon.
        children = MEDICAL_TREE.get(node, [])
        stack.extend(reversed(children))

    return results, visited


def display_results(method, results, visited):
    """Menampilkan hasil pencarian."""
    print(f"\n===== HASIL {method} =====")
    print("Urutan simpul yang dikunjungi:")
    print(" -> ".join(visited))
    print("Jumlah simpul dikunjungi:", len(visited))

    if not results:
        print("\nTidak ada kandidat yang cocok dengan gejala.")
        return

    # Kandidat dengan jumlah gejala cocok terbanyak
    # ditampilkan lebih dahulu.
    results.sort(key=lambda item: item["count"], reverse=True)

    print("\nKandidat kondisi berdasarkan kecocokan gejala:")

    for result in results:
        print(f"\nKondisi: {result['condition']}")
        print("Gejala cocok:", ", ".join(result["matched"]))
        print(
            f"Jumlah gejala cocok: "
            f"{result['count']}"
        )


def main():
    print("====================================")
    print("     MEDICAL DIAGNOSIS SEARCH")
    print("====================================")
    print("Masukkan gejala yang dirasakan.")
    print("Pisahkan beberapa gejala dengan koma.")
    print("\nContoh: demam, batuk, lemas")

    user_input = input("\nGejala: ").strip().lower()

    symptoms = {
        item.strip()
        for item in user_input.split(",")
        if item.strip()
    }

    if not symptoms:
        print("Gejala belum dimasukkan.")
        return

    print("\nGejala yang dimasukkan:", ", ".join(sorted(symptoms)))

    bfs_results, bfs_visited = bfs_search(
        "Medical Diagnosis", symptoms
    )
    dfs_results, dfs_visited = dfs_search(
        "Medical Diagnosis", symptoms
    )

    display_results("BFS", bfs_results, bfs_visited)
    display_results("DFS", dfs_results, dfs_visited)

    print("\nCatatan:")
    print("Hasil ini hanya simulasi edukasi, bukan diagnosis medis.")
    print("Gejala yang sama dapat muncul pada berbagai kondisi.")
    print("Hubungi tenaga kesehatan untuk penilaian medis.")


if __name__ == "__main__":
    main()
