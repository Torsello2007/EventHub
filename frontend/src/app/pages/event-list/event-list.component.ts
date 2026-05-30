import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EventoService } from '../../core/services/evento.service';
import { Evento } from '../../core/models/evento.model';

@Component({
  selector: 'app-event-list',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-list.component.html'
})
export class EventListComponent implements OnInit {
  private eventoService = inject(EventoService);
  eventi: Evento[] = [];

  ngOnInit(): void {
    this.eventoService.getEventi().subscribe(data => this.eventi = data);
  }
}
