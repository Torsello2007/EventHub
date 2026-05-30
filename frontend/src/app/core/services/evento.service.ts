import { Injectable, inject } from '@angular/core';
import { HttpClient } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { Evento } from '../models/evento.model';
import { Observable } from 'rxjs';

@Injectable({ providedIn: 'root' })
export class EventoService {
  private http = inject(HttpClient);
  private apiUrl = `${environment.apiUrl}/eventi`;

  getEventi(): Observable<Evento[]> {
    return this.http.get<Evento[]>(this.apiUrl);
  }
}
