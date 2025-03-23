import { Component, Input } from '@angular/core';

@Component({
  selector: 'app-base-task',
  template: ''
})

export class BaseTaskComponent {
  @Input() title: string = '';
  @Input() description: string = '';
  @Input() category: string = '';
  @Input() status: string = 'pending';
  @Input() deadline: Date = new Date();
}