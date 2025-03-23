import { Injectable } from '@angular/core';

@Injectable({
  providedIn: 'root'
})
export class TaskService {
  private tasks = [
    { id: 1, title: 'Task 1', description: 'Description 1', category: 'Work', status: 'pending', deadline: new Date('2023-12-01') },
    { id: 2, title: 'Task 2', description: 'Description 2', category: 'Personal', status: 'pending', deadline: new Date('2023-12-05') }
  ];

  getTasks() {
    return this.tasks;
  }

  getTaskById(id: string) {
    return this.tasks.find(task => task.id === +id);
  }
}