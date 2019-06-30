import { Component, OnInit } from '@angular/core';
import { ActivatedRoute } from '@angular/router';
import { Subscription } from 'rxjs';

@Component({
  selector: 'app-languages',
  templateUrl: './languages.component.html',
  styleUrls: ['./languages.component.scss']
})
export class LanguagesComponent implements OnInit {

  name = "";
  subscription: any;
  private routeSubscription: Subscription;
  private querySubscription: Subscription;

  ngOnInit(): void {
  }

  constructor(private route: ActivatedRoute) { 
    this.querySubscription = route.queryParams.subscribe(
        (queryParam: any) => {
          this.name = queryParam['name'];
        }
    );
  }
    
}
