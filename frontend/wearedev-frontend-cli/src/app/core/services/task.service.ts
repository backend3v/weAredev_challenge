import { Injectable } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { Observable } from 'rxjs';
import { Task } from '../models/task.model';

@Injectable({ providedIn: 'root' })
export class TaskService {
  private apiUrl = 'http://localhost:8000/api/users/tasks';

  constructor(private http: HttpClient) {}

  getByUser(userId: number): Observable<Task[]> {
    return this.http.get<Task[]>(`${this.apiUrl}/${userId}/`);
  }

  create(userId: number, description: string, due_date?: string): Observable<Task> {
    return this.http.post<Task>(`${this.apiUrl}/${userId}/`, { description, due_date });
  }

  getDetail(taskId: number): Observable<Task> {
    return this.http.get<Task>(`${this.apiUrl}/detail/${taskId}/`);
  }

  update(taskId: number, data: Partial<Task>): Observable<Task> {
    return this.http.put<Task>(`${this.apiUrl}/detail/${taskId}/`, data);
  }

  delete(taskId: number): Observable<void> {
    return this.http.delete<void>(`${this.apiUrl}/detail/${taskId}/`);
  }

  changeStatus(taskId: number, status: 'pending' | 'completed' | 'postponed'): Observable<Task> {
    return this.http.patch<Task>(`${this.apiUrl}/status/${taskId}/`, { status });
  }
} 