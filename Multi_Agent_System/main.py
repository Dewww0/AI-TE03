from planner_agent import PlannerAgent
class PlannerAgent:
    """Agen yang membagi proyek menjadi beberapa tugas."""

    def __init__(self, name):
        self.name = name

    def create_tasks(self, project):
        print(f"\n[{self.name}] Membuat rencana untuk: {project}")

        tasks = [
            "Mengumpulkan kebutuhan proyek",
            "Mengerjakan solusi proyek",
            "Menguji hasil pekerjaan"
        ]

        for i, task in enumerate(tasks, start=1):
            print(f"Tugas {i}: {task}")

        return tasks


class WorkerAgent:
    """Agen yang mengerjakan tugas."""

    def __init__(self, name):
        self.name = name

    def perform_task(self, task):
        print(f"[{self.name}] Mengerjakan: {task}")

        # Simulasi pengerjaan tugas
        result = {
            "task": task,
            "status": "Selesai"
        }

        print(f"[{self.name}] Status: {result['status']}")
        return result


class EvaluatorAgent:
    """Agen yang memeriksa hasil pekerjaan."""

    def __init__(self, name):
        self.name = name

    def evaluate(self, results):
        print(f"\n[{self.name}] Memeriksa hasil pekerjaan...")

        completed = all(
            result["status"] == "Selesai"
            for result in results
        )

        if completed:
            print("Evaluasi: Semua tugas berhasil diselesaikan!")
        else:
            print("Evaluasi: Masih ada tugas yang belum selesai.")

        return completed


class MultiAgentSystem:
    """Mengatur kerja sama seluruh agen."""

    def __init__(self):
        self.planner = PlannerAgent("Planner Agent")
        self.worker = WorkerAgent("Worker Agent")
        self.evaluator = EvaluatorAgent("Evaluator Agent")

    def run(self, project):
        print("=" * 45)
        print(" MULTI-AGENT SYSTEM")
        print("=" * 45)

        # Agen perencana membuat daftar tugas
        tasks = self.planner.create_tasks(project)

        # Agen pekerja mengerjakan setiap tugas
        results = []
        for task in tasks:
            result = self.worker.perform_task(task)
            results.append(result)

        # Agen evaluator memeriksa semua hasil
        success = self.evaluator.evaluate(results)

        print("\n" + "=" * 45)
        print("HASIL AKHIR")
        print(f"Proyek       : {project}")
        print(f"Jumlah tugas : {len(tasks)}")
        print(f"Status       : {'BERHASIL' if success else 'BELUM SELESAI'}")
        print("=" * 45)


if __name__ == "__main__":
    mas = MultiAgentSystem()
    mas.run("Pembuatan Sistem Informasi Sederhana")

