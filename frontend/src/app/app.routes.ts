import { Routes } from '@angular/router';
import { EventListComponent } from './pages/event-list/event-list.component';

export const routes: Routes = [
  { path: '', component: EventListComponent },
  { path: '**', redirectTo: '' }
];
