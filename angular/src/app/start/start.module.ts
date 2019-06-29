import { NgModule } from '@angular/core';

import { Router } from '@angular/router';
import { AppModule } from '../app.module';
import { StartComponent } from './start.component';

@NgModule({
  imports: [
      
  ],
  declarations: [
    StartComponent,
  ],
})

export class AddBranchModule { 
  constructor (router : Router) {
    
  }
}
