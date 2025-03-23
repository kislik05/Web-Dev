import { Component } from '@angular/core';
import { SpacexLaunchesComponent } from './spacex-launchers/spacex-launchers.component';
import { LaunchFilterComponent } from './launch-filter/launch-filter.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [SpacexLaunchesComponent, LaunchFilterComponent], // Импортируем SpacexLaunchesComponent
  templateUrl: './app.component.html',
  styleUrls: ['./app.component.css']
})
export class AppComponent {
  title = 'spacex-launches-app';
}