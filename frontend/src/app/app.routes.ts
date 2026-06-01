// Apri il file src/app/app.routes.ts e incolla questo:
import { Routes } from '@angular/router';
import { HomeComponent } from './pages/home/home.component';
import { EventListComponent } from './pages/event-list/event-list.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', component: HomeComponent },         // Homepage di benvenuto
  { path: 'eventi', component: EventListComponent }, // Lista completa eventi
  { path: 'profile', component: ProfileComponent, canActivate: [authGuard] },
  { path: '**', redirectTo: '' }
];