import { Routes } from '@angular/router';
import { LoginComponent } from './login/login.component';
import { RegisterComponent } from './register/register.component';

export const routes: Routes = [
    {
        path: 'Login',
        title: 'Login Menü',
        component: LoginComponent,
    },
    {
        path: 'Register',
        title: 'Register Menü',
        component: RegisterComponent,
    },
];
