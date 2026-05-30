import { Component, OnInit, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { EventoService } from '../../core/services/evento.service';
import { RouterModule } from '@angular/router';

@Component({
  selector: 'app-my-tickets',
  standalone: true,
  imports: [CommonModule, RouterModule],
  templateUrl: './my-tickets.component.html'
})
export class MyTicketsComponent implements OnInit {
  private eventoService = inject(EventoService);
  biglietti: any[] = [];

  ngOnInit(): void {
    this.eventoService.getMieiBiglietti().subscribe(data => {
      this.biglietti = data;
    });
  }
}
