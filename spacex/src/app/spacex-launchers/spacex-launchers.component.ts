import { Component, OnInit } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { CommonModule } from '@angular/common'; // Импортируйте CommonModule

@Component({
  selector: 'app-spacex-launches',
  standalone: true, // Добавьте это
  imports: [CommonModule], // Импортируйте CommonModule для *ngFor и *ngIf
  templateUrl: './spacex-launches.component.html',
  styleUrls: ['./spacex-launches.component.css']
})
export class SpacexLaunchesComponent implements OnInit {
  launches: any[] = [];
  filteredLaunches: any[] = [];

  constructor(private http: HttpClient) {}

  ngOnInit(): void {
    this.http.get('https://api.spacexdata.com/v4/launches').subscribe((data: any) => {
      this.launches = data;
      this.filteredLaunches = data;
    });
  }

  filterLaunches(successful: boolean): void {
    this.filteredLaunches = this.launches.filter(launch => launch.success === successful);
  }
}