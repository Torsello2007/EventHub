import { Injectable } from '@angular/core';
import Keycloak from 'keycloak-js';
import { environment } from '../../../environments/environment';

@Injectable({ providedIn: 'root' })
export class AuthService {
  private keycloak: Keycloak = new Keycloak({
    url: environment.keycloak.url,
    realm: environment.keycloak.realm,
    clientId: environment.keycloak.clientId
  });

  async init() {
    try {
      await this.keycloak.init({
        onLoad: 'check-sso',
        checkLoginIframe: false
      });
    } catch (error) {
      console.error('Errore Keycloak:', error);
    }
  }

  login() { this.keycloak.login(); }
  logout() { this.keycloak.logout({ redirectUri: window.location.origin }); }
  isLoggedIn() { return this.keycloak.authenticated || false; }
  getUsername() { return this.keycloak.tokenParsed?.['preferred_username']; }
  getToken() { return this.keycloak.token; }
  hasRole(role: string) { return this.keycloak.hasRealmRole(role); }
}