import { Component } from '@angular/core';
import { RouterOutlet } from '@angular/router';
import { Router } from '@angular/router';
import { HeaderComponent } from './components/header/header.component';
import { CommonModule } from '@angular/common';

@Component({
  selector: 'app-root',
  standalone: true,
  imports: [RouterOutlet, HeaderComponent, CommonModule],
  templateUrl: './app.component.html',
  styleUrl: './app.component.scss'
})
export class AppComponent {
  title = 'gui';

  constructor(private router: Router) {}

  // Check if the current route is /todos
  hideHeader(): boolean {
    const pagesWitoutHeader: Array<string> = ["/login", "/register"]
    return pagesWitoutHeader.includes(this.router.url);
  }
}
