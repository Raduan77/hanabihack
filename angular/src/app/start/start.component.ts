import { Component, OnInit } from '@angular/core';
import { NgForm } from '@angular/forms';
import { Router } from '@angular/router';
import { HttpClient } from '@angular/common/http';

@Component({
  selector: 'app-start',
  templateUrl: './start.component.html',
  styleUrls: ['./start.component.scss']
})
export class StartComponent implements OnInit {

  constructor(private router: Router, private http: HttpClient) { 

  }

  ngOnInit() {
    this.http.get('https://api.tinkoff.ru/v1/news_content?id=10024').subscribe((data) => console.log(data));
  }

  Login(form: NgForm) {
    console.log(form.value.email);
    console.log(form.value);
    window.location.href = 'http://localhost:4200/languages?name=Artemiy';
  }

  
}
