import { Injectable, inject } from '@angular/core';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Evento } from '../models/evento.model';
import { Observable } from 'rxjs';
import { AuthService } from './auth.service';

@Injectable({ providedIn: 'root' })
export class EventoService {
  private http = inject(HttpClient);
  private auth = inject(AuthService);
  private apiUrl = `${environment.apiUrl}`;

  getEventi(): Observable<Evento[]> {
    return this.http.get<Evento[]>(`${this.apiUrl}/eventi`);
  }

  getMieiBiglietti(): Observable<any[]> {
    const headers = new HttpHeaders().set('Authorization', `Bearer ${this.auth.getToken()}`);
    return this.http.get<any[]>(`${this.apiUrl}/utente/biglietti`, { headers });
  }

  iscriviti(idEvento: number): Observable<any> {
    const headers = new HttpHeaders().set('Authorization', `Bearer ${this.auth.getToken()}`);
    return this.http.post(`${this.apiUrl}/eventi/${idEvento}/iscriviti`, {}, { headers });
  }
}
