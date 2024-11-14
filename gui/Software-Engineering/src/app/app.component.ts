import { Component } from '@angular/core';
import { RouterLink, RouterOutlet } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { GalerieComponent } from './galerie/galerie.component';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterLink, RouterOutlet, RegisterComponent, HomeComponent, GalerieComponent],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  ShowLogin: boolean = true;
  ShowRegister: boolean = false;
  ShowHome: boolean = false;
  ShowGalerie: boolean = false;

  Register() {
    this.ShowLogin = false,
    this.ShowRegister = true
  }

  Home(){
    this.ShowHome = true,
    this.ShowLogin = false,
    this.ShowGalerie = false
  }

  Galerie(){
    this.ShowGalerie = true,
    this.ShowHome = false
  }
}
