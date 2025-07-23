export interface Task {
  task_id: number;
  description: string;
  user_id: number;
  status: 'pending' | 'completed' | 'postponed';
  due_date: string | null;
  deleted: boolean;
  created_at: string;
  updated_at: string;
} 