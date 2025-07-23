import { Component, Input, Output, EventEmitter, OnInit } from '@angular/core';
import { FormBuilder, FormGroup, Validators } from '@angular/forms';
import { TaskService } from '../../../core/services/task.service';
import { Task } from '../../../core/models/task.model';

@Component({
  selector: 'app-task-form',
  templateUrl: './task-form.component.html',
  styleUrls: ['./task-form.component.scss']
})
export class TaskFormComponent implements OnInit {
  @Input() userId!: number;
  @Input() task?: Task; // Si se pasa, es edición
  @Output() taskSaved = new EventEmitter<Task>();

  taskForm: FormGroup;
  errorMessage = '';
  isEdit = false;

  constructor(private fb: FormBuilder, private taskService: TaskService) {
    this.taskForm = this.fb.group({
      description: ['', Validators.required],
      due_date: ['']
    });
  }

  ngOnInit(): void {
    if (this.task) {
      this.isEdit = true;
      this.taskForm.patchValue({
        description: this.task.description,
        due_date: this.task.due_date
      });
    }
  }

  onSubmit() {
    if (this.taskForm.valid) {
      const { description, due_date } = this.taskForm.value;
      if (this.isEdit && this.task) {
        this.taskService.update(this.task.task_id, { description, due_date }).subscribe({
          next: (updatedTask: Task) => {
            this.taskSaved.emit(updatedTask);
            this.errorMessage = '';
          },
          error: (err: any) => {
            this.errorMessage = err.error?.detail || 'Error updating task.';
          }
        });
      } else {
        this.taskService.create(this.userId, description, due_date).subscribe({
          next: (newTask: Task) => {
            this.taskSaved.emit(newTask);
            this.errorMessage = '';
            this.taskForm.reset();
          },
          error: (err: any) => {
            this.errorMessage = err.error?.detail || 'Error creating task.';
          }
        });
      }
    }
  }
}
