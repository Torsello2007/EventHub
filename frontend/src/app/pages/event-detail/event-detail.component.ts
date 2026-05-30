import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { ActivatedRoute } from '@angular/router';
import { EventoService } from '../../core/services/evento.service';

@Component({
  selector: 'app-event-detail',
  standalone: true,
  imports: [CommonModule],
  templateUrl: './event-detail.component.html'
})
export class EventDetailComponent implements OnInit {
  private route = inject(ActivatedRoute);
  private eventoService = inject(EventoService);
  evento: any;

  ngOnInit() {
    const id = this.route.snapshot.params['id'];
    this.eventoService.getEvento(id).subscribe(data => this.evento = data);
  }

  iscriviti() {
    this.eventoService.iscriviti(this.evento.id).subscribe({
      next: () => alert('Iscrizione completata!'),
      error: (err) => alert(err.error.error)
    });
  }
}
