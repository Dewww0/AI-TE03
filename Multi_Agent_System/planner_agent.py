```python
class PlannerAgent:
    """
    Agen yang bertugas merencanakan proyek
    dan membagi proyek menjadi beberapa tugas.
    """

    def __init__(self, name="Planner Agent"):
        self.name = name

    def create_tasks(self, project):
        """
        Membuat daftar tugas berdasarkan jenis proyek.
        """

        print("\n" + "=" * 50)
        print(f"[{self.name}] PERENCANAAN PROYEK")
        print("=" * 50)

        print(f"Nama proyek: {project}")
        print("\nMenganalisis proyek dan menyusun tugas...")

        # Menentukan tugas berdasarkan jenis proyek
        project_lower = project.lower()

        if "website" in project_lower or "web" in project_lower:
            tasks = [
                "Menganalisis kebutuhan website",
                "Merancang antarmuka website",
                "Membuat kode program website",
                "Menguji fungsi website",
                "Mengevaluasi hasil website"
            ]

        elif "sistem informasi" in project_lower:
            tasks = [
                "Mengidentifikasi kebutuhan sistem",
                "Merancang struktur sistem informasi",
                "Mengembangkan fungsi sistem",
                "Menguji fungsi sistem",
                "Mengevaluasi hasil pengembangan sistem"
            ]

        elif "monitoring" in project_lower or "esp32" in project_lower:
            tasks = [
                "Mengidentifikasi kebutuhan perangkat",
                "Menentukan sensor dan komponen",
                "Merancang sistem monitoring",
                "Membuat program mikrokontroler",
                "Menguji dan mengevaluasi sistem"
            ]

        else:
            tasks = [
                "Mengumpulkan kebutuhan proyek",
                "Menyusun rencana penyelesaian proyek",
                "Melaksanakan pekerjaan proyek",
                "Menguji hasil pekerjaan",
                "Mengevaluasi hasil akhir proyek"
            ]

        # Menampilkan daftar tugas
        print("\nDaftar tugas yang berhasil dibuat:")

        for i, task in enumerate(tasks, start=1):
            print(f"{i}. {task}")

        print(f"\nTotal tugas: {len(tasks)}")
        print("=" * 50)

        # Mengembalikan daftar tugas untuk agen berikutnya
        return tasks


if __name__ == "__main__":
    planner = PlannerAgent()

    project_name = input("Masukkan nama proyek: ")

    if project_name.strip():
        planner.create_tasks(project_name)
    else:
        print("Nama proyek tidak boleh kosong.")
```
