"""

To-Do List (Yapılacaklar Listesi)

Proje Tanımı: 
Bir yapılacaklar listesi uygulaması oluşturun. Kullanıcı görev ekleyebilir, görevleri tamamlandı olarak işaretleyebilir ve tamamlananları silebilir.

İstenilen Özellikler:
Görev ekleme.
Görevleri tamamlama ve tamamlandı olarak işaretleme.
Görev listesini görüntüleme (tamamlananlar ve tamamlanmayanlar ayrı listelerde tutulabilir).
Görev silme.
Verileri bir .txt dosyasına kaydetme ve program çalıştığında yeniden yükleme.


Yönerge:
Bir Task (Görev) sınıfı oluşturun. Bu sınıf, görev adı ve tamamlanma durumunu (True/False) saklasın.
Bir TaskManager sınıfı oluşturun. Bu sınıf, görevlerin eklenmesi, silinmesi ve yönetilmesi için gerekli metotları içersin.


"""


class Task:
    def __init__(self, name):
        self.name = name
        self.completed = False

    def complete(self):
        self.completed = True

    def __str__(self):
        return f"[{'*' if self.completed else ' '}] {self.name}"
    
class TaskManager:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def remove_task(self, task):
        self.tasks.remove(task)

    def complete_task(self, task):
        task.complete()

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(f"{task.name},{task.completed}\n")

    def load_tasks(self, filename):
        try:
            with open(filename, 'r') as f:
                for line in f:
                    name, completed = line.strip().split(',')
                    task = Task(name)
                    task.completed = completed == 'True'
                    self.tasks.append(task)
        except FileNotFoundError:
            pass

    def display_tasks(self):
        print("Yapılacaklar:")
        for task in self.tasks:
            print(task)
        print("Tamamlananlar:")
        for task in self.tasks:
            if task.completed:
                print(task)

if __name__ == "__main__":
    manager = TaskManager()
    manager.load_tasks("tasks.txt")

    while True:
        print("\n1. Görev Ekle\n2. Görev Sil\n3. Görevi Tamamla\n4. Görevleri Görüntüle\n5. Çıkış")
        choice = input("Seçenek: ")

        if choice == '1':
            task_name = input("Görev adı: ")
            manager.add_task(Task(task_name))
        elif choice == '2':
            manager.display_tasks()
            task_index = int(input("Silmek istediğiniz görevin numarası: ")) - 1
            manager.remove_task(manager.tasks[task_index])
        elif choice == '3':
            manager.display_tasks()
            task_index = int(input("Tamamlamak istediğiniz görevin numarası: ")) - 1
            manager.complete_task(manager.tasks[task_index])
        elif choice == '4':
            manager.display_tasks()
        elif choice == '5':
            manager.save_tasks("tasks.txt")
            break
        else:
            print("Geçersiz seçenek.")

