import { async, ComponentFixture, TestBed } from '@angular/core/testing';

import { LiderboardComponent } from './liderboard.component';

describe('TabsComponent', () => {
  let component: LiderboardComponent;
  let fixture: ComponentFixture<LiderboardComponent>;

  beforeEach(async(() => {
    TestBed.configureTestingModule({
      declarations: [ LiderboardComponent ]
    })
    .compileComponents();
  }));

  beforeEach(() => {
    fixture = TestBed.createComponent(LiderboardComponent);
    component = fixture.componentInstance;
    fixture.detectChanges();
  });

  it('should create', () => {
    expect(component).toBeTruthy();
  });
});
