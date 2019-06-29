import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent implements OnInit {

  constructor(private router: Router) { 
  }

  ngOnInit() {
  }

  Login(form: NgForm) {
    console.log(form.value.email);
    console.log(form.value);
    window.location.href = 'http://localhost:4200/languages';
  }
}
