import { Routes } from '@angular/router';
import { EventListComponent } from './pages/event-list/event-list.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { OrganizerDashboardComponent } from './pages/organizer-dashboard/organizer-dashboard.component';
import { MyTicketsComponent } from './pages/my-tickets/my-tickets.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', component: EventListComponent },
  { path: 'profile', component: ProfileComponent, canActivate: [authGuard] },
  { path: 'biglietti', component: MyTicketsComponent, canActivate: [authGuard] },
  { path: 'organizer', component: OrganizerDashboardComponent, canActivate: [authGuard], data: { role: 'organizer' } },
  { path: '**', redirectTo: '' }
];
