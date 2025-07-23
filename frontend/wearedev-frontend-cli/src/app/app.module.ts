import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { HttpClientModule } from '@angular/common/http';
import { AppRoutingModule } from './app-routing.module';
import { AppComponent } from './app.component';
import { RegisterComponent } from './features/auth/register/register.component';
import { TaskListComponent } from './features/tasks/task-list/task-list.component';
import { TestComponent } from './features/test/test.component';
import { TaskFormComponent } from './features/tasks/task-form/task-form.component';

@NgModule({
  declarations: [
    AppComponent,
    RegisterComponent,
    TaskListComponent,
    TestComponent,
    TaskFormComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    HttpClientModule
  ],
  providers: [],
  bootstrap: [AppComponent]
})
export class AppModule { }
