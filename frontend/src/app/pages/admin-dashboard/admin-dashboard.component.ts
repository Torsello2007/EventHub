import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-admin-dashboard',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './admin-dashboard.component.html'
})
export class AdminDashboardComponent implements OnInit {
  private http = inject(HttpClient);
  private auth = inject(AuthService);
  utenti: any[] = [];
  recensioni: any[] = [];

  ngOnInit() {
    const headers = new HttpHeaders().set('Authorization', `Bearer ${this.auth.getToken()}`);
    this.http.get<any[]>(`${environment.apiUrl}/admin/utenti`, { headers }).subscribe(d => this.utenti = d);
    this.http.get<any[]>(`${environment.apiUrl}/admin/recensioni`, { headers }).subscribe(d => this.recensioni = d);
  }

  banUtente(user: string) { alert('Utente ' + user + ' bannato'); }
  deleteRecensione(id: number) { alert('Recensione ' + id + ' eliminata'); }
}
