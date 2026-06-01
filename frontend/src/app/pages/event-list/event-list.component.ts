import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { RouterModule } from '@angular/router';
import { EventoService } from '../../core/services/evento.service';
import { Evento } from '../../core/models/evento.model';

@Component({
  selector: 'app-event-list',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './event-list.component.html'
})
export class EventListComponent implements OnInit {
  private eventoService = inject(EventoService);
  eventi: Evento[] = [];

  ngOnInit(): void {
    this.eventoService.getEventi().subscribe({
      next: (data) => this.eventi = data,
      error: (err) => console.error('Errore caricamento:', err)
    });
  }
}
