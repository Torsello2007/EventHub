export interface Evento {
  id: number;
  titolo: string;
  descrizione: string;
  data_evento: string;
  luogo: string;
  posti_disponibili: number;
  categoria: string;
  prezzo: number;
  locandina_url?: string;
}
