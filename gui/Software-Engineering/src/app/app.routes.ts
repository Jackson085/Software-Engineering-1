import { Routes } from '@angular/router';
import { RegisterComponent } from './register/register.component';
import { HomeComponent } from './home/home.component';
import { GalerieComponent } from './galerie/galerie.component';

export const routes: Routes = [
    {
        path: 'Register',
        title: 'Register Menü',
        component: RegisterComponent,
    },
    {
        path: 'Home',
        title: 'Home Menü',
        component: HomeComponent,
    },
    {
        path: 'Galerie',
        title: 'Galerie Menü',
        component: GalerieComponent,
    }
];
