import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { TaskService } from '../task.service';

@Component({
  selector: 'app-task-detail',
  template: `
    <div class="task-detail">
      <h2>{{ task.title }}</h2>
      <p>{{ task.description }}</p>
      <p>Category: {{ task.category }}</p>
      <p>Status: {{ task.status }}</p>
      <p>Deadline: {{ task.deadline | date }}</p>
      <button (click)="goBack()">Вернуться к задачам</button>
    </div>
  `,
  styleUrls: ['./task-detail.component.css']
})
export class TaskDetailComponent implements OnInit {
  task: any;

  constructor(private route: ActivatedRoute, private taskService: TaskService) {}

  ngOnInit() {
    const taskId = this.route.snapshot.paramMap.get('id')!;
    this.task = this.taskService.getTaskById(taskId);
  }

  goBack() {
    window.history.back();
  }
}