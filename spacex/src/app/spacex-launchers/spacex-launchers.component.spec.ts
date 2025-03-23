import { ComponentFixture, TestBed } from '@angular/core/testing';

import { SpacexLaunchersComponent } from './spacex-launchers.component';

describe('SpacexLaunchersComponent', () => {
  let component: SpacexLaunchersComponent;
  let fixture: ComponentFixture<SpacexLaunchersComponent>;

  beforeEach(async () => {
    await TestBed.configureTestingModule({
      imports: [SpacexLaunchersComponent]
    })
    .compileComponents();

    fixture = TestBed.createComponent(SpacexLaunchersComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
