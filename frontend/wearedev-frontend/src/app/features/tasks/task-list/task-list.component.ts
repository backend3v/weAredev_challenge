import { Component, OnInit } from '@angular/core';
import { TaskService } from 'src/app/core/services/task.service';
import { Task } from 'src/app/core/models/task.model';

@Component({
  selector: 'app-task-list',
  templateUrl: './task-list.component.html',
  styleUrls: ['./task-list.component.scss']
})
export class TaskListComponent implements OnInit {
  tasks: Task[] = [];
  userId = 1; // Cambia esto según el usuario seleccionado
  errorMessage = '';
  editingTask?: Task;

  constructor(private taskService: TaskService) {}

  ngOnInit(): void {
    this.loadTasks();
  }

  loadTasks() {
    this.taskService.getByUser(this.userId).subscribe({
      next: (tasks) => {
        this.tasks = tasks;
        this.errorMessage = '';
      },
      error: (err) => {
        this.errorMessage = err.error?.detail || 'Error loading tasks.';
      }
    });
  }

  onTaskSaved(newTask: Task) {
    this.loadTasks();
  }

  editTask(task: Task) {
    this.editingTask = { ...task };
  }

  onTaskEdited(updatedTask: Task) {
    this.editingTask = undefined;
    this.loadTasks();
  }

  deleteTask(taskId: number) {
    if (confirm('Are you sure you want to delete this task?')) {
      this.taskService.delete(taskId).subscribe({
        next: () => this.loadTasks(),
        error: (err) => {
          this.errorMessage = err.error?.detail || 'Error deleting task.';
        }
      });
    }
  }

  changeStatus(taskId: number, status: 'pending' | 'completed' | 'postponed') {
    this.taskService.changeStatus(taskId, status).subscribe({
      next: () => this.loadTasks(),
      error: (err) => {
        this.errorMessage = err.error?.detail || 'Error changing status.';
      }
    });
  }
} 