import { Routes } from '@angular/router';
import { EventListComponent } from './pages/event-list/event-list.component';
import { ProfileComponent } from './pages/profile/profile.component';
import { OrganizerDashboardComponent } from './pages/organizer-dashboard/organizer-dashboard.component';
import { MyTicketsComponent } from './pages/my-tickets/my-tickets.component';
import { EventDetailComponent } from './pages/event-detail/event-detail.component';
import { AdminDashboardComponent } from './pages/admin-dashboard/admin-dashboard.component';
import { authGuard } from './core/guards/auth.guard';

export const routes: Routes = [
  { path: '', component: EventListComponent },
  { path: 'evento/:id', component: EventDetailComponent },
  { path: 'profile', component: ProfileComponent, canActivate: [authGuard] },
  { path: 'biglietti', component: MyTicketsComponent, canActivate: [authGuard] },
  { path: 'organizer', component: OrganizerDashboardComponent, canActivate: [authGuard], data: { role: 'organizer' } },
  { path: 'admin', component: AdminDashboardComponent, canActivate: [authGuard], data: { role: 'admin' } },
  { path: '**', redirectTo: '' }
];
