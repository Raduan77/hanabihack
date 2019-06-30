import { Component, OnInit } from '@angular/core';
import { Subscription } from 'rxjs';
import { ActivatedRoute } from '@angular/router';

@Component({
  selector: 'app-test',
  templateUrl: './test.component.html',
  styleUrls: ['./test.component.scss']
})
export class TestComponent implements OnInit {

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
