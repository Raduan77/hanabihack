import { Component, OnInit, Input } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-liderboard',
  templateUrl: './liderboard.component.html',
  styleUrls: ['./liderboard.component.scss']
})
export class LiderboardComponent implements OnInit {

  ln = "";
  subscription: any;
  private routeSubscription: Subscription;
  private querySubscription: Subscription;

  ngOnInit(): void {
  }

  constructor(private route: ActivatedRoute) { 
    this.querySubscription = route.queryParams.subscribe(
        (queryParam: any) => {
          console.log(queryParam['ln']);
        }
    );
  }

}
