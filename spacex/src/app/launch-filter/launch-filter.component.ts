import { Component, Output, EventEmitter } from '@angular/core';
import { CommonModule } from '@angular/common'; // Импортируйте CommonModule

@Component({
  selector: 'app-launch-filter',
  standalone: true, // Добавьте это
  imports: [CommonModule], // Импортируйте CommonModule для работы с шаблоном
  templateUrl: './launch-filter.component.html',
  styleUrls: ['./launch-filter.component.css']
})
export class LaunchFilterComponent {
  @Output() filter = new EventEmitter<boolean>();

  filterSuccessful(): void {
    this.filter.emit(true);
  }
}