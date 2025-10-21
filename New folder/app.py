# Danh sách để lưu các công việc
tasks = [
    {'name': 'Học bài Git', 'completed': False},
    {'name': 'Làm bài tập', 'completed': False}
]

def complete_task(task_index):
    tasks[task_index]['completed'] = True

def list_tasks():
    for i, task in enumerate(tasks, start=1):
        print(f"{i}. {task}")# Thêm hàm xóa công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks.pop(task_index)
    else:
        print("Chỉ số không hợp lệ!")


# --- Điểm bắt đầu của chương trình ---
if __name__ == "__main__":
   print("Chào mừng đến với ứng dụng To-Do List!")
   add_task("Học bài Git và GitHub")
   add_task("Làm bài tập thực hành ở nhà")
