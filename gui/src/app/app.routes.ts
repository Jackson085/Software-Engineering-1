import { RouterModule, Routes, UrlSerializer, DefaultUrlSerializer, UrlTree } from '@angular/router';
import { authGuard } from './auth.guard';

export const routes: Routes = [
  {
    path: 'login',
    loadComponent: () => {
      return import('./login/login.component').then((m) => m.LoginComponent);
    },
  },
  {
    path: 'register',
    loadComponent: () => {
      return import('./register/register.component').then((m) => m.RegisterComponent);
    },
  },
  {
    path: 'home',
    canActivate: [authGuard], // Protect this route
    loadComponent: () => {
      return import('./home/home.component').then((m) => m.HomeComponent);
    },
  },
  {
    path: '**',
    canActivate: [authGuard], // Protect the wildcard route
    loadComponent: () => {
      return import('./home/home.component').then((m) => m.HomeComponent); // Redirect to Home if logged in
    },
  },
];