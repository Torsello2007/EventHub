import { Component, inject } from '@angular/core';
import { CommonModule } from '@angular/common';
import { FormBuilder, ReactiveFormsModule, Validators } from '@angular/forms';
import { HttpClient, HttpHeaders } from '@angular/common/http';
import { environment } from '../../../environments/environment';
import { AuthService } from '../../core/services/auth.service';

@Component({
  selector: 'app-organizer-dashboard',
  standalone: true,
  imports: [CommonModule, ReactiveFormsModule],
  templateUrl: './organizer-dashboard.component.html'
})
export class OrganizerDashboardComponent {
  private fb = inject(FormBuilder);
  private http = inject(HttpClient);
  private auth = inject(AuthService);

  eventForm = this.fb.group({
    titolo: ['', Validators.required],
    descrizione: ['', Validators.required],
    data_evento: ['', Validators.required],
    luogo: ['', Validators.required],
    posti_disponibili: [0, Validators.required],
    categoria: ['', Validators.required],
    prezzo: [0, Validators.required]
  });

  selectedFile: File | null = null;

  onFileSelected(event: any) {
    this.selectedFile = event.target.files[0];
  }

  onSubmit() {
    const formData = new FormData();
    Object.keys(this.eventForm.value).forEach(key => {
      formData.append(key, (this.eventForm.value as any)[key]);
    });
    
    if (this.selectedFile) {
      formData.append('immagine', this.selectedFile);
    }

    const headers = new HttpHeaders().set('Authorization', `Bearer ${this.auth.getToken()}`);

    this.http.post(`${environment.apiUrl}/organizzatore/eventi`, formData, { headers })
      .subscribe(() => {
        alert('Evento creato!');
        this.eventForm.reset();
      });
  }
}
