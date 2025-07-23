import { NgModule } from '@angular/core';
import { RouterModule, Routes } from '@angular/router';
import { RegisterComponent } from './features/auth/register/register.component';
import { TaskListComponent } from './features/tasks/task-list/task-list.component';
import { TestComponent } from './features/test/test.component';

const routes: Routes = [
  { path: '', redirectTo: 'tasks', pathMatch: 'full' },
  { path: 'register', component: RegisterComponent },
  { path: 'tasks', component: TaskListComponent },
  { path: 'test', component: TestComponent },
  { path: '**', redirectTo: 'tasks' }
];

@NgModule({
  imports: [RouterModule.forRoot(routes)],
  exports: [RouterModule]
})
export class AppRoutingModule { }
