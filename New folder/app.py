# Danh sách để lưu các công việc
tasks = [
    {'name': 'Học bài Git', 'completed': False},
    {'name': 'Làm bài tập thực hành ở nhà', 'completed': False}
]

# Hàm thêm công việc mới
def add_task(task_name):
    tasks.append({'name': task_name, 'completed': False})
    print(f"✅ Đã thêm công việc: {task_name}")

# Hàm liệt kê các công việc
def list_tasks():
    print("\n📋 Danh sách công việc:")
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task['completed'] else "❌"
        print(f"{i}. {task['name']} - {status}")

# Hàm đánh dấu công việc hoàn thành
def complete_task(task_index):
    if 0 <= task_index < len(tasks):
        tasks[task_index]['completed'] = True
        print(f"🎉 Công việc '{tasks[task_index]['name']}' đã hoàn thành!")
    else:
        print("⚠️ Chỉ số không hợp lệ!")

# Hàm xóa công việc
def delete_task(task_index):
    if 0 <= task_index < len(tasks):
        removed = tasks.pop(task_index)
        print(f"🗑️ Đã xóa công việc: {removed['name']}")
    else:
        print("⚠️ Chỉ số không hợp lệ!")

# --- Bắt đầu chương trình ---
if __name__ == "__main__":
    print("👋 Chào mừng đến với ứng dụng To-Do List!")
    list_tasks()
