import { Component, OnInit } from '@angular/core';
import { Router } from '@angular/router';
import { delay } from 'q';

@Component({
  selector: 'app-progressbar',
  templateUrl: './progressbar.component.html',
  styleUrls: ['./progressbar.component.scss']
})
export class ProgressbarComponent implements OnInit {

  constructor(private router: Router) { }

  ngOnInit() {
    this.func();
  }

  async func() {
    await delay(3000);
    window.location.href = 'http://localhost:4200/languages?name=Artemiy';
  }

}
