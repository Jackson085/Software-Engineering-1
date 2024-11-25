import { RouterModule, Routes, UrlSerializer, DefaultUrlSerializer, UrlTree } from '@angular/router';

export const routes: Routes = [
    {
        path: 'login',
        loadComponent: () => {
            return import('./login/login.component').then((m) => m.LoginComponent)
        },
    },
    {
        path: 'register',
        loadComponent: () => {
            return import('./register/register.component').then((m) => m.RegisterComponent)
        },
    }
];