import { NgModule } from '@angular/core';
import { BrowserModule } from '@angular/platform-browser';
import { AppRoutingModule } from './app-routing.module';
import { FontAwesomeModule } from '@fortawesome/angular-fontawesome';
import { BrowserAnimationsModule } from '@angular/platform-browser/animations';
import { HeaderModule } from './header/header.module';
import { NgbModule } from '@ng-bootstrap/ng-bootstrap';
import { LogoModule } from './common/logo/logo.module';

import { ThemeService } from './core/services/theme.service';
import { BackendService } from './core/services/backend.service'

import { AppComponent } from './app.component';



@NgModule({
  declarations: [
    AppComponent
  ],
  imports: [
    BrowserModule,
    AppRoutingModule,
    BrowserAnimationsModule,
    FontAwesomeModule,
    HeaderModule,
    LogoModule,
    NgbModule
  ],
  providers: [
    ThemeService,
    BackendService
  ],
  bootstrap: [AppComponent]
})
export class AppModule { }
